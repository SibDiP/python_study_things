class Employee:
    # Python читает эту строку и ищет класс Boss. 
    # Но Boss описан ниже!
    def __init__(self, name: str, boss: Boss): 
        self.name = name
        self.boss = boss

class Boss:
    def __init__(self, name: str):
        self.name = name

# Результат: NameError: name 'Boss' is not defined
