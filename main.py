#Get root dir name
#Go to root dir name
    #Throw error if root dir name not found
#Find all possible paths
    #If two files with same name found, throw Error
    #If no matching file found, throw Error
#Return file path as str
import os

def main():
    root = input("Enter Root directory: ")
    root_path = get_dir(root)

def get_dir(root):
    while True:
        current_dir = os.getcwd()
        if os.path.basename(current_dir) == root:
            return current_dir
        elif current_dir == '/':
            raise FileNotFoundError("Requested directory not found")
        os.chdir("..")

if __name__ == "__main__":
    main()