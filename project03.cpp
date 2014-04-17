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
vector<string> read_lines(string file_name, int count);

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
	auto lines = read_lines(file_name, num_lines);

	//Print Head
	cout << "First 10 words: [\'" << lines[0];
	for (int i = 1; i < 10; ++i)
	{
		cout << "\', \'" << lines[i];
	}
	cout << "\']\n" << endl;

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
vector<string> read_lines(string file_name, int count)
{
	vector<string> list;
	string temp;
	ifstream infile;

	infile.open(file_name);

	for (int i = 0; i < count; ++i)
	{
		infile >> temp;
		list.push_back(temp);
	}

	infile.close();

	cout << "Read the first " << count << " lines from " << file_name << endl;

	return list;
}
