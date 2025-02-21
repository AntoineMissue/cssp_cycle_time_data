import pandas as pd
import matplotlib.pyplot as plt

def daughter_cycle_analyzer(file_path, scenario, save_bar, save_box):
    # Load the CSV file
    df = pd.read_csv(file_path)
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
    # for state in df['Read input'].unique():
    #     plt.figure(figsize=(10, 6))
    #     subset = df[df['Read input'] == state]
    #     plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'{"Read" if state else "Write"} requests')
    #     plt.title(f'Distribution of Cycle Times for {"read" if state else "write"} requests')
    #     plt.xlabel('Cycle Time (ms)')
    #     plt.ylabel('Frequency')
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()

    # Plot statistics by cycle state for request times
    # for state in df['Read input'].unique():
    #     plt.figure(figsize=(10, 6))
    #     subset = df[df['Read input'] == state]
    #     plt.hist(subset['Request Time ms'], bins=30, alpha=0.7, label=f'{"Read" if state else "Write"} requests')
    #     plt.title(f'Distribution of Request Times for {"read" if state else "write"} requests')
    #     plt.xlabel('Cycle Time (ms)')
    #     plt.ylabel('Frequency')
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()
        # Plot all cycle states in one figure for cycle times
        # plt.figure(figsize=(10, 6))
        # for state in df['Read input'].unique():
        #     subset = df[df['Read input'] == state]
        #     plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'{"Read" if state else "Write"} requests')
        # plt.title('Distribution of Cycle Times by Cycle State')
        # plt.xlabel('Cycle Time (ms)')
        # plt.ylabel('Frequency')
        # plt.legend()
        # plt.grid(True)
        # plt.show()

    # Plot all cycle states in one figure for request times
    plt.figure(figsize=(12, 8))
    for state in df['Read input'].unique():
        subset = df[df['Read input'] == state]
        plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.5, label=f'{"Read" if state else "Write"} Cycle Time')
        plt.hist(subset['Request Time ms'], bins=30, alpha=0.5, label=f'{"Read" if state else "Write"} Request Time')
    plt.title(f'{scenario}: Distribution of Cycle and Request Times by Cycle State')
    plt.xlabel('Time (ms)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.savefig(save_bar)

    plt.figure(figsize=(12, 8))
    i = 0
    for state in df['Read input'].unique():
        i += 1
        subset = df[df['Read input'] == state]
        bg_colors = ['lightblue', 'lightgreen']
        colors = ['blue', 'green']
        bg_colors_req = ['moccasin', 'salmon']
        colors_req = ['orange', 'red']
        plt.boxplot(subset['Cycle Time ms'], positions=[i], widths=0.4, patch_artist=True, boxprops=dict(facecolor=bg_colors[i % len(bg_colors)]), medianprops=dict(color=colors[i % len(colors)]), showfliers=False)
        plt.boxplot(subset['Request Time ms'], positions=[i+0.5], widths=0.4, patch_artist=True, boxprops=dict(facecolor=bg_colors_req[i % len(bg_colors_req)]), medianprops=dict(color=colors_req[i % len(colors_req)]), showfliers=False)
    plt.xticks(range(1, len(df['Read input'].unique()) + 1), [f'{"Read" if state else "Write"}' for state in df['Read input'].unique()])
    plt.title(f'{scenario}: Box Plot of Cycle and Request Times by Cycle State')
    plt.xlabel('Cycle State')
    plt.ylabel('Time (ms)')
    plt.legend(['Read Cycle Time', 'Read Request Time', 'Write Cycle Time', 'Write Request Time'])
    plt.grid(True)
    # plt.show()
    plt.savefig(save_box)

if __name__ == '__main__':
    files = ['1IO_1blinking/cycle_time.csv', '2IO_2blinking/cycle_time.csv', '8IO_0blinking/cycle_time.csv', '8IO_4blinking/cycle_time.csv', '8IO_8blinking/cycle_time.csv']
    scenarios = ['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4', 'Scenario 5']
    saves_bar = ['1IO_1blinking/daughter_board/histogramm_1IO_1.png', '2IO_2blinking/daughter_board/histogramm_2IO_2.png', '8IO_0blinking/daughter_board/histogramm_8IO_0.png', '8IO_4blinking/daughter_board/histogramm_8IO_4.png', '8IO_8blinking/daughter_board/histogramm_8IO_8.png']
    saves_box = ['1IO_1blinking/daughter_board/boxplot_1IO_1.png', '2IO_2blinking/daughter_board/boxplot_2IO_2.png', '8IO_0blinking/daughter_board/boxplot_8IO_0.png', '8IO_4blinking/daughter_board/boxplot_8IO_4.png', '8IO_8blinking/daughter_board/boxplot_8IO_8.png']
    for i in range(len(files)):
        daughter_cycle_analyzer(files[i], scenarios[i], saves_bar[i], saves_box[i])