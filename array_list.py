class ArrayList:
    def __init__(self, cap=2, num=0, ary=None):
        if ary is None:
            ary = ([None, None])
        self.capacity = cap
        self.num_items = num
        self.arr = ary

    def __eq__(self, other):
        return (isinstance(other, ArrayList)
                and self.num_items == other.num_items
                and self.capacity == other.capacity
                and self.arr == other.arr
                )

    def __repr__(self):
        return ('list: ' + (' '.join(str(i) for i in self.arr)) + '\ncapacity: ' +
                str(self.capacity) + '\nnumber of items: ' + str(self.num_items))


#

def enlarge(lst):
    lst.arr += ([None] * lst.capacity)
    lst.capacity *= 2
    return lst


def shrink(lst):
    lst.capacity //= 2
    temp = [None] * lst.capacity
    for i in range(lst.num_items):
        temp[i] = lst.arr[i]
    lst.arr = temp
    return lst


def insert(lst, val, idx):
    if lst.capacity == lst.num_items:
        lst = enlarge(lst)
    for i in range(lst.capacity - 2, idx - 1, -1):
        lst.arr[i + 1] = lst.arr[i]
    lst.arr[idx] = val
    lst.num_items += 1
    return lst


def get(lst, idx):
    """get an item stored at the index indicated by the integer idx
    """
    if idx >= lst.num_items:
        raise IndexError
    return lst.arr[idx]


def contains(lst, val):
    for i in lst.arr:
        if i == val:
            return True
    return False


def search(lst, val):
    count = 0
    for i in lst.arr:
        if i == val:
            return count
        count += 1
    return None


def remove(lst, val, index=None):
    if index is None:
        index = search(lst, val)
    if index is None:
        return lst
    for i in range(index, lst.num_items - 1):
        lst.arr[i] = lst.arr[i + 1]
    lst.num_items -= 1
    if lst.num_items <= (lst.capacity // 4) and lst.capacity > 2:
        lst = shrink(lst)
    return lst


def pop(lst, idx):
    if idx >= lst.num_items:
        raise IndexError
    val = lst.arr[idx]
    lst = remove(lst, val, idx)
    return lst, val


def size(lst):
    return lst.num_items
