# LC 958 Check completeness of a binary tree
def is_complete_tree(root):
    stack = [root]
    flag = True
    while stack:
        new_stack = []
        for node in stack:
            if node.left and not flag:
                return False
            elif node.left:
                new_stack.append(node.left)
            else:
                flag = False

            if node.right and not flag:
                return False
            elif node.right:
                new_stack.append(node.right)
            else:
                flag = False
        stack = new_stack
    return True