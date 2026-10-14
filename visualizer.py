import matplotlib.pyplot as plt

def plot_fastest_laps(summary, title):
    seconds = summary['FastestLap'].dt.total_seconds()

    plt.figure(figsize=(12, 6))
    plt.bar(summary.index, seconds)
    plt.xlabel('Driver')
    plt.ylabel('FastestLap(s)')
    plt.title(title)
    plt.ylim(seconds.min() - 0.5, seconds.max() + 0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()