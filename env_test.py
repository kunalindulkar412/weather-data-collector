import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("DEMO_API_KEY")

print(f"API Key: {api_key}")