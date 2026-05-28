import gradio as gr
import re
import random
from datetime import datetime
from difflib import get_close_matches

# =========================================================
# MEMORY
# =========================================================

memory = {
    "user_name": None
}

# =========================================================
# INTENTS
# =========================================================

INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": [
            "Hello!",
            "Hi there!",
            "Hey! How can I help?"
        ]
    },

    "farewell": {
        "patterns": ["bye", "exit", "quit"],
        "responses": [
            "Goodbye!",
            "See you later!"
        ]
    },

    "time_query": {
        "patterns": ["time", "current time"],
        "responses": []
    },

    "help": {
        "patterns": ["help"],
        "responses": [
            "I can help with greetings, time, and remembering your name."
        ]
    },

    "name_introduction": {
        "patterns": ["my name is", "i am", "call me"],
        "responses": []
    }
}

# =========================================================
# PREPROCESSING
# =========================================================

def preprocess_text(text):

    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)

    return text

# =========================================================
# TYPO CORRECTION
# =========================================================

def correct_typo(user_input):

    all_patterns = []

    for intent in INTENTS.values():
        all_patterns.extend(intent["patterns"])

    corrected_words = []

    for word in user_input.split():

        match = get_close_matches(word, all_patterns, n=1, cutoff=0.8)

        corrected_words.append(match[0] if match else word)

    return " ".join(corrected_words)

# =========================================================
# ENTITY EXTRACTION
# =========================================================

def extract_name(user_input):

    patterns = [
        r"my name is (\w+)",
        r"i am (\w+)",
        r"call me (\w+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, user_input)

        if match:
            return match.group(1).capitalize()

    return None

# =========================================================
# INTENT DETECTION
# =========================================================

def detect_intent(user_input):

    for intent, data in INTENTS.items():

        for pattern in data["patterns"]:

            if pattern in user_input:
                return intent

    return "unknown"

# =========================================================
# CHATBOT RESPONSE
# =========================================================

def chatbot(user_input, history):

    processed_input = preprocess_text(user_input)

    corrected_input = correct_typo(processed_input)

    intent = detect_intent(corrected_input)

    # Greeting
    if intent == "greeting":

        if memory["user_name"]:
            response = f"Hello {memory['user_name']}!"

        else:
            response = random.choice(INTENTS[intent]["responses"])

    # Farewell
    elif intent == "farewell":

        response = random.choice(INTENTS[intent]["responses"])

    # Time
    elif intent == "time_query":

        current_time = datetime.now().strftime("%H:%M:%S")

        response = f"The current time is {current_time}"

    # Help
    elif intent == "help":

        response = random.choice(INTENTS[intent]["responses"])

    # Name Memory
    elif intent == "name_introduction":

        name = extract_name(corrected_input)

        if name:

            memory["user_name"] = name

            response = f"Nice to meet you, {name}!"

        else:
            response = "I didn't understand your name."

    # Unknown
    else:

        response = (
            "Sorry, I don't understand that yet.\n"
            "Try:\n"
            "- hello\n"
            "- what time is it\n"
            "- my name is Alex"
        )

    history.append((user_input, response))

    return history, history

# =========================================================
# GRADIO UI
# =========================================================

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 🤖 Advanced Rule-Based AI Chatbot
        
        ### Features
        - Intent Recognition
        - Typo Correction
        - Name Memory
        - Rule-Based AI
        - Continuous Conversation
        """
    )

    chatbot_ui = gr.Chatbot()

    msg = gr.Textbox(
        placeholder="Type your message here..."
    )

    clear = gr.Button("Clear Chat")

    state = gr.State([])

    msg.submit(
        chatbot,
        [msg, state],
        [chatbot_ui, state]
    )

    clear.click(
        lambda: ([], []),
        None,
        [chatbot_ui, state]
    )

# =========================================================
# LAUNCH APP
# =========================================================

demo.launch(debug=True)
