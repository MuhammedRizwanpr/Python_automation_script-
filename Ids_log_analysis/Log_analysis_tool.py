import pandas as pd

df = pd.read_csv("sample.csv")

print("==== PREVIEW OF LOGS ====")
print(df.head())

print("\n==== ATTACK COUNT BY SIGNATURE ====")
print(df['signature'].value_counts())

print("\n==== ATTACK COUNT BY SOURCE IP ====")
print(df['src_ip'].value_counts())

high = df[df['severity'] == 'high']
print("\n==== HIGH SEVERITY ALERTS ====")
print(high)

attack_counts = df['src_ip'].value_counts()
repeat_attackers = attack_counts[attack_counts > 2]

print("\n==== REPEATED ATTACKERS (more than 2 alerts) ====")
print(repeat_attackers)

blocked = df[df['action'] == 'blocked']
print("\n==== BLOCKED EVENTS ====")
print(blocked)
