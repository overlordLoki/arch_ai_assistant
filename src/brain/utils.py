# src/brain/utils.py
import json

def parse_response(response: str):
    """Parse the response from the backend AI and extract key components."""
    is_thinking = False
    function_to_use = None
    message_for_artie = None

    try:
        # Convert the string response to a dictionary
        response_data = json.loads(response)
        
        # Extract each component with default fallbacks
        function_to_use = response_data.get("function_to_use", "none")
        state = response_data.get("state", "responding")
        message_for_artie = response_data.get("message_for_artie", "")

        # Determine if the backend AI is in the "thinking" state
        is_thinking = (state == "thinking")
        
        # Set function_to_use to None if the response specifies "none"
        if function_to_use == "none":
            function_to_use = None

    except json.JSONDecodeError as e:
        # Handle cases where the response isn't valid JSON
        print(f"Error: Unable to parse backend AI response. Invalid format. Details: {e}")
        print(f"Raw response that caused error: {response}")
    
    return is_thinking, function_to_use, message_for_artie
