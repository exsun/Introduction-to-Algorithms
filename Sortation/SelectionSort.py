class Selection:

    def sort(arr):
        for i in range(len(arr)):
            
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j


            arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = [6, 99, 77, 44, 55, 0]

    print("Given array is:")
    print(arr)

    Selection.sort(arr)
    print('Sorted array is:')
    print(arr)
