import pandas as pd

def _filter_laps(laps, accurate_only):
    if accurate_only:
        return laps[laps['IsAccurate'] == True ]
    return laps

def get_extreme_lap (laps , mode='fastest' , accurate_only =True):

    laps = _filter_laps(laps , accurate_only)
    if mode == 'fastest':
        result = laps.groupby('Driver')['LapTime'].min()
    elif mode == 'slowest':
        result = laps.groupby('Driver')['LapTime'].max()
    else:
        raise ValueError("Mode Should be fastest or slowest !!! ")
    return result.sort_values()

def get_consistency(laps , accurate_only=True):
    laps = _filter_laps(laps , accurate_only)
    result = laps.groupby('Driver')['LapTime'].std()
    return result.sort_values()

def build_summary(laps , accurate_only=True):
    fastest = get_extreme_lap(laps, 'fastest' , accurate_only)
    consistency = get_consistency(laps , accurate_only)
    summary = pd.concat([fastest, consistency], axis = 1)
    summary.columns = ['FastestLap', 'Consistency']
    return summary.sort_values('FastestLap')
