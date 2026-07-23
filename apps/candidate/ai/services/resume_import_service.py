import logging

from .resume_parser import ResumeParserService
from .data_mapper import ResumeDataMapper

logger = logging.getLogger(__name__)


class ResumeImportService:
    """
    Complete AI Resume Import Service

    Flow:
    Resume PDF
        ↓
    ResumeParserService
        ↓
    Gemini AI
        ↓
    Parsed JSON
        ↓
    ResumeDataMapper
        ↓
    Database
    """

    def __init__(self, profile):

        self.profile = profile

        self.parser = ResumeParserService()

    def import_resume(self, resume_file):

        try:

            logger.info(
                "Starting AI Resume Import for Profile ID: %s",
                self.profile.id
            )

            parsed_data = self.parser.parse(resume_file)

            mapper = ResumeDataMapper(
                self.profile,
                parsed_data
            )

            mapper.save_all()

            logger.info(
                "AI Resume Import Completed Successfully for Profile ID: %s",
                self.profile.id
            )

            return {
                "success": True,
                "message": "Resume imported successfully.",
                "data": parsed_data,
            }

        except Exception as e:

            logger.exception(
                "AI Resume Import Failed for Profile ID: %s",
                self.profile.id
            )

            return {
                "success": False,
                "message": str(e),
                "data": None,
            }