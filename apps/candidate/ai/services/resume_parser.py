import json

from apps.candidate.ai.providers.gemini import generate_response
from apps.candidate.ai.prompts.resume_prompt import RESUME_PARSER_PROMPT
from apps.candidate.ai.utils.pdf_reader import extract_text_from_pdf


class ResumeParserService:
    """
    AI Resume Parser Service
    """

    @staticmethod
    def parse_resume(pdf_path: str) -> dict:
        """
        Parse resume PDF using Gemini AI.
        """

        # Step 1: Extract text
        resume_text = extract_text_from_pdf(pdf_path)

        if not resume_text:
            raise ValueError("Unable to extract text from resume.")

        # Step 2: Build prompt
        prompt = RESUME_PARSER_PROMPT.format(
            resume_text=resume_text
        )

        # Step 3: Gemini Response
        response = generate_response(prompt)

        # Step 4: Convert JSON string → Python Dictionary
        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            raise ValueError(
                "Gemini returned invalid JSON.\n\n"
                f"Response:\n{response}"
            )

        return data