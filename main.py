from data_loader import setup_cache , load_race_session
from analysis import build_summary
from visualizer import plot_fastest_laps

def main():
    setup_cache()
    session = load_race_session(2025 , 'Monza')
    summary = build_summary(session.laps)
    plot_fastest_laps(summary, '2025 Monza GP - Fastest Laps')

if __name__ == '__main__':
    main()