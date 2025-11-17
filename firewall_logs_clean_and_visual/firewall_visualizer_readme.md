# Firewall Log Cleaner & Visualizer

A simple cybersecurity tool that **cleans dirty firewall logs** and **visualizes attacks** using Pandas and Matplotlib. This project is perfect for beginners learning log analysis and data visualization.

---

## 🛡️ What This Tool Does

This project performs two major tasks:

### **1. Log Cleaning**

The tool automatically cleans messy firewall logs by:

- removing extra spaces
- fixing incorrect timestamps
- converting uppercase/lowercase
- removing duplicate logs
- removing rows with missing IPs/actions
- validating IP addresses
- correcting messy message fields
- sorting logs by time

After cleaning, you get a clean and consistent CSV file ready for analysis.

### **2. Log Visualization**

The tool generates easy-to-understand graphs:

- **Attacks by Source IP (bar chart)**
- **Severity Distribution (bar chart)**
- **Firewall Actions Summary (blocked/allowed)**
- **Attacks Over Time (line graph)**

These charts help you identify repeated attackers, severity patterns, and activity over time.

---

## 📥 How to Download This Tool

You can download it in two simple ways:

### **Option 1 — Download ZIP (Easy)**

1. Go to the GitHub repository.
2. Click the **Code** (green button).
3. Select **Download ZIP**.
4. Extract the folder on your computer.

### **Option 2 — Clone Using Git (Recommended)**

If you have Git installed:

```
git clone https://github.com/MuhammedRizwanpr/Python_automation_script-.git
```

This downloads the full project folder.

---

## ⚙️ How It Works (Simple Explanation)

### **Step 1 — Load Log File**

The tool reads your dirty firewall log.

### **Step 2 — Clean Data**

It removes bad data, fixes formatting, and ensures everything is valid.

### **Step 3 — Save Clean File**

A cleaned version of your log is saved as:

```
dirty_logs.csv
```

### **Step 4 — Visualize Data**

The tool generates graphs showing:

- which IP attacked most
- severity of alerts
- block vs allow actions
- attacks timeline

---

## 📦 Requirements

Before running this tool, install:

- **Pandas**
- **Matplotlib**

You can install them using:

```
sudo apt install python3-pandas python3-matplotlib
```

Or using pip:

```
pip install pandas matplotlib --break-system-packages
```

---

## ▶️ How to Run the Tool

1. Open the project folder.
2. Make sure your log file is named:

```
dirty_firewall_logs.csv
```

3. Run the script:

```
python3 firewall_clean_and_visualize.py
```

4. Your graphs will appear on screen and the cleaned log will be saved.

---

## 📸 Screenshot

Add a screenshot of your tool running:

```
![Firewall Tool Output](./screenshot.png)
```

---

## 📝 Notes

- This project is for cybersecurity learning and log analysis.
- You can replace the log file with any firewall/IDS logs.
- Feel free to improve graphs or add more analysis.

---

## ⭐ Contributions

You can extend this project by adding:

- GeoIP lookup for attacker locations
- Pie charts for severity
- CSV / JSON import support
- Anomaly detection

---

## 👨‍💻 Author

Created as a beginner-friendly cybersecurity project for learning log cleaning and visualization.

