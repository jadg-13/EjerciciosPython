class Person:
    def __init__(self, firstName, secondName, birthdate):
        self.firstName = firstName
        self.secondName = secondName
        self.birthdate = birthdate

    def getEmail(self):
        return f"{self.firstName}.{self.secondName}@gmail.com"

    def getAge(self):
        return 2023 - self.birthdate

    def isAdult(self):
        # operador ternario
        return "Mayor de edad" if self.getAge() >= 18 else "Menor de edad"
