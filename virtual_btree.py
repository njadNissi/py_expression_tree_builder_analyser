import graphviz

def preorder_traversal(root, dot):
    if root:
        dot.node(str(root.data), label=str(root.data))
        if root.left:
            dot.edge(str(root.data), str(root.left.data), style='dotted')
        if root.right:
            dot.edge(str(root.data), str(root.right.data), style='dotted')
        preorder_traversal(root.left, dot)
        preorder_traversal(root.right, dot)


def visualize_binary_tree(root):
    dot_preorder = graphviz.Digraph(comment='Inorder Traversal')
    preorder_traversal(root, dot_preorder)
    dot_preorder.render('Preorder Traversal', view=True, format='png')