from apps.candidate.ai.providers.gemini import generate_response

response = generate_response(
    "Reply with only one sentence: KEVORIX AI is connected successfully."
)

print(response)