#studex2.py

class Student:  # here Student is called Class Name-->Programmer-defined data type
	crs="PYTHON"

#main program
	
so1=Student()
#add  Instance Data members to an object so1
so1.stno=100
so1.sname="KVR"
so1.marks=55.55
#display the data
print("{}\t{}\t{}\t{}".format(so1.stno,so1.sname,so1.marks,so1.crs ))
print("-----------------------------------------------------------")
so2=Student()
#add  Instance Data members to an object so1
so2.stno=101
so2.sname="Omprkash"
so2.marks=65.55
print("{}\t{}\t{}\t{}".format(so2.stno,so2.sname,so2.marks,so2.crs))
