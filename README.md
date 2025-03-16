```markdown
# FuzzyMatchChatbot

Proyek ini adalah chatbot Python yang menggunakan pencocokan fleksibel (*fuzzy matching*) untuk memberikan respons yang lebih relevan terhadap pertanyaan pengguna. Data disimpan dalam format H5 untuk efisiensi, dan proyek ini dibangun sebagai mikroservice menggunakan Flask.

## Fitur Utama

- **Pencocokan Fleksibel (Fuzzy Matching):** Menggunakan algoritma `difflib.get_close_matches` untuk mengenali dan merespons pertanyaan yang mirip, bahkan jika tidak persis sama dengan data yang tersimpan.
- **Penyimpanan Data H5:** Menyimpan dataset dalam format H5 untuk efisiensi dan kecepatan akses.
- **Mikroservice Flask:** Dibangun sebagai mikroservice menggunakan Flask, memungkinkan integrasi yang mudah dengan aplikasi lain.
- **Respons yang Relevan:** Meningkatkan interaktivitas dan kemampuan chatbot dalam memahami variasi bahasa alami.

## Cara Penggunaan

1. **Clone repositori:**
    ```bash
    git clone https://github.com/AldevaRizky/FuzzyMatchChatbot.git
    cd FuzzyMatchChatbot
    ```

2. **Instal dependensi:**
    ```bash
    pip install Flask h5py
    ```

3. **Jalankan aplikasi:**
    ```bash
    python app.py
    ```

    Aplikasi akan berjalan di `http://127.0.0.1:5000/api/chatbot`.

4. **Gunakan Postman atau alat serupa untuk mengirim permintaan POST ke endpoint `/api/chatbot` dengan format JSON:**
    ```json
    {
      "question": "Apa kamu tahu Laravel?"
    }
    ```

    Respons yang diharapkan:
    ```json
    {
      "question": "Apa kamu tahu Laravel?",
      "answer": "Laravel adalah framework PHP untuk pengembangan aplikasi web."
    }
    ```

## Struktur Proyek

```
FuzzyMatchChatbot/
├── app.py        # Kode utama aplikasi Flask
├── create_h5.py  # Skrip untuk membuat dataset H5
├── data.h5       # Dataset chatbot dalam format H5
└── README.md     # File dokumentasi proyek
```

## Cara Kerja

1. Dataset pertanyaan dan jawaban disimpan dalam file `data.h5`.
2. Aplikasi Flask (`app.py`) menerima pertanyaan dari pengguna melalui endpoint `/api/chatbot`.
3. Fungsi `find_answer` menggunakan `difflib.get_close_matches` untuk mencari pertanyaan yang mirip dalam dataset.
4. Jika ditemukan pertanyaan yang mirip, jawaban yang sesuai dikembalikan.
5. Jika tidak ditemukan, respons default `"Maaf, saya tidak menemukan jawaban yang relevan."` dikembalikan.

## Kontribusi

Kontribusi dalam bentuk *pull request* sangat diharapkan untuk meningkatkan fungsionalitas dan akurasi chatbot.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.