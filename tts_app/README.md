# Dokumentasi Aplikasi Text-to-Speech Bahasa Indonesia

## Deskripsi
Aplikasi Text-to-Speech (TTS) Bahasa Indonesia adalah aplikasi web yang memungkinkan pengguna untuk mengubah teks menjadi suara dengan dukungan bahasa Indonesia. Aplikasi ini menggunakan teknologi EdgeTTS dari Microsoft untuk menghasilkan suara berkualitas tinggi.

## Fitur Utama
- Konversi teks ke suara dengan dukungan bahasa Indonesia
- Pilihan suara (id-ID-GadisNeural, id-ID-ArdiNeural, dan lainnya)
- Pengaturan lanjutan untuk kecepatan, volume, dan nada suara
- Pemutaran audio langsung di browser
- Unduh file audio hasil konversi
- Contoh teks untuk demonstrasi cepat

## Cara Penggunaan
1. Buka aplikasi melalui URL yang disediakan
2. Masukkan teks yang ingin diubah menjadi suara pada kotak teks
3. Pilih suara yang diinginkan (disarankan id-ID-GadisNeural atau id-ID-ArdiNeural untuk bahasa Indonesia)
4. Opsional: Sesuaikan pengaturan lanjutan (kecepatan, volume, nada)
5. Klik tombol "Buat Suara" untuk memproses
6. Tunggu hingga proses selesai, audio akan otomatis diputar
7. Klik "Unduh Audio" jika ingin menyimpan file audio

## Teknologi yang Digunakan
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **TTS Engine**: EdgeTTS (Microsoft)
- **Audio Processing**: Librosa, SoundFile

## Struktur Aplikasi
```
tts_app/
├── venv/                  # Virtual environment
├── app.py                 # Aplikasi Flask utama
├── tts_module.py          # Modul TTS untuk EdgeTTS
├── requirements.txt       # Dependensi Python
├── templates/
│   └── index.html         # Halaman web utama
├── static/                # Aset statis (jika ada)
└── outputs/               # Direktori untuk file audio output
```

## Instalasi Lokal
1. Pastikan Python 3.8+ terinstal
2. Clone repositori atau ekstrak file aplikasi
3. Buat virtual environment: `python -m venv venv`
4. Aktifkan virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
5. Instal dependensi: `pip install -r requirements.txt`
6. Jalankan aplikasi: `python app.py`
7. Buka browser dan akses `http://localhost:5000`

## Catatan Penting
- Aplikasi membutuhkan koneksi internet untuk mengakses layanan EdgeTTS
- Suara bahasa Indonesia yang tersedia: id-ID-GadisNeural (wanita) dan id-ID-ArdiNeural (pria)
- Untuk penggunaan produksi, disarankan untuk menggunakan server WSGI seperti Gunicorn

## Sumber dan Referensi
- Repositori Linly-Talker: https://github.com/Kedreamix/Linly-Talker/tree/main/TTS
- Dokumentasi EdgeTTS: https://github.com/rany2/edge-tts
