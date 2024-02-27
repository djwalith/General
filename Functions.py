# This is a sample Python script.
import os

import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('JD')

def readexcel(name, index):
    df = pd.read_excel(name,index_col= index)
    return df

def readcsv(name, index):
    df = pd.read_csv(name,index_col= index)
    return df

def prime():
    count = 0
    x = int(input('Enter an integer:\t'))
    #corner cases
    if x <= 1:
        print("invalid")
        print("Please try again")
        return False
    #checking for the prime number
    for i in range(2,x):
        if(x%i == 0):
            count = count +1
            break
    #result
    if (count == 0):
        print("the number %d is prime" % x)
    else:
        print("the number %d is not prime" % x)


def oddeven():
    num = int(input('Enter an integer:\t'))
    if num == 0:
        print("invalid")
        return False
    num = int(round(num))
    if num%2 == 0:
        print("the number %s is even" % num)
    else:
        print("the number %s is odd" % num)

if __name__ == '__main__':
    print_hi('JD')
    oddeven()
    prime()

###################Combing multiple excels into one dataframe

def read_excel_files(folder_path):
    # Use glob to get a list of all Excel files in the specified folder
    excel_files = glob.glob(f"{folder_path}/*.xlsx")

    # Initialize an empty list to store DataFrames
    dfs = []

    # Loop through each Excel file and read it into a DataFrame
    for excel_file in excel_files:
        df = pd.read_excel(excel_file)
        dfs.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    return combined_df


if __name__ == "__main__":
    # Replace 'path/to/excel/files' with the actual path to your Excel files
    folder_path = os.getcwd()

    # Call the function to read and combine Excel files into a DataFrame
    combined_dataframe = read_excel_files(folder_path)

    # Print or further process the combined DataFrame as needed
    print(combined_dataframe)


###############

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
