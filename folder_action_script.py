# Import required libraries
# Import OS related functions
import os
from os import path

# --------------------------------------------------------------------------------------

# Function to create new folder/dir
# Require the working dir to be the desired path!
def folder_make(folder_name):
    if not path.exists(folder_name):
        os.mkdir(folder_name)
        # Debug: After creating folder, print a message!
        print(folder_name + ' created!')
    else:
        # If the folder already exists, print a message!
        print(folder_name + ' existed!')


# Function to create new file
# Require the working dir to be the desired path!
def file_make(file_name):
    if not path.isfile(file_name):
        f = open(file_name, "w")
        f.close()
        # Debug: After creating the file, print a message!
        print(file_name + ' created!')
    else:
        # Debug: If file already exists, print a message!
        print(file_name + ' existed!')


# Function to change working dir and create new dir
def folder_manip(parent, input_name):
    # Debug: Print top working dir
    print(parent)

    # Edit here to change to the desired dir
    # Change cwd to /data_process
    folder_make("data_process")
    os.chdir(parent + '//data_process')
    # End of change dir

    # Create the desired folder
    folder_make(input_name)
    # Change cwd to the new dir
    os.chdir("./{}".format(input_name))

    # Edit this part to create new sub-directories
    # Create sub-directories
    folder_make("your_folder")
    # End of creating sub-dirs

    # Return to the parent dir
    os.chdir(parent)


# Function to create desired files
def file_manip(parent, sub_dir_name):
    # Print top working dir
    print(parent)

    # Edit here to change to the desired dir
    # Change cwd to /data_process
    os.chdir(parent + '//data_process//{}'.format(sub_dir_name))
    # End of change dir

    # Edit here to create desired files
    file_make("edit_file_name_here.txt")
    # End of create file

    # Return to the parent dir
    os.chdir(parent)


# Remove all files in the folder
def remove_folder_content(address):
    # List through all available files in the address, then execute the function
    for filename in os.listdir(address):
        if path.exists(path.join(address, filename)) & path.isfile(path.join(address, filename)):
            os.remove(path.join(address, filename))


# Remove everything within the folder and itself
def remove_all_content(address):
    # Loop until all is finished
    while True:
        # List all folder & file under the dir
        # Put in check under a loop through all item listed
        for filename in os.listdir(address):
            # Check if the item is a dir
            if path.isdir(path.join(address, filename)):
                # If the dir is empty, if yes, clear the dir
                # through check if the list of item under it is empty
                if len(os.listdir(path.join(address, filename))) == 0:
                    os.rmdir(path.join(address, filename))
                # If the dir is not empty, recurse the function
                # with the top dir is the current dir
                else:
                    remove_all_content(path.join(address, filename))
            else:
                # The item is a file
                os.remove(path.join(address, filename))
        # Check if the original dir is empty or not
        # If empty, clear the original dir
        if len(os.listdir(address)) == 0:
            break

    # Remove the top dir:
    os.rmdir(address)
    # Debug: After clearing, print a message!
    print("{} has been removed!".format(address))


# --------------------------------------------------------------------------------------
# Test commands
# folder_manip(parent= os.getcwd(), input_name= "test-folder-1")
# file_manip(parent= os.getcwd(), sub_dir_name= "test-folder-1")
remove_all_content(address= os.getcwd() + '//data_process//test-folder-1')