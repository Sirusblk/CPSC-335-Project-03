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


## MAIN ##
def main():
	if len(sys.argv) <= 2: 			# python3 project03.py
		print( "Error : You must supply a file name and number of lines")
		sys.exit(1)
	else: 							# python3 project03.py <filename.txt> <n lines>
		file_name = sys.argv[1]
		num_lines = int(sys.argv[2])

	# Read in lines
	data = read_lines(file_name, num_lines)

	start = time.perf_counter()		# Start Counting
	# Do something here...
	end = time.perf_counter()		# Stop Counting

if __name__ == '__main__':
	# unittest.main()
	main()