class Patient:
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id

    def setName(self, n):
        self.name = n
    def getName(self):
        return self.name

    def setSsn(self, ssn):
        self.ssn = ssn
    def getSsn(self):
        return self.ssn

p = Patient()
p.setId(718)
p.setName("Bob")
p.setSsn(123456789)

print(p.getId())
print(p.getName())
print(p.getSsn())