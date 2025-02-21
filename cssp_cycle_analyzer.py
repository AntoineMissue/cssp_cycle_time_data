import pandas as pd
import matplotlib.pyplot as plt

def cssp_cycle_analyzer(file_path, scenario, save_bar, save_box):
    state_dict = {
        '0': 'Wait_Local_Write_State',
        '1': 'Wait_Global_Read_State',
        '2': 'Wait_External_Write_State',
        'RW': 'Complete Read/Write Cycle'
    }
    # Load the CSV file
    df = pd.read_csv(file_path)

    # General analysis of cycle times
    general_stats = df['Cycle Time ms'].describe()

    # Analysis of cycle times by cycle state
    state_stats = df.groupby('Cycle State')['Cycle Time ms'].describe()


    # Print the results
    # print("General Statistics of Cycle Times:")
    # print(general_stats)

    print("\nStatistics of Cycle Times by Cycle State:")
    print(state_stats)
    total_string = ""
    for state in df['Cycle State'].unique():
        state_data = df[df['Cycle State'] == state]['Cycle Time ms']
        min_time = state_data.min()
        avg_time = state_data.mean()
        std_time = state_data.std()
        max_time = state_data.max()
        print(f"Cycle State {state_dict[state]}: {min_time:.2f} / {avg_time:.2f}±{std_time:.2f} / {max_time:.2f}")
        total_string += f" {min_time:.2f} / {avg_time:.2f}±{std_time:.2f} / {max_time:.2f} &"
    print(total_string)

    # print("\nHighest cycle times:")
    # for state in df['Cycle State'].unique():
    #     print(f"\nTop 10 highest cycle times for Cycle State {state}:")
    #     print(df[df['Cycle State'] == state].nlargest(10, 'Cycle Time ms'))

    # print("\n Sum of cycle times:")
    # print(df.groupby('Cycle State')['Cycle Time ms'].sum())

    # Plot statistics for each cycle state separately
    # for state in df['Cycle State'].unique():
    #     plt.figure(figsize=(10, 6))
    #     subset = df[df['Cycle State'] == state]
    #     plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'State {state}')
    #     plt.title(f'Distribution of Cycle Times for Cycle State {state}')
    #     plt.xlabel('Cycle Time (ms)')
    #     plt.ylabel('Frequency')
    #     plt.legend()
    #     plt.grid(True)
    #     plt.show()
    # Plot statistics by cycle state
    plt.figure(figsize=(10, 6))
    for state in df['Cycle State'].unique():
        subset = df[df['Cycle State'] == state]
        plt.hist(subset['Cycle Time ms'], bins=30, alpha=0.7, label=f'{state_dict[state]}')
    plt.title(f'{scenario}: Distribution of Cycle Times by Cycle State')
    plt.xlabel('Cycle Time (ms)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.savefig(save_bar)

    # Box plot of cycle times by cycle state
    plt.figure(figsize=(12, 8))
    i = 0
    for state in df['Cycle State'].unique():
        i += 1
        subset = df[df['Cycle State'] == state]
        bg_colors = ['lightblue', 'lightgreen']
        colors = ['blue', 'green']
        plt.boxplot(subset['Cycle Time ms'], positions=[i], widths=0.4, patch_artist=True, boxprops=dict(facecolor=bg_colors[i % len(bg_colors)]), medianprops=dict(color=colors[i % len(colors)]), showfliers=False)
    plt.xticks(range(1, len(df['Cycle State'].unique()) + 1), [state_dict[state] for state in df['Cycle State'].unique()])
    plt.title(f'{scenario}: Box Plot of Cycle Times by Cycle State')
    plt.xlabel('Cycle State')
    plt.ylabel('Cycle Time (ms)')
    plt.grid(True)
    # plt.show()
    plt.savefig(save_box)

if __name__ == '__main__':
    files = ['1IO_1blinking/cssp_cycle_times_1_1blink.csv', '2IO_2blinking/cssp_cycle_times_2_2blink.csv', '8IO_0blinking/cssp_cycle_times_8_0blink_bis.csv', '8IO_4blinking/cssp_cycle_times_8_4blink.csv', '8IO_8blinking/cssp_cycle_times_8_8blink.csv']
    saves_bar = ['1IO_1blinking/cssp/histogramm_1IO_1.png', '2IO_2blinking/cssp/histogramm_2IO_2.png', '8IO_0blinking/cssp/histogramm_8IO_0.png', '8IO_4blinking/cssp/histogramm_8IO_4.png', '8IO_8blinking/cssp/histogramm_8IO_8.png']
    saves_box = ['1IO_1blinking/cssp/boxplot_1IO_1.png', '2IO_2blinking/cssp/boxplot_2IO_2.png', '8IO_0blinking/cssp/boxplot_8IO_0.png', '8IO_4blinking/cssp/boxplot_8IO_4.png', '8IO_8blinking/cssp/boxplot_8IO_8.png']
    for i in range(len(files)):
        cssp_cycle_analyzer(files[i], f'Scenario {i+1}', saves_bar[i], saves_box[i])