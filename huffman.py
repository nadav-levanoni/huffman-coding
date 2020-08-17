class HuffmanNode:
    """Node in a huffman tree
    Attributes:
        freq : frequency of a character
        char : a character
        left : pointer to left node
        right : pointer to right node
    """

    def __init__(self, frequency, char=None, left=None, right=None):
        self.freq = frequency
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.freq == other.freq and self.char == other.char and self.left == other.left and self.right == other.right

    def __repr__(self):
        return "freq: " + str(self.freq) + " char ord: " + str(ord(self.char))

    def __lt__(self, other):
        """overriding built in less than function. will enable direct logical comparison of nodes
        Args:
            other (HuffmanNode): huffman node being compared
        Returns:
            (boolean): self < other or ord check if equal
        """
        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            return ord(self.char) < ord(other.char)
        return False
