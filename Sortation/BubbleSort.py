class Bubble:
    def sort(arr):
        n = len(arr)

        for i in range(n):

            for j in range(0, n-i-1):

                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1], arr[j]



if __name__ == '__main__':
    arr = [15, 58, 92, 10, 76, 46, 38, 19]
    print("Given array is: ")
    print(arr)

    Bubble.sort(arr)
    print("Sorted array is: ")
    print(arr)