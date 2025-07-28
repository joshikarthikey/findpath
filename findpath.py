import os


class FindPath:
    def __init__(self, root=None):
        self.root = root
        self.root_path = None
        self.all_paths = None
        self.file = None
        self.your_path = None
        self.current_dir = os.getcwd()

    def find(self, desired_file: str) -> str:
        self.file = desired_file
        if self.root == "/":
            self.root_path = self.root
        while True:
            if os.path.basename(self.current_dir) == self.root:
                self.root_path = self.current_dir
                break
            elif self.current_dir == "/":
                raise FileNotFoundError("Requested directory not found")
            os.chdir("..")

        FindPath.find_all_paths(self, self.root_path)
        desired_path = ""
        occurrences = 0
        for path in self.all_paths:
            if self.file == os.path.basename(path):
                desired_path = path
                occurrences += 1
        if not desired_path:
            raise FileNotFoundError("Requested file not found")
        elif occurrences > 1:
            raise ValueError("More than one file found")

        self.your_path = desired_path
        return self.your_path

    def find_all_paths(self, root_path: str) -> list:
        paths = []

        current_dir = root_path
        current_dir_contents = os.listdir(current_dir)
        for path in current_dir_contents:
            if not os.path.isdir(os.path.join(current_dir, path)):
                paths.append(os.path.join(current_dir, path))
            else:
                paths.extend(
                    FindPath.find_all_paths(self, os.path.join(current_dir, path))
                )

        self.all_paths = paths
        return self.all_paths

    @property
    def root(self):
        if self._root is None:
            raise AttributeError("Root is not set")
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    @property
    def root_path(self):
        if self._root_path is None:
            raise AttributeError("Root is not set")
        return self._root_path

    @root_path.setter
    def root_path(self, value):
        self._root_path = value

    @property
    def all_paths(self):
        if self._all_paths is None:
            raise AttributeError("Root is not set")
        return self._all_paths

    @all_paths.setter
    def all_paths(self, value):
        self._all_paths = value

    @property
    def file(self):
        if self._file is None:
            raise AttributeError("File is not set")
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    @property
    def your_path(self):
        if self._your_path is None:
            raise AttributeError("Your path is not set")
        return self._your_path

    @your_path.setter
    def your_path(self, value):
        self._your_path = value
