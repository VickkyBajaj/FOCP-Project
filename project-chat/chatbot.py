import random
import json
import time

# Load configuration from a JSON file
with open("chat_config.json", "r") as config_file:
    config = json.load(config_file)

agent_names = config["agent_names"]
responses = config["responses"]
random_responses = config["random_responses"]

def get_random_agent_name():
    """Select a random agent name."""
    return random.choice(agent_names)

def detect_keywords(user_input):
    """Detect keywords in the user's input and provide an appropriate response."""
    for keyword, reply in responses.items():
        if keyword in user_input.lower():
            return reply
    return random.choice(random_responses)

def log_interaction(log_file, user_name, user_input, agent_name, response):
    """Log the interaction to a file."""
    with open(log_file, "a") as log:
        log.write(f"{user_name}: {user_input}\n{agent_name}: {response}\n")

def simulate_typing(response):
    """Simulate typing delay before showing the response."""
    typing_time = random.uniform(1, 3)  # Random delay between 1 and 3 seconds
    time.sleep(typing_time)
    print(response)

def emergency_contact_check(user_input, agent_name):
    """Check if the user input indicates an emergency and provide contact details."""
    emergency_keywords = ["help", "emergency", "urgent", "contact"]
    if any(keyword in user_input.lower() for keyword in emergency_keywords):
        emergency_response = "If this is an emergency, please contact the University Helpline at +1-800-555-1234."
        simulate_typing(f"{agent_name}: {emergency_response}")
        return True
    return False

def main_chat():
    """Main chat function."""
    # Greet the user and introduce the chat system
    user_name = input("Welcome! Please enter your name: ")
    print(f"Hello, {user_name}! Welcome to the University of Poppleton chat system.")

    # Introduce the virtual assistant
    agent_name = get_random_agent_name()
    print(f"My name is {agent_name}, and I'm here to assist you today.")

    log_file = "chat_log.txt"
    
    while True:
        # Randomly disconnect to mimic real chat systems
        if random.random() < 0.05:  # 5% chance to disconnect
            print(f"{agent_name}: Oops! It seems like I've been disconnected. Please try again later!")
            break

        user_input = input(f"{user_name}: ")
        
        if user_input.lower() in ["bye", "quit", "exit"]:
            simulate_typing(f"{agent_name}: Goodbye, {user_name}! Have a wonderful day!")
            break

        # Check for emergency contact
        if emergency_contact_check(user_input, agent_name):
            continue

        response = detect_keywords(user_input)
        simulate_typing(f"{agent_name}: {response}")

        # Log the interaction
        log_interaction(log_file, user_name, user_input, agent_name, response)

# Run the chat system if the script is executed
if __name__ == "__main__":
    main_chat()
