from flask import Flask, request, jsonify
import h5py
import json
import difflib  # Untuk fuzzy matching

app = Flask(__name__)

# Fungsi untuk mencari jawaban dengan pencocokan fleksibel
def find_answer(question):
    with h5py.File("data.h5", "r") as f:
        dataset = json.loads(f["dataset"][()])

    # Ambil semua pertanyaan dari dataset
    questions = [item["question"] for item in dataset]

    # Coba cari pertanyaan yang mirip dengan input pengguna
    closest_match = difflib.get_close_matches(question, questions, n=1, cutoff=0.4)  # Bisa diatur sensitivity

    if closest_match:
        for item in dataset:
            if item["question"] == closest_match[0]:
                return item["answer"]

    return "Maaf, saya tidak menemukan jawaban yang relevan."

@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Pertanyaan tidak boleh kosong"}), 400

    answer = find_answer(question)
    return jsonify({"question": question, "answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
