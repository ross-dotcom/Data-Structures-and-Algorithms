import random

def binary_search(some_list, n):
    
    first = 0
    last = len(some_list)-1
    found = False
    
    while (first<=last and not found):
        mid = (first + last)//2
        if some_list[mid] == n:
            found = True
        else:
            if n < some_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
                
    return found

if __name__ == '__main__':
    
    r_list = random.sample(range(1, 101), 10)
    
    print(binary_search(r_list, 25))