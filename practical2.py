'''
newArray =[
    42,                # Integer
    3.14,              # Float
    "Hello, World!",   # String
    True,              # Boolean
    [1, 2, 3]          # List
]

print(newArray)
length = len(newArray)
print( length)
firstArrayLength = len(newArray[2])
print(firstArrayLength)
newArray.append("Ugyen Dema")
print(newArray)
secondArrayLength = len(newArray[5])
print(secondArrayLength)
'''
newArray= ["ECE", "SWE", "IT", "EEE", "ME", "CE", "ICE", "A", "WRE", "EG"]
arraylen =len(newArray)
for index in range(arraylen):
    print(newArray[index])

newArray = ["ECE", "SWE", "IT", "EEE", "ME", "CE", "ICE", "A", "WRE", "EG"]
lowercaseArray = [element.lower() for element in newArray]

print("Original array:", newArray)
print("Lowercase array:", lowercaseArray)