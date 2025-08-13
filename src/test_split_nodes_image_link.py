import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link

class TestSplitNodesImageAndLink(unittest.TestCase):
    def test_split_nodes_image_basic(self):
        node = TextNode("This is ![img](https://a.com/img.png) text", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "https://a.com/img.png"),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_split_nodes_image_multiple(self):
        node = TextNode("A ![one](url1) and ![two](url2)", TextType.TEXT)
        result = split_nodes_image([node])
        expected = [
            TextNode("A ", TextType.TEXT),
            TextNode("one", TextType.IMAGE, "url1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.IMAGE, "url2"),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_split_nodes_image_none(self):
        node = TextNode("No images here", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

    def test_split_nodes_link_basic(self):
        node = TextNode("This is [a link](https://a.com) text", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "https://a.com"),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_split_nodes_link_multiple(self):
        node = TextNode("[one](url1) and [two](url2)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("one", TextType.LINK, "url1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.LINK, "url2"),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_split_nodes_link_none(self):
        node = TextNode("No links here", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_split_nodes_link_and_image(self):
        node = TextNode("[link](url) and ![img](imgurl)", TextType.TEXT)
        # First split images, then links
        nodes = split_nodes_image([node])
        nodes = split_nodes_link(nodes)
        expected = [
            TextNode("link", TextType.LINK, "url"),
            TextNode(" and ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "imgurl"),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in nodes], [(n.text, n.text_type, n.url) for n in expected])

    def test_split_nodes_link_nested_brackets(self):
        node = TextNode("[text [with] brackets](https://a.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("text [with] brackets", TextType.LINK, "https://a.com"),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

if __name__ == "__main__":
    unittest.main()
