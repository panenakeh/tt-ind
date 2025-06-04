import asyncio
import os
from io import TextIOWrapper
from typing import Union, TextIO
from edge_tts import Communicate, SubMaker

class EdgeTTS:
    def __init__(self, list_voices_flag=False, proxy=None) -> None:
        # Fallback list of voices for Indonesian and English
        self.SUPPORTED_VOICE = [
            'id-ID-GadisNeural', 
            'id-ID-ArdiNeural', 
            'en-US-EmmaNeural', 
            'en-US-RogerNeural',
            'en-US-ChristopherNeural',
            'en-US-AriaNeural',
            'zh-CN-XiaoxiaoNeural'
        ]
        self.network = True

    def preprocess(self, rate, volume, pitch):
        if rate >= 0:
            rate = f'+{rate}%'
        else:
            rate = f'{rate}%'
        if pitch >= 0:
            pitch = f'+{pitch}Hz'
        else:
            pitch = f'{pitch}Hz'
        volume = 100 - volume
        volume = f'-{volume}%'
        return rate, volume, pitch

    def predict(self, TEXT, VOICE, RATE, VOLUME, PITCH, OUTPUT_FILE='result.wav', OUTPUT_SUBS='result.vtt', words_in_cue=8):
        async def amain() -> None:
            """Main function"""
            rate, volume, pitch = self.preprocess(rate=RATE, volume=VOLUME, pitch=PITCH)
            communicate = Communicate(TEXT, VOICE, rate=rate, volume=volume, pitch=pitch)
            subs: SubMaker = SubMaker()
            sub_file: Union[TextIOWrapper, TextIO] = (
                open(OUTPUT_SUBS, "w", encoding="utf-8")
            )
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    # audio_file.write(chunk["data"])
                    pass
                elif chunk["type"] == "WordBoundary":
                    # print((chunk["offset"], chunk["duration"]), chunk["text"])
                    subs.create_sub((chunk["offset"], chunk["duration"]), chunk["text"])
            sub_file.write(subs.generate_subs(words_in_cue))
            await communicate.save(OUTPUT_FILE)
            
        asyncio.run(amain())
        
        # Process subtitles to remove spaces (optional for Indonesian)
        with open(OUTPUT_SUBS, 'r', encoding='utf-8') as file:
            vtt_lines = file.readlines()

        # Remove spaces in each line of text (except for lines with timestamps)
        vtt_lines_without_spaces = [line.replace(" ", "") if "-->" not in line else line for line in vtt_lines]
        
        with open(OUTPUT_SUBS, 'w', encoding='utf-8') as output_file:
            output_file.writelines(vtt_lines_without_spaces)
            
        return OUTPUT_FILE, OUTPUT_SUBS
