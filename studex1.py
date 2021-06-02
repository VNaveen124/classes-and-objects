#studex1.py

class Student:pass  # here Student is called Class Name-->Programmer-defined data type

#main program
so1=Student()
print("Id of so1=",id(so1))
print("content of so=",so1. __dict__) # { }
#add  Instance Data members to an object so1
so1.stno=100
so1.sname="KVR"
so1.marks=55.55
#display the data
print("{}\t{}\t{}".format(so1.stno,so1.sname,so1.marks))
print("-----------------------------------------------------------")
so2=Student()
print("Id of so2=",id(so2))
#add  Instance Data members to an object so1
so2.stno=101
so2.sname="Omprkash"
so2.marks=65.55
print("Id of so2=",id(so2))
print("{}\t{}\t{}".format(so2.stno,so2.sname,so2.marks))
