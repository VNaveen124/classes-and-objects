#program for cal area and perimeter of Circle  using classes and objects
#Circledemo.py
class Circle:
	@classmethod
	def  setpi(cls):   # class Level method
		cls.pi=3.14    # class level data member
	
	def  circlearea(self):
		print("---------------------------------------------------------------------")
		self.r=float(input("Enter Radious for cal Area of Circle:"))
		self.ac=Circle.pi*self.r*self.r
		print("Area of Circle={}".format(self.ac))
		print("---------------------------------------------------------------------")

	def  circleperi(self):
		print("--------------------------------------------------------------------")
		self.r=float(input("Enter Radious for cal Peri of Circle:"))
		self.pc=2*self.pi*self.r
		print("Area of Circle={}".format(self.pc))
		print("--------------------------------------------------------------------")

#main program
Circle.setpi()
co=Circle()
co.circleperi()
co.circlearea()
