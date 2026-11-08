import os
from dotenv import load_dotenv

load_dotenv()

for name in ["GEMINI_API_KEY", "GITHUB_TOKEN"]:
    value = os.getenv(name)
    if value:
        print(f"{name}: loaded (starts with {value[:4]}..., length {len(value)})")
    else:
        print(f"{name}: MISSING, check your .env file")