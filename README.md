
# Game Playing : Alpha Beta Pruning algorithm impl 

- This code implements the alpha-beta pruning algorithm on a game tree represented by nested data. Here is a brief comment on what this code does:

- The code defines two classes: GameNode represents a node in the game tree, and GameTree represents the game tree itself.

- The build_tree method in the GameTree class takes a data list and builds the game tree by recursively parsing the nested data and creating the corresponding nodes and connections.

- The alpha_beta function implements the alpha-beta pruning algorithm. It takes a node, depth, alpha, beta, and a flag indicating if it's the maximizing player's turn. It recursively traverses the game tree using alpha-beta pruning to determine the optimal value for the current player.

- The main function is the entry point of the program. It reads the data from a file, builds the game tree, and then applies the alpha-beta pruning algorithm to find the optimal value. It also prints the tree structure using the print_tree function.

- The print_tree function recursively prints the tree structure in a top-to-bottom manner,(in the terminal it is show in left to right fashion) showing the name of each node and its children.

- Overall, this code parses the input data into a game tree, applies the alpha-beta pruning algorithm to find the optimal value, and prints the tree structure.

**Folder str:**
- Alpha_beta_algo: Above explanation.
- tic-tac-toe: Game without alpha beta pruning (not needed)

To run the code in the terminal run ``` python3 main.py data.txt ``` 
