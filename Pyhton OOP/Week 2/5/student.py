class Student:
    def __init__(self,name,id,studies_in):
        self.name = name    
        self.id = id
        self.studies_in = studies_in

class Teacher:
    def __init__(self, name,id, subject):
        self.name = name    
        self.subject = subject
        self.id=id

class School:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.teachers=[]
    def add_teacher(self,name,subject):
        id=len(self.teachers) +101
        teacher=Teacher(name,id,subject)
        self.teachers.append(teacher)
    
    def enroll(self,name,fee):
        if fee<6000:
            print(f'Please pay {6000-fee} more')
            return
        else:
            id=len(self.students) +101
            student=Student(name,id,'CSE')
            self.students.append(student)
            print(f'{name} enrolled successfully with ID {id}')
        
    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('--------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All Done for now'

phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)