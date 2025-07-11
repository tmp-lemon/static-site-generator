from textnode import TextNode, TextType


def main():
    node = TextNode("Testing text", TextType.LINK, "https://google.com")
    print(node)


main()