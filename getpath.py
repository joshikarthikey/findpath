import os

class GetPath:
    def __init__(self):
        self.root = None
        self.root_path = None
        self.all_paths = None
        self.desired_file = None
        self.desired_path = None
        self.current_dir = os.getcwd()

    def find(self, desired_file):
        self.desired_file = desired_file
        if self.root == '/':
            self.root_path = self.root
        while True:
            if os.path.basename(self.current_dir) == self.root:
                self.root_path =  self.current_dir
                break
            elif self.current_dir == '/':
                raise FileNotFoundError("Requested directory not found")
            os.chdir("..")

        GetPath.find_all_paths(self, self.root_path)
        desired_path = ""
        occurrences = 0
        for path in self.all_paths:
            if self.desired_file == os.path.basename(path):
                desired_path = path
                occurrences += 1
        if not desired_path:
            raise FileNotFoundError("Requested file not found")
        elif occurrences > 1:
            raise ValueError("More than one file found")

        self.desired_path = desired_path
        return desired_path


    def find_all_paths(self, root_path):
        paths = []

        current_dir = root_path
        current_dir_contents = os.listdir(current_dir)
        for path in current_dir_contents:
            if not os.path.isdir(os.path.join(current_dir, path)):
                paths.append(os.path.join(current_dir, path))
            else:
                paths.extend(GetPath.find_all_paths(self, os.path.join(current_dir, path)))

        self.all_paths =  paths
        return paths









