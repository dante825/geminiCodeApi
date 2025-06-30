import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./gemini-cli/gemini.env')
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

for m in genai.list_models():
    print(m.name)
