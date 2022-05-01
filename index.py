from pprint import pprint
from engine.allotter import Allotter

SUBJECTS_AND_TEACHERS = {
    "English": ["MM", "RS"],
    "Physics": ["RJ", "RT", "KT"],
    "Maths": ["MD", "SK"],
    "Chemistry": ["RN"],
}

CLASSES = [ "A", "B", "C" ]
PERIODS = 4

alloter = Allotter(
    subjects_and_teachers_list = SUBJECTS_AND_TEACHERS,
    classes = CLASSES,
    periods = PERIODS
)

routine = alloter.make_routine()
pprint(routine)