import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "bold", "https://different-url.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_instance(self):
        node = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, "This is not a TextNode instance")

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://example.com")
        expected_repr = "TextNode(This is a text node, bold, https://example.com)"
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()