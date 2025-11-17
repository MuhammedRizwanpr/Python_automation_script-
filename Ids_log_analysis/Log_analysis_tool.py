import pandas as pd

# Step 1: Load IDS logs
df = pd.read_csv("sample.csv")

# SHOW DATA
print("==== PREVIEW OF LOGS ====")
print(df.head())

# Step 2: Count attacks by signature
print("\n==== ATTACK COUNT BY SIGNATURE ====")
print(df['signature'].value_counts())

# Step 3: Count attacks by source IP (who attacks most?)
print("\n==== ATTACK COUNT BY SOURCE IP ====")
print(df['src_ip'].value_counts())

# Step 4: Filter only HIGH severity alerts
high = df[df['severity'] == 'high']
print("\n==== HIGH SEVERITY ALERTS ====")
print(high)

# Step 5: Detect repeated attackers (more than 2 alerts)
attack_counts = df['src_ip'].value_counts()
repeat_attackers = attack_counts[attack_counts > 2]

print("\n==== REPEATED ATTACKERS (more than 2 alerts) ====")
print(repeat_attackers)

# Step 6: Show only blocked events
blocked = df[df['action'] == 'blocked']
print("\n==== BLOCKED EVENTS ====")
print(blocked)
