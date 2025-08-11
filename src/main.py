from textnode import TextNode, TextType

def main():
    # Create a new TextNode object with some dummy values
    node = TextNode("Example Text", TextType.LINK, "http://example.com")
    
    # Print the object
    print(node)

if __name__ == "__main__":
    main()