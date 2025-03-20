#Strings--> Set of literals(digits,alphabets,special character)and enclosed with quotes
# Sequence,order,indexing,follows,slicing and immutable(not modifyable) data type

#EMoty string
# s="" 
# print(s,type(s))
# msg=str()
# print(msg,type(msg))

# s="a"
# print(s,type(s))
# s1="python is easy"
# print(s1,type(s1))
# s2="335465434"
# print(s2),type(s2)
# features="""
# dynamic
# easy
# case-sensitive
# """
# print(features,type(features))

# name=input("Enter name = ")
# print(name,type(name))
# percentage=str(77.878)
# print(percentage,type(percentage))

msg="welcome"
print(msg)
#positive index
# print("first char=",msg[0])
# print("second char=",msg[1])
# print(len(msg))
# print("modle char=",msg[len(msg)//2])
# print("second char=",msg[len(msg)-2])
# print("last char=",msg[len(msg)-1])

#neagative index
print("first char=",msg[-len(msg)])
print("second char=",msg[-len(msg)+1])
print(len(msg))
print("modle char=",msg[-len(msg)//2])
print("second char=",msg[-2])
print("last char=",msg[-1])