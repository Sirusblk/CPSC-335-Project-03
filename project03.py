# Project 03
# By: Maira Ahmad & David McLaren
# Due: 04/18/14
import sys
import time

## FUNCTIONS ##
def read_lines(file_name, num_lines):
	with open(file_name) as f:
		lines = [line.strip('\n') for line in f]

	lines = lines[0:num_lines-1]
	print("Read the first "+str(num_lines)+" from "+file_name)
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


## MAIN ##
def main():
	if len(sys.argv) <= 2: 			# python3 project03.py
		print( "Error : You must supply a file name and number of lines")
		sys.exit(1)
	else: 							# python3 project03.py <filename.txt> <n lines>
		file_name = sys.argv[1]
		num_lines = int(sys.argv[2])

	start = time.perf_counter()		# Start Counting

	# Read in lines & print head
	data = read_lines(file_name, num_lines)
	print("First 10 words: " + str(data[0:10]))

	# Sort lines
	print("Selection sort...")
	selection_sort(data)
	end = time.perf_counter()		# Stop Counting

	# Print new head
	print("First 10 words: " + str(data[0:10]))

	# Print elapsed time
	print("Elapsed time: " + str(end - start))


if __name__ == '__main__':
	# unittest.main()
	main()
