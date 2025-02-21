import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file
df = pd.read_csv('1IO_1blinking/cycle_time.csv')
df['Cycle Time ms'] = df['Cycle time'] * 1000
df['Request Time ms'] = df['Request time'] * 1000
# Analysis of cycle times by cycle state
state_stats = df.groupby('Read input')['Cycle Time ms'].describe()
request_stats = df.groupby('Read input')['Request Time ms'].describe()

print("\nStatistics of Cycle Times by Cycle State:")
print(state_stats)

print("\nStatistics of Request Times by Request:")
print(request_stats)

print("\nHighest cycle times:")
for state in df['Read input'].unique():
    print(f"\nTop 10 highest cycle times for Cycle State {state}:")
    print(df[df['Read input'] == state].nlargest(10, 'Cycle Time ms'))

print("\nHighest cycle times:")
for state in df['Read input'].unique():
    print(f"\nTop 10 highest cycle times for Cycle State {state}:")
    print(df[df['Read input'] == state].nlargest(10, 'Request Time ms'))

print("\nSum of cycle times:")
for state in df['Read input'].unique():
    print(f"\nSum of cycle times for Cycle State {state}:")
    print(df[df['Read input'] == state]['Cycle Time ms'].sum())

# Plot statistics for each cycle state separately
for state in df['Read input'].unique():
    plt.figure(figsize=(10, 6))
    subset = df[df['Read input'] == state]
    plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'{"Read" if state else "Write"} requests')
    plt.title(f'Distribution of Cycle Times for {"read" if state else "write"} requests')
    plt.xlabel('Cycle Time (ms)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
# Plot statistics by cycle state
for state in df['Read input'].unique():
    plt.figure(figsize=(10, 6))
    subset = df[df['Read input'] == state]
    plt.hist(subset['Request Time ms'], bins=30, alpha=0.7, label=f'{"Read" if state else "Write"} requests')
    plt.title(f'Distribution of Request Times for {"read" if state else "write"} requests')
    plt.xlabel('Cycle Time (ms)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()