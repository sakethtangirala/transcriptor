import whisper
from pydub import AudioSegment
import sys
import os

def convert_mp3_to_wav(mp3_file, wav_file):
    AudioSegment.from_mp3(mp3_file).export(wav_file, format="wav")

def transcribe_audio(file):
    model = whisper.load_model("base")  
    result = model.transcribe(file)
    return result["text"]

def save_transcription(text, output_file):
    with open(output_file, "w") as f:
        f.write(text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input.mp3>")
        sys.exit(1)
    
    mp3_file = sys.argv[1]
    
    if not os.path.exists('../wavs'):
        os.makedirs('../wavs')
    if not os.path.exists('../outputs'):
        os.makedirs('../outputs')
    
    wav_file = os.path.join("../wavs", "converted.wav")
    output_text_file = os.path.join("../outputs", "transcription.txt")
    
    print("Converting MP3 to WAV...")
    convert_mp3_to_wav(mp3_file, wav_file)
    
    print("Transcribing audio...")
    transcription = transcribe_audio(wav_file)
    
    print("Saving transcription...")
    save_transcription(transcription, output_text_file)
    
    print(f"Transcription saved to {output_text_file}")

if __name__ == "__main__":
    main()
