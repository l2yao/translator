import google.generativeai as genai
import os

GOOGLE_API_KEY=os.environ['GOOGLE_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash-exp')

def generate_output(prompt):
    response = model.generate_content(
        prompt,
        request_options = {
            "timeout": 1000
        }
    )

    try:
        return response.text
    except Exception as ex:
        raise ex

def translations(text,
                 inputLanguage='Chinese',
                 targetLanguage='English'):

    translation_prompt = f"""
    As a professional book translator,
    translate the following book from {inputLanguage} into {targetLanguage}.

    Book to Translate:
    {text}

    """

    return translation_prompt