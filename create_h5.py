import h5py
import json

data = [
    {"question": "Apa itu Laravel?", "answer": "Laravel adalah framework PHP untuk pengembangan aplikasi web."},
    {"question": "Apa itu Docker?", "answer": "Docker adalah platform untuk mengembangkan dan menjalankan aplikasi dalam container."},
    {"question": "Apa itu API?", "answer": "API adalah antarmuka yang memungkinkan aplikasi berkomunikasi satu sama lain."},
    {"question": "Apa itu Machine Learning?", "answer": "Machine Learning adalah bagian dari AI yang memungkinkan sistem belajar dari data."}
]

# Simpan dataset dalam file H5
with h5py.File("data.h5", "w") as f:
    f.create_dataset("dataset", data=json.dumps(data))

print("Dataset H5 berhasil dibuat!")
