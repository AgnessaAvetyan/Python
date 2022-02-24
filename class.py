class student:
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks
	def __str__(self):
		print(f"Student name is {self.name}, mark is {self.marks}")
	def __setitem__(self, new_name, new_marks):
		self.name = new_name
		self.marks = new_marks
		return f"Student name is {new_name}, mark is {new_marks}"

a = student("Agnes", 2)
a.__str__()
print(a.__setitem__("Ashot", 5))
