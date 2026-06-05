class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Вставка элемента в BST"""
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def search(root, target):
    """Поиск элемента в BST"""
    if root is None:
        return False

    if root.value == target:
        return True

    if target < root.value:
        return search(root.left, target)

    return search(root.right, target)


def inorder(root):
    """Симметричный обход дерева"""
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


def count_leaves(root):
    """Подсчет листьев"""
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaves(root.left) + count_leaves(root.right)


# Пример работы программы

root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Элементы дерева по возрастанию:")
inorder(root)

print("\n")

target = int(input("Введите число для поиска: "))

if search(root, target):
    print("Элемент найден.")
else:
    print("Элемент не найден.")

print("Количество листьев:", count_leaves(root))