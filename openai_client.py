import openai
from config import OPENAI_API_KEY

# Initialize OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_openai_response(prompt: str) -> str:
    """Send a query to OpenAI's ChatCompletion endpoint and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if enabled for your account
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100,
        )
        # Extract the content of the AI response
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
