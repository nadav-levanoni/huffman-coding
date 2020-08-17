def shift_up(lst, index):
    if index < 0:
        raise IndexError
    if index == 0:
        return lst
    if lst[index] < lst[(index - 1) // 2]:
        lst[index], lst[(index - 1) // 2] = lst[(index - 1) // 2], lst[index]
        return shift_up(lst, (index - 1) // 2)
    return lst


def shift_down(lst, index, end):
    if index >= end:
        return lst
    min_child = find_smaller_child(lst, index, end)
    if min_child is None:
        return lst
    if lst[index] > lst[min_child]:
        lst[index], lst[min_child] = lst[min_child], lst[index]
        return shift_down(lst, min_child, end)
    return lst


def find_smaller_child(lst, index, end):
    left = index * 2 + 1
    right = index * 2 + 2
    if left >= end:
        return None
    if right >= end:
        return left
    if lst[left] < lst[right]:
        return left
    return right


class MinPQ:

    def __init__(self, ary=None):
        if ary is None:
            self.arr = [None, None]
            self.capacity = 2
            self.num_items = 0
        else:
            self.arr = ary
            self.heapify(self.arr)
            self.capacity = len(self.arr)
            self.num_items = len(self.arr)

    def __eq__(self, other):
        temp = True
        for i in range(self.num_items):
            if self.arr[i] != other.arr[i]:
                temp = False
                break
        return self.num_items == other.num_items and temp and\
            self.capacity == other.capacity

    def __repr__(self):
        return "arr: " + str(self.arr) + " cap: " + str(self.capacity) +\
            " num_items: " + str(self.num_items)

    def heapify(self, lst):
        start = (len(lst) - 2) // 2
        end = len(self.arr)
        for i in range(start, -1, -1):
            lst = shift_down(lst, i, end)
            end -= 1
        self.arr = lst

    def insert(self, item):
        if self.capacity == self.num_items:
            self.enlarge()
        self.arr[self.num_items] = item
        self.num_items += 1
        self.arr = shift_up(self.arr, self.num_items - 1)

    def del_min(self):
        if self.num_items == 0:
            raise IndexError
        temp = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.arr = shift_down(self.arr, 0, self.num_items)
        self.num_items -= 1
        if self.num_items <= (self.capacity // 4) and self.capacity > 2:
            self.shrink()
        return temp

    def min(self):
        if self.is_empty():
            raise IndexError
        return self.arr[0]

    def is_empty(self):
        return self.num_items == 0

    def size(self):
        return self.num_items

    def enlarge(self):
        self.arr += ([None] * self.capacity)
        self.capacity *= 2

    def shrink(self):
        self.capacity //= 2
        temp = [None] * self.capacity
        for i in range(self.num_items):
            temp[i] = self.arr[i]
        self.arr = temp
