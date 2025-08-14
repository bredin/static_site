from textnode import TextNode, TextType
from typing import List

from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    """
    Splits text nodes in old_nodes by the given delimiter, converting the delimited text to the given text_type.
    Non-text nodes are left unchanged.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        parts = text.split(delimiter)
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                # Outside delimiter: keep as TEXT
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Inside delimiter: convert to text_type
                new_nodes.append(TextNode(part, text_type))
    return new_nodes


def split_nodes_image(old_nodes: list) -> list:
    """
    Splits text nodes in old_nodes by markdown images, converting them to TextType.IMAGE nodes.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = list(extract_markdown_images(text))
        if not matches:
            new_nodes.append(node)
            continue
        idx = 0
        for alt, url in matches:
            # Find the image markdown in the text
            img_md = f"![{alt}]({url})"
            start = text.find(img_md, idx)
            if start > idx:
                # Add preceding text as TEXT
                new_nodes.append(TextNode(text[idx:start], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            idx = start + len(img_md)
        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list) -> list:
    """
    Splits text nodes in old_nodes by markdown links, converting them to TextType.LINK nodes.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        matches = list(extract_markdown_links(text))
        if not matches:
            new_nodes.append(node)
            continue
        idx = 0
        for anchor, url in matches:
            link_md = f"[{anchor}]({url})"
            start = text.find(link_md, idx)
            if start > idx:
                new_nodes.append(TextNode(text[idx:start], TextType.TEXT))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            idx = start + len(link_md)
        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))
    return new_nodes

def text_to_textnodes(text: str) -> list:
    """
    Converts markdown text to a list of TextNode objects, handling bold, italic, code, images, and links.
    """
    nodes = [TextNode(text, TextType.TEXT)]
    # Order: images, links, code, bold, italic
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    # Remove empty text nodes
    nodes = [n for n in nodes if not (n.text_type == TextType.TEXT and n.text == "")]
    return nodes