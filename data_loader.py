import fastf1

def setup_cache(cache_dir='cache'):
    fastf1.Cache.enable_cache(cache_dir)

def load_race_session(year, race, session_type = 'R'):
    session = fastf1.get_session(year, race, session_type)
    session.load()
    return session