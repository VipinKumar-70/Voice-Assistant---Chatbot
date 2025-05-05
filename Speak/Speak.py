import os
import io
import pygame
from google.cloud import texttospeech
from Config import GOOGLE_SERVICE_CREDENTIALS

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_SERVICE_CREDENTIALS

# Initialize Google TTS Client
client = texttospeech.TextToSpeechClient()

# Voice configuration
voice = texttospeech.VoiceSelectionParams(
    language_code="en-IN",
    name="en-IN-Chirp-HD-D",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Audio configuration
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Initialize pygame mixer
pygame.mixer.init()

def speak(text: str):
    """Synthesizes speech from text and plays it using pygame."""
    try:
        # Synthesize speech
        synthesis_input = texttospeech.SynthesisInput(text=text)
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Load audio directly from memory
        audio_stream = io.BytesIO(response.audio_content)

        # Ensure pygame mixer is initialized
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Play audio
        sound = pygame.mixer.Sound(audio_stream)
        sound.play()

        # Wait until playback is finished
        while pygame.mixer.get_busy():
            pygame.time.wait(100)

    except Exception as e:
        print(f"Error during speech synthesis: {e}")

    finally:
        pygame.mixer.quit()