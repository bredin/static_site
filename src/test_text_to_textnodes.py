import unittest
from textnode import TextNode, TextType
from split_nodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_full_markdown(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_only_text(self):
        text = "Just plain text."
        result = text_to_textnodes(text)
        expected = [TextNode("Just plain text.", TextType.TEXT)]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_only_bold(self):
        text = "**bold**"
        result = text_to_textnodes(text)
        expected = [TextNode("bold", TextType.BOLD)]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_only_italic(self):
        text = "_italic_"
        result = text_to_textnodes(text)
        expected = [TextNode("italic", TextType.ITALIC)]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_only_code(self):
        text = "`code`"
        result = text_to_textnodes(text)
        expected = [TextNode("code", TextType.CODE)]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_only_image(self):
        text = "![alt](url)"
        result = text_to_textnodes(text)
        expected = [TextNode("alt", TextType.IMAGE, "url")]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_only_link(self):
        text = "[anchor](url)"
        result = text_to_textnodes(text)
        expected = [TextNode("anchor", TextType.LINK, "url")]
        self.assertEqual([(n.text, n.text_type, n.url) for n in result], [(n.text, n.text_type, n.url) for n in expected])

    def test_empty(self):
        text = ""
        result = text_to_textnodes(text)
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
