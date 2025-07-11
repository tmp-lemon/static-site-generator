import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_eq_false(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.LINK, "https://www.testing.com")
        self.assertNotEqual(node1, node2)

    def test_eq_link(self):
        node1 = TextNode("This is a text node", TextType.LINK, "https://www.testing.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.testing.com")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.testing.com")
        self.assertEqual(
            "TextNode(This is a text node, link, https://www.testing.com)",
            repr(node)
        )


if __name__ == "__main__":
    unittest.main()
