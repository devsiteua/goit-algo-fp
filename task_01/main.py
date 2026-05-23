class Node:
    def __init__(self, data=None):
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

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    def sort(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._insert_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _insert_sorted(self, sorted_head, new_node):
        if sorted_head is None or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head

    def to_list(self):
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def print_list(self):
        current = self.head

        if current is None:
            print("Empty list")
            return

        values = []
        while current:
            values.append(str(current.data))
            current = current.next

        print(" -> ".join(values))


def create_linked_list(values):
    linked_list = LinkedList()

    for value in values:
        linked_list.insert_at_end(value)

    return linked_list


def merge_sorted_lists(first_list, second_list):
    merged_list = LinkedList()

    current_first = first_list.head
    current_second = second_list.head

    while current_first and current_second:
        if current_first.data <= current_second.data:
            merged_list.insert_at_end(current_first.data)
            current_first = current_first.next
        else:
            merged_list.insert_at_end(current_second.data)
            current_second = current_second.next

    while current_first:
        merged_list.insert_at_end(current_first.data)
        current_first = current_first.next

    while current_second:
        merged_list.insert_at_end(current_second.data)
        current_second = current_second.next

    return merged_list


def run_tests():
    linked_list = create_linked_list([1, 2, 3, 4])
    linked_list.reverse()
    assert linked_list.to_list() == [4, 3, 2, 1]

    linked_list = create_linked_list([4, 2, 1, 5, 3])
    linked_list.sort()
    assert linked_list.to_list() == [1, 2, 3, 4, 5]

    first_list = create_linked_list([1, 3, 5])
    second_list = create_linked_list([2, 4, 6])
    merged_list = merge_sorted_lists(first_list, second_list)
    assert merged_list.to_list() == [1, 2, 3, 4, 5, 6]

    empty_list = LinkedList()
    empty_list.reverse()
    empty_list.sort()
    assert empty_list.to_list() == []


def main():
    run_tests()

    linked_list = create_linked_list([4, 2, 1, 5, 3])

    print("Original list:")
    linked_list.print_list()

    linked_list.reverse()
    print("\nReversed list:")
    linked_list.print_list()

    linked_list.sort()
    print("\nSorted list:")
    linked_list.print_list()

    first_list = create_linked_list([1, 3, 5])
    second_list = create_linked_list([2, 4, 6])

    print("\nFirst sorted list:")
    first_list.print_list()

    print("\nSecond sorted list:")
    second_list.print_list()

    merged_list = merge_sorted_lists(first_list, second_list)

    print("\nMerged sorted list:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
