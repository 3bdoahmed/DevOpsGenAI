from pathlib import Path # is module for handling filesystem paths


class ProjectScanner:
    """
    Responsible for scanning a project directory
    and collecting basic information.
    """
# this constructor takes a string argument project_path which is the path to the project directory
    def __init__(self, project_path: str): 
        self.project_path = Path(project_path)

# this method checks if the project directory exists and is a directory
    def exists(self) -> bool: 
        return self.project_path.exists() and self.project_path.is_dir()

# this method Scan the project folder and return project information.
    def scan(self) -> dict:
        if not self.exists():
            raise FileNotFoundError(
                f"Project not found: {self.project_path}"
            )
        
        files = []

        # Read only files in project root
        for item in self.project_path.iterdir():
            if item.is_file():
                files.append(item.name)

        return {
            "project_name": self.project_path.name,
            "project_path": str(self.project_path),
            "files": sorted(files)
        }