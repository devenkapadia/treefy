from treefy.tree import BinaryTree

tree = BinaryTree(10)

lc = tree.add_node(tree.root, 5, is_left=True)
rc = tree.add_node(tree.root, 15, is_left=False)

llc = tree.add_node(lc, 3, is_left=True)
lrc = tree.add_node(lc, 7, is_left=False)

rrc = tree.add_node(rc, 5, is_left=False)

llrc = tree.add_node(llc, 12, is_left=False)

# rrlc = tree.add_node(rrc, 7, is_left=True)

# print(tree.root.left.is_leaf())

# print(tree.get_height(tree.root))

# print(tree.root)

# print(tree)


# traversal = tree.level_order_traversal(tree.root)
# print(traversal)

tree.print_tree(tree.root)
print(tree.preorder_traversal(tree.root))
print(tree.inorder_traversal(tree.root))
print(tree.postorder_traversal(tree.root))

# tree1 = BinaryTree()
# arr = [5, 1, 2, 11, 17, None, 3]
# tree1.generate_tree_from_array(arr)
# tree.print_tree(tree1.root)

# tree.attach_subtree(rc, tree1, is_left=True)
# print(tree.preorder_traversal(tree.root))
# print(tree.inorder_traversal(tree.root))
# print(tree.postorder_traversal(tree.root))
# tree.print_tree(tree.root)

def maximum_path_sum(tree):
    """
    Finds the maximum path sum in the binary tree.
    :param tree: The tree object.
    :return: Maximum path sum.
    """
    def helper(node):
        if node is None:
            return 0, float('-inf')  # (Max path from this node, Max path in subtree)
        
        # Recursive calls to left and right children
        left_single, left_max = helper(node.left)  # Correct recursive call: left child
        right_single, right_max = helper(node.right)  # Correct recursive call: right child
        
        # Max path from current node (single branch)
        single_path = max(node.value, node.value + left_single, node.value + right_single)
        
        # Max path sum including this node (both branches)
        max_path_through_node = max(single_path, node.value + left_single + right_single)
        
        # Max path in this subtree
        subtree_max = max(left_max, right_max, max_path_through_node)
        
        return single_path, subtree_max
    
    # Start the recursion from the root
    _, result = helper(tree.root)
    return result


# Register the maximum_path_sum function
tree.register_function("maximum_path_sum", maximum_path_sum)

# Call the function dynamically
result = tree.call_function("maximum_path_sum")

print(f"Maximum Path Sum: {result}")


def lca(tree, root, n1, n2):
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes in the binary tree.
    :param tree: The tree object.
    :param root: The root of the tree/subtree.
    :param n1: First node.
    :param n2: Second node.
    :return: The LCA of nodes n1 and n2.
    """
    def helper(node):
        # Base case: If node is None, return None
        if node is None:
            return None

        # If the current node matches either n1 or n2, return the node
        if node == n1 or node == n2:
            return node

        # Search for n1 and n2 in the left and right subtrees
        left = helper(node.left)
        right = helper(node.right)

        # If both left and right subtrees return non-None values,
        # then the current node is the LCA
        if left and right:
            return node

        # Otherwise, return the non-None value (either left or right)
        return left if left else right

    # Start the recursion from the root
    return helper(root)

tree.register_function("lca", lca)

lca_node = tree.call_function("lca", tree.root, rc, llrc)

if lca_node:
    print(f"LCA of {lc.value} and {llrc.value}: {lca_node.value}")
else:
    print("LCA not found")