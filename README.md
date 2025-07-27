# FindPath

FindPath provides a structured and safe way 
to search for files in Python projects without
hardcoding absolute paths. This class-based 
tool starts from the current working directory 
and moves upward in the directory tree to 
locate a user-defined root directory. 
Once the root is found, it scans all files in 
the directory tree rooted at that location 
to find the file you're looking for.

### Key Features:

* Automatically navigates to the user-defined root directory.
* Recursively scans all subdirectories and files from the root.
* Raises informative exceptions when the root or desired file is not found.
* Prevents ambiguity by detecting multiple matches of the desired file.
* Clean, object-oriented design with property validation.

### Use Cases:

* Ideal for structured projects where a specific file (like config, license, or metadata) must be dynamically located.
* Helpful in deployment scripts, testing frameworks, or automated workflows where relative locations might shift.

```python
from findpath import FindPath

finder = FindPath()
finder.root = "my_project"
file_path = finder.find("test.png")
print(f"File found at: {file_path}")
```


### Exceptions

* FileNotFoundError: Raised if the root directory or the desired file is not found.
* ValueError: Raised if multiple files with the same name are found.
* AttributeError: Raised if required attributes are accessed before being set.

### Ideal Use Case

FindPath is ideal for projects that need
to dynamically locate configuration files,
logs, or other resources in deeply nested
directory structures. It is especially useful
when the relative or absolute path to a file
is unknown, but the file name is known.