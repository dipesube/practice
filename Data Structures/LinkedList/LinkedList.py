class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = new_node
            
    def size(self):
        current = self.head
        size = 0
        while (current.next != None):
            size += 1
            current = current.next
        return size

    def display(self):
        elems = []
        current = self.head
        while (current.next != None):
            current = current.next
            elems.append(current.data)
        print(elems)

    def get(self, index):
        if (index >= self.size()):
            print("Index out of bounds")
            return None
        cur_index = 0
        current = self.head
        while True:
            current = current.next
            if cur_index == index:
                return current.data
            cur_index += 1

    def remove(self, index):
        if (index >= self.size()):
            print("Index out of bounds")
            return None
        cur_index = 0
        current = self.head
        while True:
            last_node = current
            current = current.next
            if (cur_index == index):
                last_node.next = current.next
                return
            cur_index+=1
