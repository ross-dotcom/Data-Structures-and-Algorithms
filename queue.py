list_of_names = ['Adam', 'Bianca', 'Carol', 'Denver', 'Eve', 'Felicia', 'Gail']
queue_limit = 5

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = [None]*self.max_size
        self.rear = -1
        self.front = 0
    
    def get_max_size(self):
        return self.max_size
    
    def is_full(self):
        return self.rear == self.max_size-1
    
    def enqeue(self, data):
        if(self.is_full()):
            print("Queue is full. No enqeue possible for: %s" % (data))
        else:
            self.rear+=1
            self.elements[self.rear] = data
            print(data)
            
    def display(self):
        for i in range(0, self.rear+1):
            print('Inserted at #%s %s' % (i+1, self.elements[i]))
            
    def is_empty(self):
        if (self.rear == -1 or self.front == self.max_size):
            return True
        else:
            return False
        
    def dequeue(self):
        if self.is_empty():
            print('Queue is already empty.')
        else:
            data=self.elements[self.front]
            self.front+=1
            return data
            
if __name__ == '__main__':
    
    queue1 = Queue(queue_limit)
    
    print('List of names: %s\nEN-QUEUE...' % (list_of_names))
    for e in list_of_names:
        queue1.enqeue(e)
        
    queue1.display()
    
    print('DE-QUEUE...')
    while not queue1.is_empty():
       print('Removed: %s' % (queue1.dequeue()))