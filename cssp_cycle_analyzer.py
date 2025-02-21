import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('1IO_1blinking/cssp_cycle_times_1_1blink.csv')


# General analysis of cycle times
general_stats = df['Cycle Time ms'].describe()

# Analysis of cycle times by cycle state
state_stats = df.groupby('Cycle State')['Cycle Time ms'].describe()


# Print the results
print("General Statistics of Cycle Times:")
print(general_stats)

print("\nStatistics of Cycle Times by Cycle State:")
print(state_stats)


print("\nHighest cycle times:")
for state in df['Cycle State'].unique():
    print(f"\nTop 10 highest cycle times for Cycle State {state}:")
    print(df[df['Cycle State'] == state].nlargest(10, 'Cycle Time ms'))

print("\n Sum of cycle times:")
print(df.groupby('Cycle State')['Cycle Time ms'].sum())

# Plot statistics for each cycle state separately
for state in df['Cycle State'].unique():
    plt.figure(figsize=(10, 6))
    subset = df[df['Cycle State'] == state]
    plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'State {state}')
    plt.title(f'Distribution of Cycle Times for Cycle State {state}')
    plt.xlabel('Cycle Time (ms)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
# Plot statistics by cycle state
plt.figure(figsize=(10, 6))
for state in df['Cycle State'].unique():
    subset = df[df['Cycle State'] == state]
    plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'State {state}')
plt.title('Distribution of Cycle Times by Cycle State')
plt.xlabel('Cycle Time (ms)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()
