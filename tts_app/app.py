import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from tts_module import EdgeTTS
import soundfile as sf

app = Flask(__name__)
tts = EdgeTTS()

# Ensure output directory exists
os.makedirs('outputs', exist_ok=True)

@app.route('/')
def index():
    # Get list of supported voices
    voices = tts.SUPPORTED_VOICE
    
    # Filter Indonesian voices
    id_voices = [voice for voice in voices if voice.startswith('id-ID')]
    
    # If no Indonesian voices found, add default ones
    if not id_voices:
        id_voices = ['id-ID-GadisNeural', 'id-ID-ArdiNeural']
    
    # Get all voices for complete selection
    return render_template('index.html', id_voices=id_voices, all_voices=voices)

@app.route('/generate', methods=['POST'])
def generate_audio():
    text = request.form.get('text', '')
    voice = request.form.get('voice', 'id-ID-GadisNeural')
    rate = int(request.form.get('rate', 0))
    volume = int(request.form.get('volume', 100))
    pitch = int(request.form.get('pitch', 0))
    
    # Generate unique filename
    import uuid
    filename = f"tts_{uuid.uuid4().hex[:8]}"
    output_file = os.path.join('outputs', f"{filename}.wav")
    output_subs = os.path.join('outputs', f"{filename}.vtt")
    
    # Generate audio
    audio_file, sub_file = tts.predict(text, voice, rate, volume, pitch, output_file, output_subs)
    
    # Get audio duration
    audio_info = sf.info(audio_file)
    duration = audio_info.duration
    
    return jsonify({
        'success': True,
        'audio_url': f'/outputs/{os.path.basename(audio_file)}',
        'subtitle_url': f'/outputs/{os.path.basename(sub_file)}',
        'duration': duration
    })

@app.route('/outputs/<filename>')
def serve_file(filename):
    return send_from_directory('outputs', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
