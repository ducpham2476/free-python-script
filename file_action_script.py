# Import required libraries
# OS related functions
import os
from os import path


# ---------------------------------------------------------------------------------------
# Delete all content from a file
def file_clear_content(parent, dir_name, file_name):

    # Open the file with rewrite permission
    f_clear_file = open(parent + "\\{}\\{}".format(dir_name, file_name), "w+")
    # File is cleared, close the file
    f_clear_file.close()


def file_clear_specific_content(parent, dir_name, file_name, string_to_delete):
    # Create the file path
    file_path = parent + "\\{}\\{}".format(dir_name, file_name)

    # Modify the string to be deleted
    string_to_delete = string_to_delete + "\n"

    # Open the file
    with open(file_path, "r+") as f_delete_specific_string:
        read_content = f_delete_specific_string.readlines()
        f_delete_specific_string.seek(0)

        for line in read_content:
            if line != string_to_delete and line != "\n":
                f_delete_specific_string.write(line)

        f_delete_specific_string.truncate()