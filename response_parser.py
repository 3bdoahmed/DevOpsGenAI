import re

class ResponseParser:

    @staticmethod
    def clean(text: str) -> str:
        """
        Remove markdown code fences from AI response.
        """

        # Remove ```dockerfile
        text = re.sub(r"^```[a-zA-Z0-9]*\n", "", text)

        # Remove ending ```
        text = re.sub(r"\n```$", "", text)

        return text.strip()