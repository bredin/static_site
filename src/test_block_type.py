import unittest
from block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("####### Not heading"), BlockType.HEADING)

    def test_code(self):
        code = """```
code block
```"""
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        code2 = """```
print('hi')
```"""
        self.assertEqual(block_to_block_type(code2), BlockType.CODE)

    def test_quote(self):
        quote = "> this is a quote\n> another line"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)
        not_quote = "> this is a quote\nnot a quote"
        self.assertNotEqual(block_to_block_type(not_quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)
        not_ul = "- item 1\nitem 2"
        self.assertNotEqual(block_to_block_type(not_ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)
        not_ol = "1. first\n3. third"
        self.assertNotEqual(block_to_block_type(not_ol), BlockType.ORDERED_LIST)
        not_ol2 = "1. first\n2. second\n2. third"
        self.assertNotEqual(block_to_block_type(not_ol2), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        para = "This is a paragraph.\nWith two lines."
        self.assertEqual(block_to_block_type(para), BlockType.PARAGRAPH)
        para2 = "Just one line."
        self.assertEqual(block_to_block_type(para2), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
