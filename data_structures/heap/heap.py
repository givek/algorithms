class BinaryMaxHeap:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return self.elements

    def __repr__(self):
        return self.elements

    def max_heapify(self, unordered_list, i):
        left = (2 * i) + 1
        right = (2 * i) + 2

        # If the element has no left child, then it won't have a right child either,
        # because in heaps we insert elements from left to right.
        if left >= len(unordered_list):
            return unordered_list

        # If the element has no right child, check if the max heap property is satisfied with the left child.
        if right >= len(unordered_list):
            if unordered_list[i] < unordered_list[left]:
                unordered_list[i], unordered_list[left] = (
                    unordered_list[left],
                    unordered_list[i],
                )

            return unordered_list

        # Check if the max heap property is satisfied if the element has both left and right children.
        # If not, replace the root element with the child with the greater priority.
        if (
            unordered_list[i] < unordered_list[left]
            or unordered_list[i] < unordered_list[right]
        ):

            if unordered_list[left] < unordered_list[right]:
                unordered_list[i], unordered_list[right] = (
                    unordered_list[right],
                    unordered_list[i],
                )

                # repeat the process of max heapify on the child with whom the element was exchanged.
                return self.max_heapify(unordered_list, right)
            else:
                unordered_list[i], unordered_list[left] = (
                    unordered_list[left],
                    unordered_list[i],
                )

                return self.max_heapify(unordered_list, left)

        return unordered_list

    def build_max_heap(self, unordered_list):
        # To build a max heap from an unordered list,
        # start performing the max_heapify routine on elements with index n/2 -> 0,
        # as elements with an index greater than n/2 will be leaf nodes.
        for i in reversed(range((len(unordered_list) // 2))):
            self.max_heapify(unordered_list, i)

        self.elements = unordered_list
        return unordered_list

    def get_max_element(self):
        return self.elements[0]

    def remove_max_element(self):
        # exchange the max element with the last element.
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        element = self.elements.pop(-1)

        # perform max heapify on the 0th index to maintain the max heap property.
        self.max_heapify(self.elements, 0)
        return element

    def insert_element(self, element):

        # insert the element at the last.
        self.elements.append(element)

        element_index = len(self.elements) - 1

        # keep exchanging the inserted element with its parent if its value is greater.
        while element_index > 0:
            parent_index = (element_index - 1) // 2

            if self.elements[element_index] > self.elements[parent_index]:
                self.elements[element_index], self.elements[parent_index] = (
                    self.elements[parent_index],
                    self.elements[element_index],
                )

                element_index = parent_index
            else:
                break


def main():
    h = BinaryMaxHeap()

    unordered_list = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

    print(h.build_max_heap(unordered_list))

    print(h.get_max_element())

    print(h.remove_max_element())

    h.insert_element(40)
    print(h.elements)


if __name__ == "__main__":
    main()
