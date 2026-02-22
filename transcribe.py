from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_path = r"C:\Users\HP\Downloads\PythonProject\.venv\audio.mp3"

print(" Transcribing audio... please wait.")
with open(audio_path, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",  # or "whisper-1"
        file=audio_file
    )

text = transcription.text
print("\n🗣️ Transcribed text:\n")
print(text)

# Step 3️⃣ — Use the transcription as input for chat
print("\n Asking the model about the audio...\n")

response = client.chat.completions.create(
    model="gpt-4.1-mini",  # or "gpt-4o-mini"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Here is the transcribed audio:\n\n{text}\n\nSummarize this conversation in 3 sentences."}
    ]
)

summary = response.choices[0].message.content
print(" Summary of the audio:\n")
print(summary)
