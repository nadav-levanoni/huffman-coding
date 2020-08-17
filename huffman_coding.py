from huffman import HuffmanNode
from min_pq import MinPQ


def cnt_freq(filename):
    """returns a list of 256 integers correlating to the frequencies each character in the file
    Args:
        filename (String) : the file that is being encoded
    Returns:
        lst (list) : list of frequencies of characters
    """
    reader = open(filename, "r")
    tokens = reader.readlines()
    reader.close()
    lst = [0] * 256
    for i in range(len(tokens)):
        for j in range(len(tokens[i])):
            lst[ord(tokens[i][j])] += 1
    return lst


def create_huff_tree(lst):
    """returns root node of a Huffman Tree
    Args:
        lst (list) : the list of frequencies of characters
    returns:
        mpq (MinPQ) : a huffman tree created using the lst argument
    """
    nodes = []
    for i in range(len(lst)):
        if lst[i] != 0:
            nodes.append(HuffmanNode(lst[i], chr(i)))
    mpq = MinPQ(nodes)
    while mpq.size() > 1:
        temp1 = mpq.del_min()
        temp2 = mpq.del_min()
        min_key = chr(min(ord(temp1.char), ord(temp2.char)))
        new_node = HuffmanNode(temp1.freq + temp2.freq, min_key, temp1, temp2)
        mpq.insert(new_node)
    return mpq.del_min()


def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose index corresponds to ascii code of a letter.
    Args:
        root_node (MinPQ) : the root node of a huffman tree
    returns:
        codes (list) : a list of huffman codes
    """
    lst = [None] * 256
    codes = code_helper(lst, "", root_node)
    return codes


def code_helper(lst, code, node):
    """Helps find the list of codes for a huffman tree
    Args:
        lst (list) : the list of huffman codes (empty at the start)
        code (string) : the current code being created
        node (MinPQ) : the current node being decoded (starts with root)
    returns:
        lst (list) : a list of huffman codes
    """
    if node.left:
        lst = code_helper(lst, code + "0", node.left)
    if node.right:
        lst = code_helper(lst, code + "1", node.right)
    if node.left is None and node.right is None:
        lst[ord(node.char)] = code
        return lst
    return lst


def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    Args:
        in_file (string) : the file being read from
        out_file (string) : the file being written to
    """
    raw = ""
    reader = open(in_file, "r")
    tokens = reader.readlines()
    reader.close()
    for i in range(len(tokens)):
        raw += tokens[i]
    lst = cnt_freq(in_file)
    tree = create_huff_tree(lst)
    codes = create_code(tree)
    writer = open(out_file, "w")
    # writer.write(str(lst) + "\n")
    for i in raw:
        writer.write(codes[ord(i)])
    writer.close()


def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decode encoded_file and write the decoded text to decode_file.
    This function calls create_huff_tree function.
    Args:
        list_of_freqs (lst) : list of frequencies ever index correlates with a ASCII character
        encoded_file (string) : location of the encoded file
        decode_file (string) : location of the decoded file
    """
    tree = create_huff_tree(list_of_freqs)
    # codes = create_code(tree)
    reader = open(encoded_file, "r")
    tokens = reader.readlines()
    reader.close()
    tokens = tokens[0]
    decoded = ""
    index = 0
    while index < len(tokens):
        # temp1, temp2 = decode_helper("", tokens, index, tree)
        temp1, temp2 = decoding_helper(tokens, index, tree)
        decoded += temp1
        index = temp2
    writer = open(decode_file, "w")
    writer.write(decoded)
    writer.close()


def decoding_helper(tokens, index, tree):
    """A helper function that helps decode a huffman tree's code
    Args:
         tokens (lst) : a list of the contents read from the file
         index (int) : used to keep track of index being looked at
         tree (MinPQ) : the node being observed
    returns:
        temp.char (string) : the character of the decoded code
        index (int) : the index of the decoded character
    """
    temp = tree
    while temp.left is not None and temp.right is not None:
        if tokens[index] == "0":
            temp = temp.left
            index += 1
        elif tokens[index] == "1":
            temp = temp.right
            index += 1
    return temp.char, index