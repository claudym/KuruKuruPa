class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def opposite(dir1, dir2):
    opp_dict = {'NORTH': 'SOUTH', 'EAST': 'WEST'}
    if opp_dict.get(dir1, '') == dir2 or opp_dict.get(dir2, '') == dir1:
        return True
    return False 

def dirReduc(arr):
    if len(arr) <= 1:
        return arr
    
    l_list = LinkedList()
    head = Node(arr[0])
    l_list.head = head
    # populate linked list
    for i in range(len(arr) - 1):
        l_list.head.next = Node(arr[i + 1])
        l_list.head.next.prev = l_list.head
        l_list.head = l_list.head.next

    l_list.head = head
    # check for adjacent opposites
    while l_list.head is not None:
        if l_list.head.prev is not None:  # checking opposites in the back
            if opposite(l_list.head.prev.item, l_list.head.item):
                if l_list.head.prev.prev is not None:
                    l_list.head.prev.prev.next = l_list.head.next
                else:
                    head = l_list.head.next
                    if l_list.head.next is not None:
                        l_list.head.next.prev = None
                l_list.head = l_list.head.next
                continue
        if l_list.head.next is not None:
            if opposite(l_list.head.item, l_list.head.next.item):
                if l_list.head.next.next is not None:
                    l_list.head.next.next.prev = l_list.head.prev
                if l_list.head.prev is None:
                    head = l_list.head.next.next
                else:
                    l_list.head.prev.next = l_list.head.next.next
                l_list.head = l_list.head.next.next
                continue
        l_list.head = l_list.head.next
    
    # convert linked list back to array
    ary = []
    l_list.head = head
    while l_list.head is not None:
        ary.append(l_list.head.item)
        l_list.head = l_list.head.next
    return ary

def dirReduc_test(arr):
    if len(arr) <= 1:
        return arr
    # if len(arr) == 2:
    #     if opposite(arr[0], arr[1]):
    #         return []
    #     return arr
    
    l_list = LinkedList()
    head = Node(arr[0])
    l_list.head = head
    for i in range(len(arr) - 1):
        l_list.head.next = Node(arr[i + 1])
        l_list.head.next.prev = l_list.head
        l_list.head = l_list.head.next

    l_list.head = head
    while l_list.head is not None:
        # print(f'head: {l_list.head.item}')
        if l_list.head.prev is not None:  # checking opposites in the back
            if opposite(l_list.head.prev.item, l_list.head.item):
                if l_list.head.prev.prev is not None:
                    l_list.head.prev.prev.next = l_list.head.next
                else:
                    head = l_list.head.next
                    if l_list.head.next is not None:
                        l_list.head.next.prev = None
                # l_list.head.prev = l_list.head.prev.prev
                l_list.head = l_list.head.next
                continue
        if l_list.head.next is not None:
            # print(f'head-front: {l_list.head.item}')
            if opposite(l_list.head.item, l_list.head.next.item):
                # print(f'head-front-opposite: {l_list.head.item}')
                if l_list.head.next.next is not None:
                    l_list.head.next.next.prev = l_list.head.prev
                if l_list.head.prev is None:
                    head = l_list.head.next.next
                else:
                    l_list.head.prev.next = l_list.head.next.next
                l_list.head = l_list.head.next.next
                continue
        l_list.head = l_list.head.next
        

    # printing linked list -- debugging
    # one line
    print()
    l_list.head = head
    while l_list.head is not None:
        print(l_list.head.item, end=' ')
        l_list.head = l_list.head.next     
    print('\n')
    # detailed
    l_list.head = head
    while l_list.head is not None:
        if l_list.head.prev is not None:
            print(f'prev: {l_list.head.prev.item}')
        else:
            print(f'prev: {l_list.head.prev}')
        print(f'          item: {l_list.head.item}')
        if l_list.head.next is not None:
            print(f'next: {l_list.head.next.item}\n')
        else:
            print(f'next: {l_list.head.next}\n')
        l_list.head = l_list.head.next
    # convert back to array
    ary = []
    l_list.head = head
    while l_list.head is not None:
        ary.append(l_list.head.item)
        l_list.head = l_list.head.next
    return ary


# print(dirReduc([]))
# print(dirReduc(['NORTH']))
# print('1', dirReduc(['NORTH', 'WEST', 'EAST']))
# print('1', dirReduc(['WEST', 'EAST', 'NORTH']))
# print('2', dirReduc(['NORTH', 'EAST', 'WEST', 'SOUTH', 'WEST', 'EAST']))
# print('3', dirReduc(['NORTH', 'SOUTH']))
# print('4', dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# print('5', dirReduc(['WEST', 'WEST', 'SOUTH', 'WEST', 'SOUTH', 'SOUTH', 'EAST', 'EAST', 'EAST', 'WEST', 'WEST', 'NORTH', 'WEST']))