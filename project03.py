# Project 03
# By: Maira Ahmad & David McLaren
# Due: 04/18/14
import sys
import time
import random

## FUNCTIONS ##
def read_lines(file_name, num_lines):
	with open(file_name) as f:
		lines = [line.strip('\n') for line in f]

	# Correct max length
	if (num_lines > len(lines)):
		num_lines = len(lines)

	lines = lines[0:num_lines-1]
	print("\nRead the first "+str(num_lines)+" words from "+file_name)
	return lines


def selection_sort(data):
	smallest = 0
	for i in range(0, len(data)-1):
		smallest = i
		for j in range(i + 1, len(data)):
			if (data[j] < data[smallest]):
				smallest = j

		if (smallest != i):
			data[i], data[smallest] = data[smallest], data[i]


def inplace_quick_sort(data):
	inplace_quick_sort_range(data, 0, len(data))
	return data

def inplace_quick_sort_range(data, s, e):
	if (e-s) > 1:
		lt_end, gt_start = inplace_partition(data, s, e)
		inplace_quick_sort_range(data, s, lt_end)
		inplace_quick_sort_range(data, gt_start, e)

def inplace_partition(data, s, e):
	pivot = data[random.randint(s, e-1)]

	# first pass: partition L into LT, GE zones
	lt_end = s
	ge_start = e
	while lt_end < ge_start:
		if data[lt_end] < pivot:
			lt_end += 1
		elif data[ge_start-1] >= pivot:
			ge_start -= 1
		else:
			swap(data, lt_end, ge_start-1)
			lt_end += 1

# second pass: partition GE into EQ, GT zones
	eq_end = lt_end
	gt_start = e
	while eq_end < gt_start:
		if data[eq_end] == pivot:
			eq_end += 1
		elif data[gt_start-1] > pivot:
			gt_start -= 1
		else:
			swap(data, eq_end, gt_start-1)
			eq_end += 1

	return lt_end, gt_start

def swap(data, i, j):
	data[i], data[j] = data[j], data[i]


## MAIN ##
def main():
	if len(sys.argv) <= 2: # python3 project03.py
		print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <text file> <n>')
		sys.exit(1)
	else: # python3 project03.py <filename.txt> <n lines>
		file_name = sys.argv[1]
		num_lines = int(sys.argv[2])

	
	# Read in lines & print head
	data = read_lines(file_name, num_lines)

	print("First 10 words of " + file_name + ": "+ str(data[0:10]))

	start = time.perf_counter()	# Start Counting
	# Sort lines
	print("\nSelection sort...")
	selection_sort(data)
	end = time.perf_counter()	# Stop Counting

	# Print new head
	print("Sorted First 10 words of " + file_name + ": "+ str(data[0:10]))

	# Print elapsed time
	diff = end - start
	print("Elapsed time:", format(diff, '.5f'), "seconds")
	print("\n")

	
	start = time.perf_counter()	# Start Counting
	# Sort lines
	print("In-Place Randomized Quick sort...")
	inplace_quick_sort(data)
	end = time.perf_counter()	# Stop Counting

	# Print new head
	print("Sorted First 10 words of " + file_name + ": "+ str(data[0:10]))

	# Print elapsed time
	diff = end - start
	print("Elapsed time:", format(diff, '.5f'), "seconds")
	print("\n")

if __name__ == '__main__':
# unittest.main()
	main()
