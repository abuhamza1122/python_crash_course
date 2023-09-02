# os module is a built-in module in python that provides functions for interacting in the operating system.
# DEMO:
import os 

def list_files_in_current_directory():
    """
    print the name of all the files in the current directory 
    return:
        none
        """
    files = os.listdir()
    print(f"files in current directory:")
    for file_name in files:
        print(file_name)

if __name__=="__main__":
      list_files_in_current_directory()

