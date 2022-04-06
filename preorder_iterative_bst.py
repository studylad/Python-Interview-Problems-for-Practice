def preOrderTraversal(root):
    stack = []
    stack.insert(0, root)
    while stack:
        current = stack.pop()
        print(current.value)

        right = current.right
        if right is not None:
            stack.insert(0, right)

        left = current.left
        if left is not None:
            stack.insert(0, left)
