class Quick:	
	def partition(start, end, array):

		pivot_index = start
		pivot = array[pivot_index]
		
		while start < end:
			
			while start < len(array) and array[start] <= pivot:
				start += 1
				
			while array[end] > pivot:
				end -= 1
			
			if(start < end):
				array[start], array[end] = array[end], array[start]
		
		array[end], array[pivot_index] = array[pivot_index], array[end]
		
		return end
		
	def sort(start, end, array):
		
		if (start < end):
			
			p = Quick.partition(start, end, array)
			
			Quick.sort(start, p - 1, array)
			Quick.sort(p + 1, end, array)
			
if __name__ == '__main__':
	arr = [ 10, 7, 8, 9, 1, 5 ]
	print('Given array is:')
	print(arr)
	
	Quick.sort(0, len(arr) - 1, arr)

	print('Sorted array is:')
	print(arr)
	