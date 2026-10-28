import random, timeit
import matplotlib.pyplot as plt


class LinkedList:
    """
    A linked list.

    Includes most features from a regular list.
    """

    def __init__(self):
        self.next = None
        self.value = None

    def __getitem__(self, item):
        node = self

        for _ in range(item):
            node = node.next

        return node.value

    def append(self, value):
        """
        Adds a node at the end of the chain.
        :param value: the node's value
        :return: the inserted node
        """

        node = self

        while node.value is not None:
            node = node.next

        node.set_value(value)

        return node

    def __iter__(self):
        node = self

        while node.value is not None:
            yield node.value

            node = node.next

    def __len__(self):
        node = self
        length = 0

        while node.next is not None:
            node = node.next

            length += 1

        return length

    def set_value(self, value):
        if self.next is None:
            self.next = LinkedList()
            self.value = value

        else:
            self.next.set_value(value)

    def remove_this(self, _list):
        assert self in _list
        # loop over the list until you find this node, remove it

        if self == _list:
            # special case, root

            if _list.next is None:
                _list.value = None

            else:
                _list.remove_next()

        else:
            node = _list

            while node.next != self:
                node = node.next

            node.remove_next()

    def remove_item(self, item):
        assert item in self
        # loop over self until you find a node that contains as value item
        node = self

        while node.next is not item:
            node = node.next

            if node is None:
                return

        node.remove_next()

    def remove_next(self):
        self.next = self.next.next
        self.value = self.next.value


a = LinkedList()

a.append(1)
a.append('2')
a.append('4')
a.append(6)
a.append(8)
a.append('2')

for i in a:
    print(i)  # print "1\n2"

print('~`~`~`~`~`~`')
print(a[0], 6 in a)
print('~~~~~~~~~~~~')


def remove_dupes_in_my_LinkedList_class(the_LinkedList_object: LinkedList):
    """
    removes duplicates from the linked list
    for example if you input [1, 2, 6, 2] you would get [1, 2, 6];
    it stores the item and removes all others following it
    :param the_LinkedList_object: the linked list
    :returns: the linked list but with no dupes
    """
    seen_things = LinkedList()

    for item in the_LinkedList_object:
        if not item in seen_things:
            seen_things.append(item)

        else:
            the_LinkedList_object.remove_item(item)

    return seen_things

def remove_dupes_in_my_LinkedList_class2(the_LinkedList_object: LinkedList):
    """
    removes duplicates from the linked list
    for example if you input [1, 2, 6, 6, 2] you would get [1, 2, 6];
    it stores the item and removes all others following it
    :param the_LinkedList_object: the linked list
    :returns: the linked list but with no dupes
    """
    seen_things = set()

    for item in the_LinkedList_object:
        if not item in seen_things:
            seen_things.add(item)

        else:
            item.remove_next()

    return seen_things


for i in remove_dupes_in_my_LinkedList_class(a):
    print(i)

print('~' * 6)
# b = LinkedList()
# for _19 in range(25000):
#     b.append(chr(random.randint(36, 255)))
# print('done making list')
# print(''.join(b))
# for _ in range(len(b)):
#     c = random.choice(b)
#     b.remove_item(c)
#     print(c)

sizes = list(range(1, 5))
times = []
l = LinkedList()
for i in sizes:
    actual_size = 10 ** i
    # generate your list of actual size element
    for j in range(actual_size):
        l.append(chr(random.randint(32, 255)))

    times.append(timeit.timeit(lambda: remove_dupes_in_my_LinkedList_class(l), number=1))
print('times recorded')
fig, ax = plt.subplots()
ax.plot(sizes, times)
ax.set(xlabel='Characters', ylabel='Times',
       title='Processing times')
plt.show()
