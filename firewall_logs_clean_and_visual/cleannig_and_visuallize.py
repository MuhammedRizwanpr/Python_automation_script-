import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

df = pd.read_csv("dirty_logs.csv")
print("===== RAW DIRTY LOG =====")
print(df)

df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df.dropna(subset=['timestamp']) 

df['action'] = df['action'].str.lower()
df['severity'] = df['severity'].str.lower()
df['message'] = df['message'].str.lower()

df = df.drop_duplicates()

df = df.dropna(subset=['src_ip', 'dst_ip'])

def is_valid_ip(ip):
    pattern = r'\b\d{1,3}(?:\.\d{1,3}){3}\b'
    if not re.match(pattern, ip):
        return False
    parts = ip.split('.')
    return all(0 <= int(part) <= 255 for part in parts)

df = df[df['src_ip'].apply(is_valid_ip)]
df = df[df['dst_ip'].apply(is_valid_ip)]

df['message'] = df['message'].str.replace(r'\s+', ' ', regex=True)

df = df[df['action'].str.strip() != ""]

df = df.fillna("unknown")

df = df.sort_values(by='timestamp')

print("\n===== CLEANED FIREWALL LOG =====")
print(df)
plt.figure(figsize=(10,4))
df['src_ip'].value_counts().plot(kind='bar')
plt.yticks(range(0,5))
plt.title("Attacks by Source IP")
plt.xlabel("Source IP")
plt.ylabel("Number of Attacks")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
df['severity'].value_counts().plot(kind='bar')
plt.title("Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
df['action'].value_counts().plot(kind='bar')
plt.title("Firewall Action Summary")
plt.xlabel("Action")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,4))
df.set_index('timestamp')['src_ip'].resample('1T').count().plot()
plt.title("Firewall Events Over Time (per minute)")
plt.xlabel("Time")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.show()
