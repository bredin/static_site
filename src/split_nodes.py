from textnode import TextNode, TextType
from typing import List

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
