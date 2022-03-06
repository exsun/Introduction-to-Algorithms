class Insertion:   
    def sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


if __name__=='__main__':
    
    arr = [12, 5, 36, 18, 7, 1, 52]
    print("Given array is", end="\n")
    print(arr)

    Insertion.sort(arr)
    print("Sorted array is", end="\n")
    print(arr)


