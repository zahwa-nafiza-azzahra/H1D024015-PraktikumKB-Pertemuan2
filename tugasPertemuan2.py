# ============================================================
# SISTEM LOGIKA FUZZY - KECEPATAN KIPAS ANGIN
# Praktikum Kecerdasan Buatan - Logika Fuzzy 1
# ============================================================

# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ============================================================
# 1. MENYIAPKAN HIMPUNAN FUZZY
# ============================================================

# Antecedent (Input)
suhu      = ctrl.Antecedent(np.arange(0, 41, 1),  'suhu')        # 0 – 40 °C
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan') # 0 – 100 %

# Consequent (Output)
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')   # 0 – 100

# ------------------------------------------------------------------
# Fungsi Keanggotaan: Suhu
#   Dingin : trimf [0,  0, 20]
#   Sejuk  : trimf [10, 20, 30]
#   Panas  : trimf [20, 40, 40]
# ------------------------------------------------------------------
suhu['Dingin'] = fuzz.trimf(suhu.universe, [0,  0,  20])
suhu['Sejuk']  = fuzz.trimf(suhu.universe, [10, 20, 30])
suhu['Panas']  = fuzz.trimf(suhu.universe, [20, 40, 40])

# ------------------------------------------------------------------
# Fungsi Keanggotaan: Kelembapan
#   Rendah : trimf [0,   0,  50]
#   Sedang : trimf [25, 50,  75]
#   Tinggi : trimf [50, 100, 100]
# ------------------------------------------------------------------
kelembapan['Rendah'] = fuzz.trimf(kelembapan.universe, [0,   0,   50])
kelembapan['Sedang'] = fuzz.trimf(kelembapan.universe, [25,  50,  75])
kelembapan['Tinggi'] = fuzz.trimf(kelembapan.universe, [50, 100, 100])

# ------------------------------------------------------------------
# Fungsi Keanggotaan: Kecepatan Kipas
#   Lambat : trimf [0,   0,  50]
#   Sedang : trimf [25, 50,  75]
#   Cepat  : trimf [50, 100, 100]
# ------------------------------------------------------------------
kecepatan['Lambat'] = fuzz.trimf(kecepatan.universe, [0,   0,   50])
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [25,  50,  75])
kecepatan['Cepat']  = fuzz.trimf(kecepatan.universe, [50, 100, 100])

# ============================================================
# 2. MENAMPILKAN GRAFIK HIMPUNAN FUZZY
# ============================================================
suhu.view()
kelembapan.view()
kecepatan.view()
input("\nTekan ENTER untuk melanjutkan ke proses inferensi...")

# ============================================================
# 3. ATURAN FUZZY (IF-THEN Rules)
# ============================================================
#  Aturan 1: Jika suhu DINGIN dan kelembapan RENDAH
#            maka kecepatan kipas LAMBAT
aturan1 = ctrl.Rule(suhu['Dingin'] & kelembapan['Rendah'], kecepatan['Lambat'])

#  Aturan 2: Jika suhu SEJUK atau kelembapan SEDANG
#            maka kecepatan kipas SEDANG
aturan2 = ctrl.Rule(suhu['Sejuk'] | kelembapan['Sedang'], kecepatan['Sedang'])

#  Aturan 3: Jika suhu PANAS atau kelembapan TINGGI
#            maka kecepatan kipas CEPAT
aturan3 = ctrl.Rule(suhu['Panas'] | kelembapan['Tinggi'], kecepatan['Cepat'])

# ============================================================
# 4. INFERENCE ENGINE DAN SISTEM FUZZY
# ============================================================
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

# ============================================================
# 5. PENGUJIAN SISTEM
# ============================================================
print("=" * 55)
print("  SISTEM FUZZY – KECEPATAN KIPAS ANGIN")
print("=" * 55)

# --- Test Case 1: Suhu dingin, kelembapan rendah ---
system.input['suhu']       = 10   # °C  (Dingin)
system.input['kelembapan'] = 20   # %   (Rendah)
system.compute()
print(f"\n[Test 1] Suhu: 10°C | Kelembapan: 20%")
print(f"  → Kecepatan Kipas : {system.output['kecepatan']:.2f} / 100")
kecepatan.view(sim=system)
input("  Tekan ENTER untuk test berikutnya...")

# --- Test Case 2: Suhu sejuk, kelembapan sedang ---
system.input['suhu']       = 22   # °C  (Sejuk)
system.input['kelembapan'] = 55   # %   (Sedang)
system.compute()
print(f"\n[Test 2] Suhu: 22°C | Kelembapan: 55%")
print(f"  → Kecepatan Kipas : {system.output['kecepatan']:.2f} / 100")
kecepatan.view(sim=system)
input("  Tekan ENTER untuk test berikutnya...")

# --- Test Case 3: Suhu panas, kelembapan tinggi ---
system.input['suhu']       = 35   # °C  (Panas)
system.input['kelembapan'] = 85   # %   (Tinggi)
system.compute()
print(f"\n[Test 3] Suhu: 35°C | Kelembapan: 85%")
print(f"  → Kecepatan Kipas : {system.output['kecepatan']:.2f} / 100")
kecepatan.view(sim=system)
input("  Tekan ENTER untuk selesai...")

print("\nProgram selesai.")