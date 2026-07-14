# DevOpsGenAI

DevOpsGenAI is a small Python CLI tool that scans a local project, detects its language, framework, and package manager, and then uses Google's Gemini API to automatically generate a production-ready `Dockerfile` for that project.

## How It Works

1. **Scan** – `ProjectScanner` reads the top-level files in your project directory.
2. **Detect** – `ProjectDetector` inspects key files (`package.json`, `requirements.txt`, `pyproject.toml`, `pom.xml`, `build.gradle`) to figure out the language, framework, and package manager.
3. **Prompt** – `PromptBuilder` builds a detailed prompt describing the project and asking for a production-ready Dockerfile.
4. **Generate** – `GeminiClient` sends the prompt to the Gemini API and receives the generated Dockerfile content.
5. **Clean** – `ResponseParser` strips any markdown code fences from the AI response.
6. **Write** – `Writer` saves the result as a `Dockerfile` inside the project directory.

### Currently Detected Stacks

| Language | Detection File(s)                          | Frameworks Recognized                              |
|----------|---------------------------------------------|-----------------------------------------------------|
| Node.js  | `package.json`                              | Next.js, React, Express, NestJS, Vite (else generic Node.js) |
| Python   | `requirements.txt` or `pyproject.toml`      | Generic Python (pip or poetry)                      |
| Java     | `pom.xml` or `build.gradle`                 | Maven or Gradle                                     |

## Requirements

- Python 3.9+
- A [Gemini API key](https://ai.google.dev/)

## Installation

```bash
git clone https://github.com/3bdoahmed/DevOpsGenAI.git
cd DevOpsGenAI
pip install google-genai python-dotenv
```

## Configuration

Create a `.env` file in the project root with your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the tool from the project directory:

```bash
python main.py
```

You'll be prompted to enter the path to the project you want to containerize:

```
Enter project path: /path/to/your/project
```

DevOpsGenAI will scan the project, detect its stack, generate a Dockerfile via Gemini, and write it to `Dockerfile` inside that project's directory.

## Project Structure

```
DevOpsGenAI/
├── main.py             # Entry point / orchestrates the workflow
├── scanner.py          # Scans the project directory for files
├── detector.py         # Detects language, framework, package manager
├── prompt_builder.py    # Builds the AI prompt
├── gemini_client.py     # Wraps calls to the Gemini API
├── response_parser.py   # Cleans markdown fences from AI output
├── writer.py            # Writes the generated Dockerfile to disk
└── config.py            # Loads environment variables (.env)
```

## Notes / Known Limitations

- The API key is read from the `GEMINI_API_KEY` environment variable via `.env` — make sure not to commit this file (it's already listed in `.gitignore`).
- Detection currently only looks at files in the project's root directory, not subdirectories.
- The Gemini model used is hardcoded in `gemini_client.py` — update it there if you need a different model version.

## 📌 Author
AbdelRahman Ahmed