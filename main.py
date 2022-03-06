from Sortation.BubbleSort import Bubble
from Sortation.InsertionSort import Insertion
from Sortation.MergeSort import Merge
from Sortation.QuickSort import Quick
from Sortation.SelectionSort import Selection
from Sortation.HeapSort import Heap


def main():

    arr = [10, 103, 2, 19, 44]
    print(f"Given array is: {arr}")
    print()

    print("Bubble Sort:")
    Bubble.sort(arr)
    print(arr, end="\n")
    print()


    print("Insertion Sort:")
    Insertion.sort(arr)
    print(arr, end="\n")
    print()

    print("Merge Sort:")
    Merge.sort(arr)
    print(arr, end="\n")
    print()

    print("Selection Sort:")
    Selection.sort(arr)
    print(arr, end="\n")
    print()

    print("Heap Sort:")
    Heap.sort(arr)
    print(arr, end="\n")
    print()

    print("Quick Sort:")
    Quick.sort(0, len(arr) - 1, arr)
    print(arr, end="\n")
    print()

if __name__ == '__main__':
    main()