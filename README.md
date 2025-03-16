**FuzzyMatchChatbot** adalah proyek chatbot berbasis Python yang menggunakan metode pencocokan fleksibel (*fuzzy matching*) untuk memberikan jawaban yang lebih relevan terhadap pertanyaan pengguna. Data chatbot disimpan dalam format H5 untuk efisiensi dan proyek ini dikembangkan sebagai mikroservice menggunakan Flask.  

### **Fitur Utama:**  
1. **Pencocokan Fleksibel (Fuzzy Matching)**  
   Chatbot ini menggunakan algoritma `difflib.get_close_matches` untuk mengenali pertanyaan yang mirip, meskipun tidak ditulis persis seperti data yang tersimpan.  

2. **Penyimpanan Data dalam Format H5**  
   Dataset chatbot disimpan dalam file H5 agar lebih efisien dan cepat diakses.  

3. **Dibangun sebagai Mikroservice dengan Flask**  
   Aplikasi ini dikembangkan menggunakan Flask sehingga bisa diintegrasikan dengan aplikasi lain dengan mudah.  

4. **Respons yang Relevan**  
   Dengan metode pencocokan fuzzy, chatbot dapat memahami variasi bahasa alami dan memberikan jawaban yang lebih akurat.  

### **Cara Menggunakan:**  
1. **Clone repositori GitHub**  
   Jalankan perintah berikut untuk mengunduh proyek:  
   ```bash
   git clone https://github.com/AldevaRizky/FuzzyMatchChatbot.git
   cd FuzzyMatchChatbot
   ```  

2. **Install dependensi yang diperlukan**  
   Pastikan Python sudah terinstal, lalu jalankan perintah berikut:  
   ```bash
   pip install Flask h5py
   ```  

3. **Menjalankan aplikasi**  
   Setelah semua dependensi terinstal, jalankan chatbot dengan perintah berikut:  
   ```bash
   python app.py
   ```  
   Aplikasi akan berjalan di alamat `http://127.0.0.1:5000/api/chatbot`.  

4. **Menguji API Chatbot**  
   Gunakan Postman atau aplikasi serupa untuk mengirimkan permintaan POST ke endpoint `/api/chatbot` dengan format JSON berikut:  
   ```json
   {
     "question": "Apa kamu tahu Laravel?"
   }
   ```  
   Chatbot akan merespons dengan jawaban yang sesuai, misalnya:  
   ```json
   {
     "question": "Apa kamu tahu Laravel?",
     "answer": "Laravel adalah framework PHP untuk pengembangan aplikasi web."
   }
   ```  

### **Struktur Proyek:**  
- **`app.py`** → Kode utama aplikasi Flask  
- **`create_h5.py`** → Skrip untuk membuat dataset H5  
- **`data.h5`** → Dataset chatbot dalam format H5  
- **`README.md`** → Dokumentasi proyek  

### **Cara Kerja Chatbot:**  
1. Semua pertanyaan dan jawaban chatbot disimpan dalam file `data.h5`.  
2. Aplikasi Flask menerima pertanyaan dari pengguna melalui endpoint `/api/chatbot`.  
3. Fungsi `find_answer` menggunakan `difflib.get_close_matches` untuk mencari pertanyaan yang paling mirip dalam dataset.  
4. Jika ada pertanyaan yang cocok, chatbot akan mengembalikan jawaban yang sesuai.  
5. Jika tidak ditemukan jawaban yang relevan, chatbot akan memberikan respons default:  
   **"Maaf, saya tidak menemukan jawaban yang relevan."**  

### **Kontribusi:**  
Jika ingin berkontribusi, silakan buat *pull request* di repositori GitHub untuk membantu meningkatkan akurasi dan fitur chatbot ini.  

### **Lisensi:**  
Proyek ini menggunakan **Lisensi MIT**, sehingga bebas digunakan dan dikembangkan lebih lanjut.