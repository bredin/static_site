import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ], matches)

    def test_no_images(self):
        matches = extract_markdown_images("No images here!")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ], matches)

    def test_links_and_images(self):
        text = "A [link](https://a.com) and ![img](https://b.com/img.png)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)
        self.assertListEqual([("link", "https://a.com")], links)
        self.assertListEqual([("img", "https://b.com/img.png")], images)

    def test_no_links(self):
        matches = extract_markdown_links("No links here!")
        self.assertListEqual([], matches)

    def test_nested_brackets(self):
        text = "[text [with] brackets](https://a.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("text [with] brackets", "https://a.com")], matches)

if __name__ == "__main__":
    unittest.main()
