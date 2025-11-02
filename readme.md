# 🩺 PhysioNet Challenge 2019 - Training Set B (Early Prediction of Sepsis)

This repository focuses on **Training Set B** from the [PhysioNet/Computing in Cardiology Challenge 2019: Early Prediction of Sepsis](https://physionet.org/content/challenge-2019/1.0.0/).  
The goal of this challenge is to develop algorithms that can **detect sepsis early** from ICU time-series data.

---

## 📘 About the Dataset

The dataset consists of **multivariate clinical time series** data collected from Intensive Care Unit (ICU) patients.  
Each patient’s data is stored in a separate `.psv` file, where rows represent hourly measurements and columns represent clinical features and outcomes.

This project uses **only Training Set B**, which contains thousands of patient records.

---

## 📊 Data Description

Each `.psv` file includes **40 input variables** and **1 output label**, as summarized below.

### 🫀 Vital Signs (Columns 1–8)
| Column | Description | Unit |
|---------|--------------|------|
| HR | Heart rate | beats per minute |
| O2Sat | Pulse oximetry | % |
| Temp | Temperature | °C |
| SBP | Systolic blood pressure | mm Hg |
| MAP | Mean arterial pressure | mm Hg |
| DBP | Diastolic blood pressure | mm Hg |
| Resp | Respiration rate | breaths per minute |
| EtCO2 | End tidal carbon dioxide | mm Hg |

---

### 🧪 Laboratory Values (Columns 9–34)
| Column | Description | Unit |
|---------|--------------|------|
| BaseExcess | Measure of excess bicarbonate | mmol/L |
| HCO3 | Bicarbonate | mmol/L |
| FiO2 | Fraction of inspired oxygen | % |
| pH | Blood pH | — |
| PaCO2 | Partial pressure of CO₂ (arterial) | mm Hg |
| SaO2 | Oxygen saturation (arterial) | % |
| AST | Aspartate transaminase | IU/L |
| BUN | Blood urea nitrogen | mg/dL |
| Alkalinephos | Alkaline phosphatase | IU/L |
| Calcium | Serum calcium | mg/dL |
| Chloride | Serum chloride | mmol/L |
| Creatinine | Serum creatinine | mg/dL |
| Bilirubin_direct | Direct bilirubin | mg/dL |
| Glucose | Serum glucose | mg/dL |
| Lactate | Lactic acid | mg/dL |
| Magnesium | Serum magnesium | mmol/dL |
| Phosphate | Serum phosphate | mg/dL |
| Potassium | Serum potassium | mmol/L |
| Bilirubin_total | Total bilirubin | mg/dL |
| TroponinI | Troponin I | ng/mL |
| Hct | Hematocrit | % |
| Hgb | Hemoglobin | g/dL |
| PTT | Partial thromboplastin time | seconds |
| WBC | Leukocyte count | ×10³/µL |
| Fibrinogen | Fibrinogen | mg/dL |
| Platelets | Platelet count | ×10³/µL |

---

### 👤 Demographics (Columns 35–40)
| Column | Description |
|---------|--------------|
| Age | Patient age (100 = 90 or older) |
| Gender | Female = 0, Male = 1 |
| Unit1 | ICU type indicator (MICU) |
| Unit2 | ICU type indicator (SICU) |
| HospAdmTime | Hours between hospital and ICU admission |
| ICULOS | ICU length-of-stay (hours since ICU admit) |

---

### 🚨 Outcome (Column 41)
| Column | Description |
|---------|--------------|
| SepsisLabel | Binary label (1 = sepsis, 0 = non-sepsis). For sepsis patients, label switches from 0 → 1 at least 6 hours before clinical sepsis onset. |

---

## 🧹 Project Workflow

### 1. Data Download
Downloaded `.psv` files directly from PhysioNet using `wget`, with resume support:
```bash
wget -c "https://physionet.org/files/challenge-2019/1.0.0/training/training_setB/"
