class Student:
    """Provides a simple class to find the student with highest gpa and
prints out its name,hours and gpa."""
    def __init__(self,name,hours,qpoints):
        self.name=name
        self.hours=float(hours)
        self.qpoints=float(qpoints)
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def gpa(self):
        return self.qpoints/self.hours
  
