#program for cal area and perimeter of Circle  using classes and objects
#Circledemo1.py
class Circle:
	@classmethod
	def  setpi(cls):   # class Level method
		cls.pi=3.14    # class level data member
	def readradious(self, op):
		self.r=float(input("Enter Radious for {}:".format(op) ))
		return self.r

class Hyderabad:
	@staticmethod
	def  operations(c):
		rad=c.readradious("area")
		ac=3.14*rad*rad
		print("Area of Circle={}".format(ac))
		rad=c.readradious("peri")
		pc=2*3.14*rad
		print("\nperi of Circle={}".format(pc))
	
#main program
Circle.setpi()
co=Circle()
Hyderabad.operations(co)
