"""
    Bubble sort algorithm.
"""
@profile
def bubble_sort(arr):
    
    length = len(arr)-1
    while length >= 1:
        position = 0
        for i in range(length):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                position = i
        length = position
        
    return arr

if __name__ == '__main__':

    my_array = [10, 4, 6, 8, 5, 2, 4, 6, 8, 9, 22]
    print(bubble_sort(my_array))
