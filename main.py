# import the ProjectScanner class from the scanner module
from scanner import ProjectScanner
from detector import ProjectDetector
from prompt_builder import PromptBuilder
from gemini_client import GeminiClient
from writer import Writer
from config import GEMINI_API_KEY
from response_parser import ResponseParser

# this is the main entry point of the program
project_path = input("Enter project path: ")

# create an instance of ProjectScanner
scanner = ProjectScanner(project_path)
# scan the project and get information
info = scanner.scan()

detector = ProjectDetector(project_path)
project_info = detector.detect()
builder = PromptBuilder()
prompt = builder.build_docker_prompt(project_info)
print(prompt)

client = GeminiClient(GEMINI_API_KEY)

dockerfile = client.generate(prompt)

writer = Writer(project_path)
dockerfile = ResponseParser.clean(dockerfile)
writer.write("Dockerfile", dockerfile)

print("Done.")