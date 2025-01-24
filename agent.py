from models import UserQuery, AIResponse
from openai_client import get_openai_response

def run_agent(user_input: str) -> str:
    """Process user input and return an AI response."""
    try:
        # Validate user input
        user_query = UserQuery(query=user_input)

        # Fetch response from OpenAI
        ai_output = get_openai_response(user_query.query)

        # Validate AI output
        validated_response = AIResponse(response=ai_output)
        return validated_response.response
    except Exception as e:
        return f"Error processing request: {str(e)}"
