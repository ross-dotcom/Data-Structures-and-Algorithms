class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        #Inserts a new node next to the current node when the current node is 'None'
        while current_node.next != None: #Traversing through the list
            current_node = current_node.next
        current_node.next = new_node
        
    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None: #Traversing through the list
            total += 1
            current_node = current_node.next
        return total
    
    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None: #Traversing through the list
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)
        
    def get(self, index):
        if index >= self.length():
            print('ERROR: index out of range!')
            return
        current_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_idx == index:
                return current_node.data
            current_idx += 1
            
    def erase(self, index):
        if index >= self.length():
            print('ERROR: index out of range!')
            return
        current_idx = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_idx == index:
                last_node.next = current_node.next
                return
            current_idx += 1
            
my_list = LinkedList()
print('Display empty linked list:')
my_list.display()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print('Display appended linked list:')
my_list.display()
print('Length: %s' % (my_list.length()))
print('Get element at index [3]: %s' % (my_list.get(3)))
print('Erase element at index [4]')
my_list.erase(4)
print('Display linked list without erased element:')
my_list.display()