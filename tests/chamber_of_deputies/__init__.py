def get_fixtures_dir():
    import os

    FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')
    return FIXTURES_DIR
