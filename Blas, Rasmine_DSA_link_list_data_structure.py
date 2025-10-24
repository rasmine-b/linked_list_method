class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        """Print friendly step chain ending with X"""
        current = self.head
        if current is None:
            print("X (No more steps!)")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("X")

    def to_pylist(self):
        """Return Python list of node data (useful for debugging)"""
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

    # a) remove_beginning(self)
    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    # b) remove_at_end(self)
    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed = self.head.data
            self.head = None
            return removed
        current = self.head
        while current.next.next:
            current = current.next
        removed = current.next.data
        current.next = None
        return removed

    # c) remove_at(self, data)
    def remove_at(self, data: str):
        if self.head is None:
            return None
        # If head matches
        if self.head.data == data:
            removed = self.head.data
            self.head = self.head.next
            return removed
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None: 
            return None
        removed = current.next.data
        current.next = current.next.next
        return removed

    # add at end
    def add(self, data: str):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


def setup_sample_steps():
    L = LinkedList()
    L.add("A. Prepare")
    L.add("B. Cook rice")
    L.add("C. Place on mat")
    L.add("D. Roll")
    L.add("E. Eat")
    return L


def normalize_step_input(inp: str):
    """User may input 'A' or 'a' or 'A.' or 'A. Prepare' -> normalize to full step if possible."""
    inp = inp.strip()
    if not inp:
        return ""
    letter = inp.upper()
    if len(letter) == 1 and letter in "ABCDE":
        mapping = {
            "A": "A. Prepare",
            "B": "B. Cook rice",
            "C": "C. Place on mat",
            "D": "D. Roll",
            "E": "E. Eat",
        }
        return mapping[letter]
    return inp


if __name__ == "__main__":
    steps = setup_sample_steps()

    print("STEP LIST")
    steps.display()

    print("\nRemoving beginning step...")
    removed = steps.remove_beginning()
    print("Removed:", removed)
    steps.display()

    print("\nRemoving end step...")
    removed = steps.remove_at_end()
    print("Removed:", removed)
    steps.display()

    print("\nRemoving specific step 'C. Place on mat'...")
    removed = steps.remove_at("C. Place on mat")
    print("Removed:", removed)
    steps.display()

    print("\nAdding new step 'E. Serve and enjoy'...")
    steps.add("E. Serve and enjoy")
    steps.display()

    print("\nFinal steps list:", steps.to_pylist())
