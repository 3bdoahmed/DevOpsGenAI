
# thes class is responsible for building prompts for the AI model.
class PromptBuilder:
# thes constructor takes a dictionary argument project_info
    def build_docker_prompt(self, project_info: dict) -> str:
        prompt = f"""
You are a Senior DevOps Engineer.
Generate a production-ready Dockerfile.
Project Information:
Language: {project_info["language"]}
Framework: {project_info["framework"]}
Package Manager: {project_info["package_manager"]}

Requirements:
- Use multi-stage build when appropriate.
- Use a lightweight base image.
- Run the application as a non-root user.
- Optimize image size.
- Add comments explaining important steps.
- Expose the correct application port.
- Return ONLY the Dockerfile content.
"""
        return prompt.strip()