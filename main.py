import audio as atsc 
import srt_writer as swr 
from googletrans import Translator 
import subprocess
import moviepy.editor as mp
def getLanguage(argument):
    switcher = {
        1: "en-IN",
        2: "hi-IN",
        3: "kn-IN",
        4: "ta-IN",
        5: "te-IN",
        6: "mr-IN",
        7: "bn-IN",
        8: "gu-IN",
        9: "ml-IN",
        10: "pa-IN",
        11: "ur-IN",
        12: "as-IN",
        13: "or-IN",
        14: "ne-NP",
        15: "si-LK",
    }
    return switcher.get(argument, 0)
def getSelection():
    while True:
        try:
            userInput = int(input())
            if (userInput<1 or userInput>15):
                print("Not an integer! Try again.")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
def translate(text,dest):
    translator = Translator()
    try:
        detected_lang = translator.detect(text).lang
        translated = translator.translate(text, src=detected_lang, dest=dest)
        translated_with_spaces = ' '.join(translated.text)
        return translated_with_spaces
    except Exception as e:
        return str(e)
def AudioToSRT(audio_file_name,audio_language,file_name): 
    srt_content = atsc.get_large_audio_transcription(audio_file_name,audio_language) 
    swr.writeSRTFile(file_name,srt_content,True) 

if __name__ == "__main__":
    name=input("Enter the file name (excluding format): ")
    print('Please Select Language for Translate : ')
    print('1. English')
    print('2. Hindi')
    print('3. Kannada')
    print('4. Tamil')
    print('5. Telugu')
    print('6. Marathi')
    print('7. Bengali')
    print('8. Gujarati')
    print('9. Malayalam')
    print('10. Punjabi')
    print('11. Urdu')
    print('12. Assamese')
    print('13. Odia')
    print('14. Nepali')
    print('15. Sinhala')
    languageSelection = getLanguage(getSelection())
    audio_file_path = name  # Replace with the path to your audio file
    output_srt_file = name  # Replace with the desired SRT file path
    mp4=name+".mp4"
    wav=name+".wav"
    video = mp.VideoFileClip(mp4)
    audio_file = video.audio
    audio_file.write_audiofile(wav)
    srt=name+".srt"
    AudioToSRT(audio_file_path,languageSelection,output_srt_file)
    subprocess.call(["ffmpeg", "-i", mp4 , "-vf", f"subtitles={srt}", "-y", "output_video.mp4"])