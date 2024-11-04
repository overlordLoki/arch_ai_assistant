# src/brain/brain.py

from src.brain.api import get_response
from src.brain.utils import parse_response
from src.functions.functions import get_system_info, list_directory, read_file, execute_shell_command , list_fuction_names

# Backend AI internal conversation history
backend_conversation_history = [
    {
        "role": "system",
        "content": (
            "You are the backend AI for Artie, an AI assistant. All responses must strictly follow the JSON format below, "
            "with double quotes around both property names and string values. Always return a single JSON object with these properties:\n\n"
            '{\n'
            '  "function_to_use": [function_name as a string, or "none"],\n'
            '  "state": "thinking" or "responding",\n'
            '  "message_for_artie": "<message text as a string>"\n'
            '}\n\n'
            "Examples:\n\n"
            'Example 1 (requires a function call):\n'
            '{\n'
            '  "function_to_use": "get_system_info",\n'
            '  "state": "thinking",\n'
            '  "message_for_artie": ""\n'
            '}\n\n'
            "Example 2 (no function call needed, direct response):\n"
            '{\n'
            '  "function_to_use": "none",\n'
            '  "state": "responding",\n'
            '  "message_for_artie": "Your system is running on Arch Linux."\n'
            '}\n\n'
            "Always follow this format exactly, even if no function is needed.\n"
            "Here are the available functions:\n"
            f"{list_fuction_names()}"
        )
    }
]
def process_message(message: str) -> str:
    """Process the user message, interact with backend AI if needed, and return the response."""
    backend_conversation_history.append({"role": "user", "content": message})

    while True:
        # Send the current conversation history to the backend AI
        backend_response = get_response(backend_conversation_history)

        # Parse the response to determine the AI's state and instructions
        is_thinking, function_to_use, message_for_artie = parse_response(backend_response)

        if is_thinking and function_to_use:
            # The AI is "thinking" and requires a function to be executed
            function_result = None
            
            # Call the specified function based on `function_to_use`
            if function_to_use == "get_system_info":
                function_result = get_system_info()
            elif function_to_use == "list_directory":
                function_result = list_directory("/path/to/directory")  # Adjust the path as needed
            elif function_to_use == "read_file":
                function_result = read_file("/path/to/file")  # Adjust the path as needed
            elif function_to_use == "execute_shell_command":
                function_result = execute_shell_command("ls")  # Replace with desired command
            
            content = f"function_result {function_result}"
            # Append the result to the backend history and continue the loop
            backend_conversation_history.append({"role": "user", "content": content})

        else:
            # The AI is "responding" with a message, end the loop and return the message
            backend_conversation_history.append({"role": "assistant", "content": message_for_artie})
            return message_for_artie
