import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Text")])

    def test_parent_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_parent_with_props(self):
        node = ParentNode("div", [LeafNode("span", "Hello")], {"class": "container"})
        self.assertEqual(node.to_html(), "<div><span>Hello</span></div>")

    def test_nested_parent_nodes(self):
        child_node = ParentNode("span", [LeafNode("b", "Bold")])
        parent_node = ParentNode("div", [child_node, LeafNode("i", "Italic")])
        self.assertEqual(parent_node.to_html(), "<div><span><b>Bold</b></span><i>Italic</i></div>")

    def test_multiple_children(self):
        node = ParentNode("ul", [
            ParentNode("li", [LeafNode(None, "Item 1")]),
            ParentNode("li", [LeafNode(None, "Item 2")]),
        ])
        self.assertEqual(node.to_html(), "<ul><li>Item 1</li><li>Item 2</li></ul>")

if __name__ == "__main__":
    unittest.main()
