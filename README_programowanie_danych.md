
Readme for the provided Python script
This Python script reads data from text files containing currency exchange rates for various currencies, and loan information from another text file. 
It then calculates the value of each loan in the given currency on the date of the loan, and saves the results as a list of tuples in a JSON file.

Required Packages
This script requires the following packages to be installed:

numpy
datetime
json

Functionality
The script contains two main functions:

kursy(plik) - Reads in currency exchange rate data from a text file with tab-separated values and returns a dictionary of exchange rates for a given currency.
pozyczki(data_path) - Reads in loan information from a text file and returns a list of lists containing the loan date, borrower name, loan amount, and currency.
The script also defines a helper function Substring(record, start_index, end_index, alpha) that extracts a substring from a given record, 
starting at a specified index and ending at another specified index. The alpha argument indicates whether the substring should contain only 
alphabetic characters or only numeric characters.

Finally, the script converts the loan information into a numpy array and calculates the value of each loan in the given currency on the date of the loan. 
It saves the results as a list of tuples containing the borrower name, loan date, and loan value in a JSON file.
