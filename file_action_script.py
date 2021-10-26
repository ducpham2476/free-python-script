# Import required libraries
# OS related functions
import os
from os import path


# ---------------------------------------------------------------------------------------
# Delete all content from a file
def file_clear_content(parent_path, file_path, file_name):

    # Open the file with rewrite permission
    f_clear_file = open(parent_path + "\\{}\\{}".format(file_path, file_name), "w+")
    # File is cleared, close the file
    f_clear_file.close()


# Delete a specific line within the file
def file_clear_specific_line(parent_path, file_path, file_name, line_to_delete):

    # Create the file path
    file_address = parent_path + "\\{}\\{}".format(file_path, file_name)

    # Modify the string to be deleted
    line_to_delete = line_to_delete + "\n"

    # Open the file
    with open(file_address, "r+") as f_delete_specific_string:
        read_content = f_delete_specific_string.readlines()
        f_delete_specific_string.seek(0)

        for line in read_content:
            if line != line_to_delete and line != "\n":
                f_delete_specific_string.write(line)

        f_delete_specific_string.truncate()


# Remove special characters from the filename, prevent unwanted behaviours
def file_name_standardize(string):
    # Include removing white space " ", hyphen "-" and underscore "_"
    # Remove white space: " "
    modded_string = string.split(" ")
    result_string = "".join(modded_string)
    # Remove hyphen: "-"
    modded_string = result_string.split("-")
    result_string = "".join(modded_string)
    # Remove underscore: "_"
    modded_string = result_string.split("_")
    result_string = "".join(modded_string)

    # Return final string
    return result_string


# Specific use: Read all lines from file, return as an one-dimension array
# If the file is not available, do nothing
# If the file is empty, return a flag that's empty
# If the file has contents, return each line of the file as an element in an one-dimension array
def read_line_from_file(parent_path, file_path, file_name):
    # Initiate return values
    file_flag = 0
    available_data = []

    # Open file
    # Avoid using static addresses
    file_address = parent_path + "\\{}\\{}".format(file_path, file_name)
    file_open = open(file_address, 'r+')
    if os.stat(file_address).st_size == 0:
        # Indicate if the file is empty or not
        # If the file is empty, return the flag value as 1
        file_flag = 1
        # The available data is null
        available_data = ""

        return available_data, file_flag
    # If the file is not empty
    else:
        # Create a temporary string
        string_x = ""
        # Initiate a new list, get the value from the list
        lis = [line.split() for line in file_open]
        # Debug:
        # print(lis)
        # Get file length (number of lines in file)
        file_length = len(lis)

        for index in range(file_length):
            # Check if the line has multiple white spaces
            flag_multiple_white_space = len(lis[index])
            # If there are multiple white spaces, join all elements of the array as one
            if flag_multiple_white_space > 1:
                temp = ' '.join(lis[index])
                string_x = temp
            # Else just get a new line as the value of the element
            else:
                for value in lis[index]:
                    string_x = value
            # Finish writing the value of a line to an element of an one-dimension array
            available_data.append(string_x)

    file_open.close()

    return available_data, file_flag


# Append a new line to the file
def file_append(parent_path, file_path, file_name, line_to_write):
    # Open the file:
    file_address = parent_path + "\\{}\\{}".format(file_path, file_name)
    file_open = open(file_address, 'a+')

    # Write the desired line
    file_open.write(line_to_write)
    file_open.write("\n")

    # Close the file
    file_open.close()


# Test script

# parent_path = os.getcwd()
# current_path = ""
# file_name = "test.txt"
#
# lines, flag = read_line_from_file(parent_path, current_path, file_name)
# for index in range(len(lines)):
#     print(lines[index])