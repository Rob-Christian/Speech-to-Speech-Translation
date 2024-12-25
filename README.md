# Speech-to-Speech Translation with OpenAI Models
This is a Streamlit web application that utilizes OpenAI's models for automatic speech recognition (ASR), text translation, and text-to-speech (TTS) generation. The app allows users to upload an audio file, convert it to text, translate the text into a different language, and generate speech from the translated text. The models used in this application include:
1. Whisper-1: (for speech to text conversion)
2. GPT-4o-mini: (for text translation)
3. TTS-1: (for text-to-speech conversion)
# How to setup?
1. Clone the repository:
    git clone https://github.com/yourusername/speech-to-speech-translation.git
    cd speech-to-speech-translation
2. Create a .env file in the root directory of the project folder. Then add your openai key
    key=your-openai-api-key
3. Run the app:
    streamlit run app.py
