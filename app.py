import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from io import BytesIO

# Load the OpenAI API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key = OPENAI_API_KEY)

# Function to convert speech to text
def speech_to_text(audio):
    transcription = client.audio.transcriptions.create(
        model = "whisper-1",
        file = audio
    )
    return transcription.text

# Function to translate text to other language
def translate_text(text, language):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {'role': 'system', 'content': f'Convert the given text into its corresponding {language}'},
            {'role': 'user', 'content': text}
        ],
        temperature = 0,
        max_tokens = 128
    )
    return response.choices[0].message.content

# Function to generate speech from text using a TTS model
def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input = text
    )
    audio_stream = BytesIO(response.content)
    return audio_stream

# Streamlit app interface
def main():
    st.title("Speech to Speech Translation")
    
    uploaded_audio = st.file_uploader("Upload an Audio File (only mp3)", type=["mp3"])

    # User input for desired output language
    language = st.text_input("Enter the desired language for the output text (e.g., Spanish, French, etc.)")
    
    if uploaded_audio is not None and language:
        # Step 1: Convert speech to text
        st.subheader("Original Transcription")
        original_text = speech_to_text(uploaded_audio)
        st.write(original_text)

        # Step 2: Modify or Translate text based on user input language
        st.subheader(f"Modified Text in {language}")
        modified_text = translate_text(original_text, language=language) 
        st.write(modified_text)
        
        # Step 3: Convert modified text to speech
        st.subheader("Generated Speech")
        audio_stream = text_to_speech(modified_text)
        
        # Play the generated speech
        st.audio(audio_stream, format="audio/mp3")

if __name__ == "__main__":
    main()
