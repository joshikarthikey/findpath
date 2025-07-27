import os

def main():
    root = input("Enter Root directory: ")
    root_path = get_dir(root)
    all_paths = find_all_paths(root_path)
    desired_file = input("Enter desired file: ")
    print(f"Found! File: {find_path(desired_file, all_paths)}")

def get_dir(root):
    while True:
        current_dir = os.getcwd()
        if os.path.basename(current_dir) == root:
            return current_dir
        elif current_dir == '/':
            raise FileNotFoundError("Requested directory not found")
        os.chdir("..")

def find_all_paths(root_path):
    paths = []

    current_dir = root_path
    current_dir_contents = os.listdir(current_dir)
    for path in current_dir_contents:
        if not os.path.isdir(path):
            paths.append(os.path.join(current_dir, path))
        else:
            paths.extend(find_all_paths(path))

    return paths

def find_path(desired_file, all_paths):
    requested_path = ""
    occurrences = 0
    for path in all_paths:
        if desired_file == os.path.basename(path):
            requested_path = path
            occurrences += 1
    if not requested_path:
        raise FileNotFoundError("Requested file not found")
    elif occurrences > 1:
        raise ValueError("More than one file found")

    return requested_path

if __name__ == "__main__":
    main()