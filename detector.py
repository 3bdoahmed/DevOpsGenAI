import json # thos module is used to parse the package.json file
from pathlib import Path # is module for handling filesystem paths

# this class is responsible for detecting the programming language, framework, and package manager
class ProjectDetector:

# this constructor takes a string argument project_path which is the path to the project directory
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)

    def detect(self):
        # create a result dictionary with default values.
        result = {
            "language": "Unknown",
            "framework": "Unknown",
            "package_manager": "Unknown"
        }
        # var to hold the path to the package.json.
        package_json = self.project_path / "package.json"

        if package_json.exists(): # if package.json exists, then the project is a Node.js project.
            result["language"] = "Node.js" 
            result["package_manager"] = "npm"
            with open(package_json, "r", encoding="utf-8") as f: # open package.json
                data = json.load(f) # convert content of package.json to Dictionary

            deps = {} # create an empty Dictionary

            deps.update(data.get("dependencies", {}))
            deps.update(data.get("devDependencies", {}))

            if "next" in deps:
                result["framework"] = "Next.js"

            elif "react" in deps:
                result["framework"] = "React"

            elif "express" in deps:
                result["framework"] = "Express"

            elif "@nestjs/core" in deps:
                result["framework"] = "NestJS"

            elif "vite" in deps:
                result["framework"] = "Vite"

            else:
                result["framework"] = "Node.js"

            return result

        if (self.project_path / "requirements.txt").exists():
            result["language"] = "Python"
            result["framework"] = "Python"
            result["package_manager"] = "pip"
            return result

        if (self.project_path / "pyproject.toml").exists():
            result["language"] = "Python"
            result["framework"] = "Python"
            result["package_manager"] = "poetry"
            return result

        if (self.project_path / "pom.xml").exists():
            result["language"] = "Java"
            result["framework"] = "Maven"
            result["package_manager"] = "Maven"
            return result

        if (self.project_path / "build.gradle").exists():
            result["language"] = "Java"
            result["framework"] = "Gradle"
            result["package_manager"] = "Gradle"
            return result

        return result