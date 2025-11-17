# IDS Log Analysis Tool

A simple Intrusion Detection System (IDS) log analysis project using Python and Pandas. This tool helps you analyze attack patterns, repeated attacker IPs, signatures, and severity levels.

---

## 📥 How to Download This Project

You can download the project in **two ways**:

### **1. Download ZIP (Easy Method)**

1. Go to the GitHub repository.
2. Click the **Code** (green button).
3. Click **Download ZIP**.
4. Extract the folder on your system.

---

### **2. Clone Using Git (Recommended)**

If you have Git installed, run:

```
git clone https://github.com/MuhammedRizwanpr/Python_automation_script-.git
```

This will download the entire project folder.

---

## 🚀 How to Use This IDS Analyzer

Follow these steps after downloading the project:

### **1. Install Dependencies (Pandas)**

Navigate to the project folder:

```
cd ids-analysis-tool
```

Create a virtual environment (recommended):

```
python3 -m venv myenv
source myenv/bin/activate
```

Install Pandas:

```
pip install pandas
```

---

### **2. Prepare Your IDS Log File**

Place your log file in the project folder.
Make sure it follows the format used in the example:

- timestamp
- src\_ip
- dst\_ip
- signature
- severity
- action

Name the file as:

```
ids_logs.csv
```

---

### **3. Run the Analyzer Script**

Use:

```
python3 ids_analyze.py
```

The script will display:

- Preview of logs
- Attack count by signature
- Attack count by IP
- High severity alerts
- Repeated attackers
- Full details of repeated attacker IPs

---

## 📸 Screenshot of Script Output

(Place your screenshot here)


# Example placeholder:
![IDS Analysis Output](/screenshot/ids_log_analysis.png)


---

## 📝 Notes

- This tool is for **learning and cybersecurity analysis**.
- You can modify the CSV file to test different attack logs.
- Extend the script to perform advanced detection.

---

## 🛡️ Author

Created for cybersecurity practice and log analysis.

---

## ⭐ Contributions

You can improve this project by:

- Adding visualizations (matplotlib)
- Adding JSON/Excel log support
- Detecting anomalies

