from htmlnode import ParentNode, LeafNode
from split_nodes import markdown_to_blocks, text_to_textnodes
from block_type import block_to_block_type, BlockType
from text_to_html_node import text_node_to_html_node

# Helper: convert a string of text to a list of HTMLNodes (inline parsing)
def text_to_children(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        # Special handling: if all lines in block are headings, treat each as heading
        lines = [line for line in block.split('\n') if line.strip()]
        if lines and all(block_to_block_type(line) == BlockType.HEADING for line in lines):
            for line in lines:
                level = len(line.split(" ")[0])
                tag = f"h{level}"
                text = line.lstrip('#').lstrip()
                children.append(ParentNode(tag, text_to_children(text)))
        elif block_type == BlockType.PARAGRAPH:
            para_text = ' '.join(line.strip() for line in block.split('\n'))
            children.append(ParentNode("p", text_to_children(para_text)))
        elif block_type == BlockType.HEADING:
            # Single heading line
            line = block.strip()
            level = len(line.split(" ")[0])
            tag = f"h{level}"
            text = line.lstrip('#').lstrip()
            children.append(ParentNode(tag, text_to_children(text)))
        elif block_type == BlockType.CODE:
            # Remove only the first and last line's triple backticks
            code_lines = block.split('\n')
            if code_lines[0].startswith('```'):
                code_lines = code_lines[1:]
            if code_lines and code_lines[-1].startswith('```'):
                code_lines = code_lines[:-1]
            code_content = '\n'.join(code_lines)
            # Ensure trailing newline
            if not code_content.endswith('\n'):
                code_content += '\n'
            code_node = LeafNode("code", code_content)
            pre_node = ParentNode("pre", [code_node])
            children.append(pre_node)
        elif block_type == BlockType.QUOTE:
            quote_lines = [line[1:].lstrip() for line in block.split('\n')]
            quote_text = '\n'.join(quote_lines)
            children.append(ParentNode("blockquote", text_to_children(quote_text)))
        elif block_type == BlockType.UNORDERED_LIST:
            items = [line[2:] for line in block.split('\n') if line.strip()]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(ParentNode("ul", li_nodes))
        elif block_type == BlockType.ORDERED_LIST:
            items = [line[line.find('. ')+2:] for line in block.split('\n') if line.strip()]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            children.append(ParentNode("ol", li_nodes))
    return ParentNode("div", children)
