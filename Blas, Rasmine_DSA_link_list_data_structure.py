class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    # a. remove_beginning(self)
    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    # b. remove_at_end(self)
    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data
        temp = self.head
        while temp.next.next:
            temp = temp.next
        removed_data = temp.next.data
        temp.next = None
        return removed_data

    # c. remove_at(self, data)
    def remove_at(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                removed_data = temp.next.data
                temp.next = temp.next.next
                return removed_data
            temp = temp.next
        return None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


# Example
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print("Before removal:")
sushi_preparation.display()

print("\nRemoved at beginning:", sushi_preparation.remove_beginning())
sushi_preparation.display()

print("\nRemoved at end:", sushi_preparation.remove_at_end())
sushi_preparation.display()

print("\nRemoved 'prepare':", sushi_preparation.remove_at("prepare"))
sushi_preparation.display()
