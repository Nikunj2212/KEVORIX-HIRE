import os
import uuid

from django.conf import settings
from django.core.files import File

from apps.candidate.ai.image_generator import generate_cover_image
from apps.candidate.ai.prompt_builder import build_cover_prompt


def generate_ai_cover(profile):

    skills = list(
        profile.skills.values_list("name", flat=True)
    )

    prompt = build_cover_prompt(
        profile.current_job_title,
        skills
    )

    image = generate_cover_image(prompt)

    filename = f"{uuid.uuid4().hex}.png"

    folder = os.path.join(
        settings.MEDIA_ROOT,
        "candidate",
        "cover"
    )

    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, filename)

    image.save(filepath)

    if profile.cover_photo:
        profile.cover_photo.delete(save=False)

    with open(filepath, "rb") as f:

        profile.cover_photo.save(
            filename,
            File(f),
            save=True
        )

    return profile.cover_photo.url