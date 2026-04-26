#IMPORTING LIBRARIES
from os.path import join, dirname, abspath

#ABSOLUTE PATH
# abspath(__file__) -> .../Atomic launcher/code/settings.py
# dirname(...)      -> .../Atomic launcher/code
# dirname(dirname(...)) -> .../Atomic launcher (ROOT)
BASE_DIR = dirname(dirname(abspath(__file__)))
GAMES_DIR = join(BASE_DIR, 'games')

#WINDOW SETTINGS
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

#FPS / CLOCK SETTINGS
FPS = 60

#DEFAULT GAME DATA FILE
DATA_PATH = join(BASE_DIR, 'data', 'data.json')
DATA = {'NIGHT_DATA' : 1,
        'COMPLETION_STATE' : False,
        'NIGHT_ADVANCED_TO' : 1
}

#DEFAULT ANIMATRONIC AGGRESSION DATA FILE
AGGRESSION_DATA_PATH = join(BASE_DIR, 'data', 'aggression.json')
AGGRESSION_DATA = {
    'Chicka' : 1,
    'Freddy' : 1,
    'Bonnie' : 1,
    'Foxy' : 1
}
