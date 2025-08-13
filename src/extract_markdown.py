import re

def extract_markdown_images(text):
    """
    Extracts markdown images from text. Returns a list of (alt, url) tuples.
    """
    pattern = r'!\[([^\]]+)\]\(([^\)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """
    Extracts markdown links from text. Returns a list of (anchor, url) tuples.
    Ignores images (which start with !).
    """
    # This regex supports one level of nested brackets in the anchor text
    pattern = r'(?<!\!)\[((?:[^\[\]]+|\[[^\[\]]*\])+)\]\(([^\)]+)\)'
    return re.findall(pattern, text)
