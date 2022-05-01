import random

class Allotter:
    def __init__(self, subjects_and_teachers_list: list, classes: list, periods: int) -> None:
        self.SUBJECTS_AND_TEACHERS_LIST = subjects_and_teachers_list
        self.CLASSES = classes
        self.PERIODS = periods 
        self.CLASSWISE_TEACHER_ASSIGNMENT = self._make_classwise_teacher_assignment()
    
    def _make_classwise_teacher_assignment(self) -> dict:
        classwise_teacher_assignment = {}

        for cls in self.CLASSES:
            teacher_assignment = {}

            for subject in self.SUBJECTS_AND_TEACHERS_LIST.keys():
                teacher = random.choice(self.SUBJECTS_AND_TEACHERS_LIST[subject])
                teacher_assignment[subject] = teacher
            
            classwise_teacher_assignment[cls] = teacher_assignment
        
        return classwise_teacher_assignment
    
    def make_routine(self) -> dict:
        routine = dict([(cls, [ None ] * self.PERIODS) for cls in self.CLASSES])

        for cls in self.CLASSES:
            for period in range(self.PERIODS):
                assigned_teachers_combination = [ 
                    {subject: self.CLASSWISE_TEACHER_ASSIGNMENT[cls][subject]} 
                    for subject in self.CLASSWISE_TEACHER_ASSIGNMENT[cls] 
                ]

                # Removing unavailable teachers
                for other_cls in self.CLASSES:
                    if other_cls == cls:
                        continue
                    
                    adjacent_combination = routine[other_cls][period] 

                    if adjacent_combination in assigned_teachers_combination:
                        assigned_teachers_combination.remove(adjacent_combination)

                # Assigning a random subject-teacher combination to a period
                random_subject_teacher_combination = random.choice(assigned_teachers_combination)
                routine[cls][period] = random_subject_teacher_combination
        
        return routine 
    
    def reassign_teachers(self) -> None:
        self.CLASSWISE_TEACHER_ASSIGNMENT = self._make_classwise_teacher_assignment()