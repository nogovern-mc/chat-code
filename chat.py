import time
from openai import OpenAI

# ----------------------------
# 🔑 1. Configure your Gemini API settings
# ----------------------------
GEMINI_API_KEY = "AIzaSyBaIKGVWHoNyrd9-NnR8lKFIAvDHw-9_p8"  # ← Replace with your real key
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # OpenAI-compat endpoint for Gemini
GEMINI_MODEL = "gemini-2.5-flash"  # Or another gemini model you have access to

# Initialize the OpenAI client, but pointed to Gemini
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url=GEMINI_BASE_URL
)


def claude_style_response(messages):
    """
    Sends the chat history (messages) and returns a Claude-like reply via Gemini.
    """
    resp = client.chat.completions.create(
        model=GEMINI_MODEL,
        messages=messages,
        temperature=0.75,
        max_tokens=600,
    )
    # The response format is the same: .choices[0].message.content
    return resp.choices[0].message.content


def run_chat():
    print("======================================")
    print(" 🧠 Claude-style Chatbot (via Gemini)")
    print(" Type 'exit' or 'quit' to stop.")
    print("======================================\n")

    # System prompt to steer style / tone
    messages = [
        {
            "role": "system",
            "content": (
                "You are Claude, an insightful, articulate, and empathetic AI coding assistant. "
                "You think before you speak, give clear explanations with examples or analogies, "
                "and maintain a warm, professional style."
            )
        }
    ]

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("Claude: Goodbye! 👋")
            break

        # Add user message
        messages.append({"role": "user", "content": user_input})

        try:
            reply = claude_style_response(messages)
            print(f"\nClaude: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("⚠️ Error from API:", e)
            # Optionally, retry after a pause
            time.sleep(1)


if __name__ == "__main__":
    run_chat()
