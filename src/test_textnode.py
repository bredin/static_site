import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Text A", TextType.PLAIN)
        node2 = TextNode("Text B", TextType.PLAIN)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_text_type(self):
        node1 = TextNode("Same text", TextType.PLAIN)
        node2 = TextNode("Same text", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Example", TextType.LINK, "http://example.com")
        node2 = TextNode("Example", TextType.LINK, "http://different.com")
        self.assertNotEqual(node1, node2)

    def test_equal_with_none_url(self):
        node1 = TextNode("Example", TextType.LINK)
        node2 = TextNode("Example", TextType.LINK)
        self.assertEqual(node1, node2)

    def test_equal_with_none_url_different_text(self):
        node1 = TextNode("Example", TextType.LINK)
        node2 = TextNode("Example", TextType.PLAIN)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()