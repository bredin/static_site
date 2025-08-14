from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    # Heading: starts with 1-6 # and a space
    if len(lines) == 1 and lines[0].startswith(tuple(f"{'#'*i} " for i in range(1, 7))):
        return BlockType.HEADING
    # Code block: starts and ends with ```
    if block.startswith("```") and block.endswith("````"):
        return BlockType.CODE
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    # Quote: every line starts with '>'
    if all(line.startswith(">") for line in lines if line.strip()):
        return BlockType.QUOTE
    # Unordered list: every line starts with '- '
    if all(line.startswith("- ") for line in lines if line.strip()):
        return BlockType.UNORDERED_LIST
    # Ordered list: every line starts with incrementing number + '. '
    num = 1
    ordered = True
    for line in lines:
        if not line.strip():
            continue
        prefix = f"{num}. "
        if not line.startswith(prefix):
            ordered = False
            break
        num += 1
    if ordered and num > 1:
        return BlockType.ORDERED_LIST
    # Default: paragraph
    return BlockType.PARAGRAPH
