class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.age} years old student."

    # Name getter and setter
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # Age getter and setter
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

def main():
    student = get_student()
    print(student.name)

def get_student():
    name = input("Name: ")
    age = input("Age: ")
    student = Student(name, age)
    return student

if __name__ == "__main__":
    main()