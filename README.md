
# Arch AI Assistant

Work in progress project to build a AI Assistant that can interact with my computer, 

Arch AI Assistant (Artie) is a simple conversational assistant built using a two-layer AI structure. The assistant has a frontend that interacts with users and a backend that processes internal operations and function calls based on the conversation context. Artie can retrieve system information, execute commands, and provide customized responses based on user queries.

## Project Structure

```
project-root/
├── src/
│   ├── user_chat/
│   │   └── chat.py                # Frontend interaction handling (user chat loop)
│   ├── brain/
│   │   ├── brain.py               # Core backend processing logic
│   │   ├── api.py                 # Backend API request logic
│   │   └── utils.py               # Utility functions for parsing responses
│   ├── functions/
│   │   └── functions.py           # Functions the backend can call, e.g., system info, file operations
├── main.py                        # Entry point for running the assistant
└── README.md                      # Project documentation
```

## Requirements

Install the required packages by running:
```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/arch_ai_assistant.git
   cd arch_ai_assistant
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Assistant

Start the assistant by running the following command:
```bash
python main.py
```

This will start a chat loop where you can interact with Artie.

### Example Usage

```plaintext
Hi! I'm Artie, your AI Assistant! Type 'exit' to quit.
You: what system am i using?
Artie: You are using Linux.
You: exit
Artie: Goodbye!
```

## Project Components

### 1. `chat.py`
This file contains the `chat_loop` function, which initiates a conversation with the user and communicates with the backend AI through `process_message`.

### 2. `brain.py`
The core backend processing module. It maintains a `backend_conversation_history` and communicates with the AI backend via `get_response`. It interprets backend responses and initiates appropriate functions when needed, using a loop until a final response is available.

### 3. `functions.py`
Contains backend functions Artie can call, such as:
- `get_system_info`: Retrieves basic system details.
- `list_directory`: Lists directory contents (modify the path as needed).
- `read_file`: Reads file content.
- `execute_shell_command`: Executes a shell command and returns the result.

These functions can be easily expanded to add more utility for the assistant.

### 4. `utils.py`
Includes helper functions like `parse_response` to parse backend responses into usable data formats.

## Backend AI Response Format

The backend AI is instructed to use a strict JSON response format for compatibility and parsing. The required format includes:
```json
{
  "function_to_use": "function_name or 'none'",
  "state": "thinking or responding",
  "message_for_artie": "response message here"
}
```

### Example Responses
- **Function Call**:
  ```json
  {
    "function_to_use": "get_system_info",
    "state": "thinking",
    "message_for_artie": ""
  }
  ```
- **Direct Response**:
  ```json
  {
    "function_to_use": "none",
    "state": "responding",
    "message_for_artie": "Your system is running on Arch Linux."
  }
  ```


## Future Improvements

- Add more functions that Artie can call to expand its capabilities.
- Enhance error handling, especially for file access or command execution errors.
- Improve the user input validation for more robust interactions.
