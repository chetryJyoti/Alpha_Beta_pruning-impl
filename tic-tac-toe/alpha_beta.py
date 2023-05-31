class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def is_terminal_node(self):
        return len(self.children) == 0
    
    def heuristic_value(self):
        return self.value


def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or node.is_terminal_node():
        return node.heuristic_value(), [node.value]  # Return both the value and the path
    
    if maximizingPlayer:
        value = float('-inf')
        path = []
        for child in node.children:
            child_value, child_path = alpha_beta(child, depth - 1, alpha, beta, False)
            if child_value > value:
                value = child_value
                path = [node.value] + child_path  # Update the path
            alpha = max(alpha, value)
            print("Max node - Value:", value, "Alpha:", alpha, "Beta:", beta)
            if beta <= alpha:
                print("Max node - Pruning at value:", value)
                break  # beta cutoff
        return value, path
    else:
        value = float('inf')
        path = []
        for child in node.children:
            child_value, child_path = alpha_beta(child, depth - 1, alpha, beta, True)
            if child_value < value:
                value = child_value
                path = [node.value] + child_path  # Update the path
            beta = min(beta, value)
            print("Min node - Value:", value, "Alpha:", alpha, "Beta:", beta)
            if beta <= alpha:
                print("Min node - Pruning at value:", value)
                break  # alpha cutoff
        return value, path


def print_tree(node, level=0):
    if node:
        print("   " * level + "|__", node.value)
        for child in node.children:
            print_tree(child, level + 1)


# Create the tree
root = Node(0)
node1 = Node(5)
node2 = Node(3)
node3 = Node(6)
node4 = Node(2)
node5 = Node(0)
node6 = Node(1)
node7 = Node(5)
node8 = Node(31)
node9 = Node(6)
node10 = Node(32)
node11 = Node(10)
node12 = Node(1)

root.add_child(node1)
root.add_child(node2)
root.add_child(node3)
node1.add_child(node4)
node1.add_child(node5)
node2.add_child(node6)
root.add_child(node7)
root.add_child(node8)
root.add_child(node9)
node1.add_child(node10)
node1.add_child(node11)
node2.add_child(node12)


# Print the tree
print("Tree Structure:")
print_tree(root)

print()

# Run alpha-beta pruning
result, path = alpha_beta(root, 3, float('-inf'), float('inf'), True)
print("\nOptimal value:", result)
print("Path to the optimal value:", path)
