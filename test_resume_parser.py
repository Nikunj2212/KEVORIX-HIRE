from pprint import pprint

from apps.candidate.ai.services.resume_parser import ResumeParserService

result = ResumeParserService.parse_resume(
    "media/candidate/resumes/Panchal_Nikunj_resume_4.pdf"
)

pprint(result)