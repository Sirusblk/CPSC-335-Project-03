// Project 03
// By: Maira Ahmad & David McLaren
// Due: 04/18/14
#include <chrono>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// PROTOTYPES
vector<string> read_lines(string file_name);

// MAIN FUNCTION
int main(int argc, char const *argv[])
{
	//Variables
	string file_name = "";
	int num_lines = 0;

	if (argc < 3)
	{
		cout<<"Error : You must supply a file name and number of lines\n";
	}
	else
	{
		file_name = argv[1];
		num_lines = atoi(argv[2]);
	}

	//Start Counting
	auto start = chrono::high_resolution_clock::now();

	//Read in lines
	auto lines = read_lines(file_name);

	//Print Head

	//Sort List

	//Print Sorted Head

	//Stop Counting
	auto end = chrono::high_resolution_clock::now();

	int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
	double seconds = microseconds / 1E6;
	cout << "Elapsed time: " << seconds << " seconds" << endl;
	return 0;
}

// FUNCTIONS
vector<string> read_lines(string file_name)
{
	vector<string> list;

	return list;
}
