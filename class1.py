class obj:
	def __init__(self):
		self.obj = input("Please, enter any item: ")
		self.f_n = input("Enter functions number: ")

	def obj_int(self):
		number = int(self.obj)
		if (number ** 0.5) == int(number ** 0.5):
			return number ** 0.5
		else: 
			return "Error sqrt this number"

	def obj_str(self):
		if len(self.obj) > 2:
			return self.obj[-2:]
		else:
			return "String len less then 2"
	def check(self):
		try: 
			int(self.obj)
			if self.f_n == "1":
				print(obj.obj_int(self))
			else:
				print(f"The {self.obj} isn't string")
		except ValueError:
			if self.f_n == "2":
  	                  	print(obj.obj_str(self))
			else:
				print(f"The {self.obj} isn't integer")

def main():
	member = obj()
	if member.f_n == "1" or member.f_n == "2":
		member.check()
	else:
		print("Invalid function number")

if __name__ == "__main__":
	main() 
