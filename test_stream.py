from google import genai
from dotenv import load_dotenv
import os
import sys
import time

# Load environment variables from the local .env file
load_dotenv()

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
        print("Please check your .env file in this directory.", file=sys.stderr)
        sys.exit(1)

    print("Initializing client...")
    client = genai.Client(api_key=api_key)

    prompt = "Tell me a short, 3-sentence sci-fi story."
    print(f"\nPrompt: {prompt}")
    print("Gemini response (streaming char-by-char): ", end="", flush=True)

    try:
        # Request stream from Gemini
        response = client.models.generate_content_stream(
            model='gemini-2.5-flash',
            contents=prompt,
        )

        # Print character by character with a small delay for a smooth typing effect
        for chunk in response:
            for char in chunk.text:
                print(char, end="", flush=True)
                time.sleep(0.015)  # 15ms delay per character
        print("\n")
    except Exception as e:
        print(f"\nAn error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
