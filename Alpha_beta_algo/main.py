from ast import literal_eval
import sys

class GameNode:
    def __init__(self, name, value=0, parent=None):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class GameTree:
    def __init__(self):
        self.root = None

    def build_tree(self, data_list):
        self.root = GameNode(data_list[0])
        for elem in data_list[1:]:
            self.parse_subtree(elem, self.root)

    def parse_subtree(self, data, parent):
        if isinstance(data, tuple):
            leaf_node = GameNode(data[0], data[1])
            leaf_node.parent = parent
            parent.add_child(leaf_node)
            return

        tree_node = GameNode(data[0])
        tree_node.parent = parent
        parent.add_child(tree_node)
        for elem in data[1:]:
            self.parse_subtree(elem, tree_node)

def parse_data_as_list(fname):
    with open(fname, "r") as f:
        data_as_string = f.read()
        data_list = literal_eval(data_as_string)
    return data_list

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break  # Beta cutoff
        print(f"Max node - Value: {value} Alpha: {alpha} Beta: {beta}")
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cutoff
        print(f"Min node - Value: {value} Alpha: {alpha} Beta: {beta}")
        return value


def main():
    filename = sys.argv[1]
    data_list = parse_data_as_list(filename)
    data_tree = GameTree()
    data_tree.build_tree(data_list)
    
    print("Tree Structure:")
    print_tree(data_tree.root)
    
    result = alpha_beta(data_tree.root, 3, float('-inf'), float('inf'), True)
    print("\nOptimal value:", result)


def print_tree(node, level=0):
    if node:
        print("   " * level + "|__", node.name)
        for child in node.children:
            print_tree(child, level + 1)


if __name__ == "__main__":
    main()
