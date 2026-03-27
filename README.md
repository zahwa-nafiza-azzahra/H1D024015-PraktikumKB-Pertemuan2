# 🌀 Sistem Logika Fuzzy – Kecepatan Kipas Angin

> Tugas Praktikum Kecerdasan Buatan – Logika Fuzzy 1  
> Implementasi sistem inferensi fuzzy menggunakan Python & SciKit-Fuzzy

---

## 📋 Deskripsi

Sistem ini menggunakan **Logika Fuzzy** untuk menentukan kecepatan kipas angin secara otomatis berdasarkan kondisi lingkungan, yaitu **suhu udara** dan **kelembapan udara**. Sistem mensimulasikan cara berpikir manusia dalam mengatur kipas — misalnya, jika suhu panas dan udara lembap, maka kipas diputar lebih cepat.

---

## ⚙️ Variabel Sistem

### 🔵 Input (Antecedent)

| Variabel | Rentang | Himpunan Fuzzy |
|---|---|---|
| Suhu Udara | 0 – 40 °C | Dingin, Sejuk, Panas |
| Kelembapan | 0 – 100 % | Rendah, Sedang, Tinggi |

### 🟢 Output (Consequent)

| Variabel | Rentang | Himpunan Fuzzy |
|---|---|---|
| Kecepatan Kipas | 0 – 100 | Lambat, Sedang, Cepat |

---

## 📐 Fungsi Keanggotaan

Semua variabel menggunakan fungsi **Triangular (trimf)**:

**Suhu:**
```
Dingin → trimf [0,  0,  20]
Sejuk  → trimf [10, 20, 30]
Panas  → trimf [20, 40, 40]
```

**Kelembapan:**
```
Rendah → trimf [0,   0,  50]
Sedang → trimf [25, 50,  75]
Tinggi → trimf [50, 100, 100]
```

**Kecepatan:**
```
Lambat → trimf [0,   0,  50]
Sedang → trimf [25, 50,  75]
Cepat  → trimf [50, 100, 100]
```

---

## 📏 Aturan Fuzzy

| No. | IF (Antecedent) | THEN (Consequent) |
|---|---|---|
| 1 | Suhu **DINGIN** AND Kelembapan **RENDAH** | Kecepatan **LAMBAT** |
| 2 | Suhu **SEJUK** OR Kelembapan **SEDANG** | Kecepatan **SEDANG** |
| 3 | Suhu **PANAS** OR Kelembapan **TINGGI** | Kecepatan **CEPAT** |

---

## 🧪 Hasil Pengujian

| Test | Suhu (°C) | Kelembapan (%) | Kecepatan Output |
|---|---|---|---|
| Test 1 | 10 (Dingin) | 20 (Rendah) | ~16.67 → **Lambat** |
| Test 2 | 22 (Sejuk)  | 55 (Sedang) | ~50.00 → **Sedang** |
| Test 3 | 35 (Panas)  | 85 (Tinggi) | ~75.00 → **Cepat**  |

---

## 🚀 Cara Menjalankan

### 1. Clone Repositori
```bash
git clone https://github.com/NIM/NIM-PraktikumKB-Pertemuan2.git
cd NIM-PraktikumKB-Pertemuan2
```

### 2. Install Dependencies
```bash
pip install scikit-fuzzy scipy numpy packaging networkx matplotlib
```

### 3. Jalankan Program
```bash
# Tugas – Kipas Angin
python kipas_angin.py

# Percobaan 1 – Kualitas Restoran
python restoran.py

# Percobaan 2 – Perusahaan Soft Drink
python produksi.py
```

---

## 🔄 Alur Kerja Sistem (Fuzzy Inference)

```
INPUT NILAI TEGAS
       │
       ▼
  FUZZIFICATION
  (nilai → derajat keanggotaan)
       │
       ▼
  RULE APPLICATION
  (evaluasi aturan IF-THEN)
       │
       ▼
   AGGREGATION
  (gabungkan semua output fuzzy)
       │
       ▼
  DEFUZZIFICATION
  (fuzzy → nilai tegas)
       │
       ▼
  OUTPUT KECEPATAN KIPAS
```

---

## 🛠️ Teknologi yang Digunakan

| Library | Kegunaan |
|---|---|
| `scikit-fuzzy` | Komputasi logika fuzzy & sistem inferensi |
| `numpy` | Operasi array & universe of discourse |
| `matplotlib` | Visualisasi grafik fungsi keanggotaan |

---

## 📦 Requirements

```
Python >= 3.7
scikit-fuzzy
scipy
numpy
packaging
networkx
matplotlib
```

---

## 👤 Informasi

| | |
|---|---|
| **Mata Kuliah** | Kecerdasan Buatan (Praktikum) |
| **Pertemuan** | 2 – Logika Fuzzy 1 |
| **Metode** | Mamdani Fuzzy Inference System |

---

> *Dibuat sebagai bagian dari Praktikum Kecerdasan Buatan*
