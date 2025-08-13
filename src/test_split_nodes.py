import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_multiple_code(self):
        node = TextNode("A `b` c `d` e", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("b", TextType.CODE),
            TextNode(" c ", TextType.TEXT),
            TextNode("d", TextType.CODE),
            TextNode(" e", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_bold(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_italic(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_no_delimiter(self):
        node = TextNode("No special text here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("No special text here", TextType.TEXT)]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_non_text_nodes(self):
        class DummyNode:
            pass
        node = DummyNode()
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_unclosed_delimiter(self):
        node = TextNode("This is `unclosed code", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("unclosed code", TextType.CODE),
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = []
        self.assertEqual(result, expected)

"""     def test_nested_delimiters(self):
        node = TextNode("**bold _and italic_**", TextType.TEXT)
        # First split bold, then italic
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("bold ", TextType.BOLD),
            TextNode("and italic", TextType.ITALIC),
            TextNode("", TextType.BOLD),
        ]
        self.assertEqual([(n.text, n.text_type) for n in nodes], [(n.text, n.text_type) for n in expected]) """

if __name__ == "__main__":
    unittest.main()
