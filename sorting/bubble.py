def bubble(numbers):
	n = len(numbers)
	# traverse through all elements in the array
	for i in range(n):
		for j in range(0, n-i-1):
			if numbers[j] > numbers[j+1]:
				temp = numbers[j]
				numbers[j] = numbers[j + 1]
				numbers[j + 1] = temp

	return numbers;
