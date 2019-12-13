class Student:
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id

    def setName(self, n):
        self.name = n
    def getName(self):
        return self.name

s = Student()
s.setId(123)
s.setName("John")
print(s.getId())
print(s.getName())