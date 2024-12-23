from openai import OpenAI
from dotenv import load_dotenv
import os
from fastapi import HTTPException
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# load .env
load_dotenv()

# OpenAI client init
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # load api key from .env
)

def text_to_ipa(text: str) -> str:
    """
    use openai api to convert text to ipa
    """
    try:
        # language auto detect and convert to ipa
        prompt = (
            f'Convert the following text to IPA symbols with strict phonetic rules and syllable boundaries. Return IPA transcription only, without explanations. Text: "{text}" '
        )

        # gpt 4o mini model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0,
        )


        ipa_result = response.choices[0].message.content.strip()
        return ipa_result

    except Exception as e:
        # 오류 로그 기록
        logger.error("OpenAI API Error occurred")
        raise HTTPException(status_code=500, detail="OpenAI API Error occurred")
