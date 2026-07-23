from django.db import transaction
from datetime import datetime
import logging  

logger = logging.getLogger(__name__)

from apps.candidate.models import (
    CandidateProfile,
    Education,
    Experience,
    Skill,
    Project,
    Certificate,
    Language,
    SocialLink,
)


class ResumeDataMapper:
    """
    Maps AI Resume JSON into Django Models.
    """

    def __init__(self, profile, parsed_data):

        self.profile = profile
        self.data = parsed_data

    @transaction.atomic
    def save_all(self):

        logger.info(
            "Starting AI Resume Mapping for Profile ID: %s",
            self.profile.id
        )

        self.save_profile()

        self.save_social_links()

        self.save_education()

        self.save_experience()

        self.save_skills()

        self.save_projects()

        self.save_certificates()

        self.save_languages()

        logger.info(
            "AI Resume Mapping Completed Successfully for Profile ID: %s",
            self.profile.id
        )

        return self.profile
    
    def save_profile(self):

        personal = self.data.get("personal_information", {})

        self.profile.current_job_title = (
            self.data.get("professional_summary", "")[:150]
            if not self.profile.current_job_title
            else self.profile.current_job_title
        )

        self.profile.about = self.data.get(
            "professional_summary",
            self.profile.about
        )

        address = personal.get("address", "")

        if address:

            parts = [p.strip() for p in address.split(",")]

            if len(parts) >= 1:
                self.profile.city = parts[-1]

            if len(parts) >= 2:
                self.profile.state = parts[-2]

            if len(parts) >= 3:
                self.profile.country = parts[-3]

        self.profile.save()

        logger.info(
            "Profile updated for profile ID %s",
            self.profile.id
        )


    def save_social_links(self):

        personal = self.data.get("personal_information", {})

        SocialLink.objects.update_or_create(

            profile=self.profile,

            defaults={

                "linkedin": self.normalize_url(
                    personal.get("linkedin")
                ),

                "github": self.normalize_url(
                    personal.get("github")
                ),

                "portfolio": self.normalize_url(
                    personal.get("portfolio")
                ),

            }

        )

        self.log_success(
            "Social Links",
            1
        )
        
        
    def save_education(self):

        Education.objects.filter(profile=self.profile).delete()

        education_list = self.data.get("education", [])

        imported = 0

        for education in education_list:

            start_date = self.parse_date(
                education.get("start_date")
            )

            if not start_date:

                self.log_skip(
                    "Education",
                    self.clean_text(
                        education.get("institution_name")
                    ),
                    "Missing or invalid start_date"
                )

                continue

            Education.objects.create(

                profile=self.profile,

                education_type=self.clean_text(
                    education.get("education_type")
                ),

                institution_name=self.clean_text(
                    education.get("institution_name")
                ),

                degree=self.clean_text(
                    education.get("degree")
                ),

                field_of_study=self.clean_text(
                    education.get("field_of_study")
                ),

                location=self.clean_text(
                    education.get("location")
                ),

                start_date=start_date,

                end_date=self.parse_date(
                    education.get("end_date")
                ),

                currently_studying=education.get(
                    "currently_studying",
                    False
                ),

                grade=self.clean_text(
                    education.get("grade")
                ),

                description=self.clean_text(
                    education.get("description")
                ),
            )

            imported += 1

        self.log_success(
            "Education",
            imported
        )

    def save_experience(self):

        Experience.objects.filter(profile=self.profile).delete()

        experience_list = self.data.get("experience", [])

        imported = 0

        for experience in experience_list:

            start_date = self.parse_date(
                experience.get("start_date")
            )

            if not start_date:

                self.log_skip(
                    "Experience",
                    self.clean_text(
                        experience.get("job_title")
                    ),
                    "Missing or invalid start_date"
                )

                continue

            Experience.objects.create(

                profile=self.profile,

                job_title=self.clean_text(
                    experience.get("job_title")
                ),

                company_name=self.clean_text(
                    experience.get("company_name")
                ),

                employment_type=self.normalize_employment_type(
                    experience.get("employment_type")
                ),

                location=self.clean_text(
                    experience.get("location")
                ),

                currently_working=experience.get(
                    "currently_working",
                    False
                ),

                start_date=start_date,

                end_date=self.parse_date(
                    experience.get("end_date")
                ),

                description=self.clean_text(
                    experience.get("description")
                ),
            )

            imported += 1

        self.log_success(
            "Experience",
            imported
        )

    def save_skills(self):

        Skill.objects.filter(profile=self.profile).delete()

        skills = self.data.get("skills", [])

        for skill in skills:

            if not skill:
                self.log_skip(
                    "Skills",
                    "Unknown Skill",
                    "Empty skill name"
                )
                continue

            Skill.objects.create(
                profile=self.profile,
                name=skill.strip(),
                proficiency="intermediate"
            )

        self.log_success(
            "Skills",
            len(skills)
        )

    def save_projects(self):

        Project.objects.filter(profile=self.profile).delete()

        project_list = self.data.get("projects", [])

        imported = 0

        for project in project_list:

            start_date = self.parse_date(
                project.get("start_date")
            )

            if not start_date:

                self.log_skip(
                    "Projects",
                    self.clean_text(
                        project.get("title")
                    ),
                    "Missing or invalid start_date"
                )

                continue

            Project.objects.create(

                profile=self.profile,

                title=self.clean_text(
                    project.get("title")
                ),

                short_description=self.clean_text(
                    project.get("short_description")
                ),

                description=self.clean_text(
                    project.get("description")
                ),

                technologies=self.join_technologies(
                    project.get("technologies")
                ),

                github_url=self.normalize_url(
                    project.get("github_url")
                ),

                live_url=self.normalize_url(
                    project.get("live_url")
                ),

                start_date=start_date,

                end_date=self.parse_date(
                    project.get("end_date")
                ),

                currently_working=project.get(
                    "currently_working",
                    False
                ),

                featured=project.get(
                    "featured",
                    False
                ),
            )

            imported += 1

        self.log_success(
            "Projects",
            imported
        )


    def save_certificates(self):

        Certificate.objects.filter(profile=self.profile).delete()

        certificate_list = self.data.get("certificates", [])

        imported = 0

        for certificate in certificate_list:

            issue_date = self.parse_date(
                certificate.get("issue_date")
            )

            if not issue_date:

                self.log_skip(
                    "Certificates",
                    self.clean_text(
                        certificate.get("certificate_name")
                    ),
                    "Missing or invalid issue_date"
                )

                continue

            Certificate.objects.create(

                profile=self.profile,

                certificate_name=self.clean_text(
                    certificate.get("certificate_name")
                ),

                issuing_organization=self.clean_text(
                    certificate.get("issuing_organization")
                ),

                issue_date=issue_date,

                expiry_date=self.parse_date(
                    certificate.get("expiry_date")
                ),

                credential_id=self.clean_text(
                    certificate.get("credential_id")
                ),

                credential_url=self.normalize_url(
                    certificate.get("credential_url")
                ),

                does_not_expire=certificate.get(
                    "does_not_expire",
                    False
                ),
            )

            imported += 1

        self.log_success(
            "Certificates",
            imported
        )


    def save_languages(self):

        Language.objects.filter(profile=self.profile).delete()

        language_list = self.data.get("languages", [])

        imported = 0

        allowed = {
            "native",
            "fluent",
            "professional",
            "intermediate",
            "basic",
        }

        for language in language_list:

            proficiency = self.clean_text(
                language.get("proficiency")
            ).lower()

            if proficiency not in allowed:
                proficiency = "intermediate"

            Language.objects.create(

                profile=self.profile,

                language=self.clean_text(
                    language.get("language")
                ),

                proficiency=proficiency,
            )

            imported += 1

        self.log_success(
            "Languages",
            imported
        )

    def parse_date(self, value):
        """
        Convert AI date string to Python date object.
        Supports:
        YYYY-MM-DD
        YYYY-MM
        YYYY
        """

        if not value:
            return None

        value = value.strip()

        formats = [
            "%Y-%m-%d",
            "%Y-%m",
            "%Y",
        ]

        for fmt in formats:
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue

        return None


    def clean_text(self, value):
        if value is None:
            return ""

        return str(value).strip()


    def join_technologies(self, technologies):

        if not technologies:
            return ""

        if isinstance(technologies, list):
            return ", ".join(technologies)

        return str(technologies)
    
    def normalize_employment_type(self, employment_type):

        employment_type = self.clean_text(employment_type).lower()

        allowed = {
            "full_time",
            "part_time",
            "internship",
            "freelance",
            "contract",
            "temporary",
            "volunteer",
        }

        if employment_type not in allowed:
            return "internship"

        return employment_type
    
    def normalize_url(self, url):

        url = self.clean_text(url)

        if not url:
            return ""

        if url.startswith(("http://", "https://")):
            return url

        return f"https://{url}"
    
    def log_success(self, section, count):

        logger.info(
            "[%s] Successfully imported %d record(s).",
            section,
            count,
        )


    def log_skip(self, section, record_name, reason):

        logger.warning(
            "[%s] Skipped '%s' - %s",
            section,
            record_name,
            reason,
        )


    def log_error(self, section, error):

        logger.error(
            "[%s] %s",
            section,
            str(error),
        )