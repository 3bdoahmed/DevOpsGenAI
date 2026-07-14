from pathlib import Path

# This class is responsible for writing content to files in a specified project directory.
class Writer:
# this constructor takes a string argument project_path which is the path to the project directory
    def __init__(self, project_path):
        self.project_path = Path(project_path)
# this method writes the given content to a file with the specified filename in the project directory
    def write(self, filename, content):
        file_path = self.project_path / filename
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{filename} created successfully.")