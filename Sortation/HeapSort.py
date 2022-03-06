class Heap:
    def heapify(arr, n, i):
        largest = i  
        l = 2 * i + 1   
        r = 2 * i + 2     
    

        if l < n and arr[largest] < arr[l]:
            largest = l
    

        if r < n and arr[largest] < arr[r]:
            largest = r
    
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
    
            Heap.heapify(arr, n, largest)
    
    
    
    def sort(arr):
        n = len(arr)
    
        for i in range(n//2 - 1, -1, -1):
            Heap.heapify(arr, n, i)
    
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            Heap.heapify(arr, i, 0)
 
 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Sorted array is")
    print(arr)

    Heap.sort(arr)
    print("Sorted array is")
    print(arr)