# Class to hold student data
class Student:
    def __init__(self, id, name, course):
        self.id = id
        self.name = name
        self.course = course

# Node of AVL Tree
class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None
        self.height = 1

# AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else  0

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, student):
        self.root = self._insert(self.root, student)

    def _insert(self, node, student):
        if not node:
            return Node(student)
        if student.id < node.student.id:
            node.left = self._insert(node.left, student)
        elif student.id > node.student.id:
            node.right = self._insert(node.right, student)
        else:
            print("Student with this ID already exists.")
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        # Balancing
        if balance > 1 and student.id < node.left.student.id:
            return self.rotate_right(node)
        if balance < -1 and student.id > node.right.student.id:
            return self.rotate_left(node)
        if balance > 1 and student.id > node.left.student.id:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and student.id < node.right.student.id:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, id):
        return self._search(self.root, id)

    def _search(self, node, id):
        if not node:
            return None
        if id == node.student.id:
            return node.student
        elif id < node.student.id:
            return self._search(node.left, id)
        else:
            return self._search(node.right, id)

    def delete(self, id):
        self.root = self._delete(self.root, id)

    def _delete(self, node, id):
        if not node:
            return node

        if id < node.student.id:
            node.left = self._delete(node.left, id)
        elif id > node.student.id:
            node.right = self._delete(node.right, id)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.get_min(node.right)
            node.student = temp.student
            node.right = self._delete(node.right, temp.student.id)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.get_balance(node)

        # Rebalance
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def get_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self):
        print("\n All Enrollments (Sorted by ID):")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            s = node.student
            print(f"ID: {s.id}, Name: {s.name}, Course: {s.course}")
            self._inorder(node.right)

    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if not node:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)
def menu():
    print("\n------ Student Enrollment System (AVL Tree) ------")
    print("1. Insert student")
    print("2. Delete student by ID")
    print("3. Search student by ID")
    print("4. Show all students (In-order)")
    print("5. Count total students")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

def main():
    avl = AVLTree()

    while True:
        choice = menu()

        if choice == '1':
            try:
                id = int(input("Enter Enrollment ID: "))
                name = input("Enter Student Name: ")
                course = input("Enter Course Name: ")
                avl.insert(Student(id, name, course))
                print(" Student inserted.")
            except ValueError:
                print(" Invalid input. ID must be a number.")

        elif choice == '2':
            try:
                id = int(input("Enter Enrollment ID to delete: "))
                avl.delete(id)
                print("️ Student deleted (if existed).")
            except ValueError:
                print(" Invalid input.")

        elif choice == '3':
            try:
                id = int(input("Enter Enrollment ID to search: "))
                student = avl.search(id)
                if student:
                    print(f" Found: ID: {student.id}, Name: {student.name}, Course: {student.course}")
                else:
                    print(" Student not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == '4':
            avl.inorder()

        elif choice == '5':
            print(f" Total Students Enrolled: {avl.count()}")

        elif choice == '6':
            print(" Exiting. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
