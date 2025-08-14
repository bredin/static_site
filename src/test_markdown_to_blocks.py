import unittest
from split_nodes import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_blocks(self):
        md = """# Heading

This is a paragraph.

- Item 1\n- Item 2\n- Item 3"""
        blocks = markdown_to_blocks(md)
        expected = [
            "# Heading",
            "This is a paragraph.",
            "- Item 1\n- Item 2\n- Item 3"
        ]
        self.assertEqual(blocks, expected)

    def test_leading_trailing_whitespace(self):
        md = "\n\n  Block 1  \n\nBlock 2\n\n  \nBlock 3  \n\n"
        blocks = markdown_to_blocks(md)
        expected = ["Block 1", "Block 2", "Block 3"]
        self.assertEqual(blocks, expected)

    def test_empty_blocks(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\n"
        blocks = markdown_to_blocks(md)
        expected = ["Block 1", "Block 2"]
        self.assertEqual(blocks, expected)

    def test_single_block(self):
        md = "Just one block, no double newlines."
        blocks = markdown_to_blocks(md)
        expected = ["Just one block, no double newlines."]
        self.assertEqual(blocks, expected)

    def test_all_empty(self):
        md = "\n\n\n\n"
        blocks = markdown_to_blocks(md)
        expected = []
        self.assertEqual(blocks, expected)

if __name__ == "__main__":
    unittest.main()
