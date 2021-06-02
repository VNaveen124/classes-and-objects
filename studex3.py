#studex3.py

class Student:pass  # here Student is called Class Name-->Programmer-defined data type
	


#main program
Student.crs="DS-AI"
so1=Student()
#add  Instance Data members to an object so1
so1.stno=100
so1.sname="KVR"
so1.marks=55.55
#display the data
print("\n{}\t{}\t{}\t{}".format(so1.stno,so1.sname,so1.marks,so1.crs ))
print("-----------------------------------------------------------")
so2=Student()
#add  Instance Data members to an object so2
so2.stno=101
so2.sname="Omprkash"
so2.marks=65.55
print("{}\t{}\t{}\t{}".format(so2.stno,so2.sname,so2.marks,Student.crs))
print("-----------------------------------------------------------")
so3=Student()
#add  Instance Data members to an object so3
so3.stno=102
so3.sname="dprasad"
so3.marks=66.55
print("{}\t{}\t{}\t{}".format(so3.stno,so3.sname,so3.marks,so3.crs))
