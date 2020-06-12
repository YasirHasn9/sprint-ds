class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

# at what current node are we ?
        current = self.head

# valid node
        while current:
            if current.get_value() == value:
                return True

# update the current node
            current = current.get_next()

# if we reached this point then we dont have a valid node
        return False

#     # def reverse_list(self, node, prev):
#     #     prev = None
#     #     cur = self.head
#     #     while cur:
#     #         next_head = cur.next
#     #         cur.next = None
#     #         prev = cur
#     #         cur = next_head
#     #     self.head = prev

#         # # myList = []
#         # # if self.head:
#         # #     myList.append(node)

#         # # return list.reverse(myList)
#         # # check the head
#         # # and then store the head in Temporarily variable
#         # # get the next node
#         # if self.head:
#         #     # Temporarily head
#         #     current_head = self.head
#         #     # we need the next node value of the current_head
#         #     next_head = current_head.get_value()
#         #     # now we need to make the head's next to none so we
#         #     # can swipe to the end

#         #     # now the current head is floating points to nothing
#         #     current_head.next = None

#         #     # iterate over the head of the nodes
#         #     while next_head:
#         #         # get the pervious head
#         #         prev = current_head

#         #         # now we can make the current head to next_head
#         #         current_head = next_head
#         #         next_head = current_head.get_next()
#         #         current_head.next_node = prev
#         #         self.head = current_head

    def reverse_list(self, node, prev):
        # make previous node == None
        prev = None
        # get the current head
        head = self.head
        while head:
            # since the head is not None
            # make the next node the node that was the next of the current head
            next_node = head.next_node

            # now the next node needs to be None
            head.next_node = prev
            # make the pervious node the next head
            prev = head

            # the new head is the next node that was the previous node
            head = next_node
        self.head = prev
