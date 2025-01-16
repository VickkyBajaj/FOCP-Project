# Chat System README

## Overview
This Python script is a simple chat system designed to provide a conversational interface for users. The system uses a configuration file to define agent names, predefined responses, and random fallback responses. It can also detect emergency situations and provide relevant contact details.

## Features
- **Dynamic Agent Names**: The system selects a random agent name from a predefined list.
- **Keyword Detection**: It detects specific keywords in user input to provide relevant responses.
- **Random Responses**: If no keyword is detected, the system provides a random fallback response.
- **Emergency Check**: The chat can identify emergency-related keywords and suggest contacting a helpline.
- **Typing Simulation**: Delays are added to simulate real-time typing.
- **Interaction Logging**: All user-agent interactions are logged to a file.
- **Random Disconnection**: A 5% chance to mimic real-world chat system disconnections.

## Files
- **`chat_config.json`**: Configuration file containing agent names, predefined responses, and random responses.
- **`chat_log.txt`**: Log file to record all interactions.
- **`chat_system.py`**: The main script containing the chat logic.

## Configuration
The script relies on a `chat_config.json` file with the following structure:

```json
{
  "agent_names": ["Alice", "Bob", "Charlie"],
  "responses": {
    "hello": "Hi there! How can I help you today?",
    "course": "Sure, I can help you with course details.",
    "fee": "The fee structure varies by program. Can you specify which one?"
  },
  "random_responses": [
    "Can you please clarify?",
    "I'm here to help, but I need more details.",
    "Could you rephrase that?"
  ]
}
```

## Functions
### 1. `get_random_agent_name()`
Selects a random name from the `agent_names` list in the configuration file.

### 2. `detect_keywords(user_input)`
Detects keywords in user input and returns the appropriate response. If no keywords match, a random fallback response is returned.

### 3. `log_interaction(log_file, user_name, user_input, agent_name, response)`
Logs user and agent interactions into the specified log file.

### 4. `simulate_typing(response)`
Simulates typing by adding a random delay (1 to 3 seconds) before displaying the agent’s response.

### 5. `emergency_contact_check(user_input, agent_name)`
Checks if the user input contains emergency-related keywords and provides a helpline contact if necessary.

### 6. `main_chat()`
The main function that handles user interaction and orchestrates the chat system.

## Usage
1. Place the script (`chat_system.py`) and the configuration file (`chat_config.json`) in the same directory.
2. Run the script using Python:
   ```bash
   python chat_system.py
   ```
3. Follow the prompts in the terminal to interact with the chat system.

## Example Interaction
```plaintext
Welcome! Please enter your name: John
Hello, John! Welcome to the University of Poppleton chat system.
My name is Alice, and I'm here to assist you today.

John: Hello
Alice: Hi there! How can I help you today?

John: Can you tell me about the course fees?
Alice: The fee structure varies by program. Can you specify which one?

John: Emergency!
Alice: If this is an emergency, please contact the University Helpline at +1-800-555-1234.

John: Bye
Alice: Goodbye, John! Have a wonderful day!
```

## Notes
- Ensure the `chat_config.json` file is correctly formatted and placed in the same directory as the script.
- The log file (`chat_log.txt`) will be created or appended to in the script’s directory.

## Future Enhancements
- Add support for natural language processing (NLP) for more sophisticated responses.
- Integrate with a database for dynamic response updates.
- Develop a GUI for an enhanced user experience.
