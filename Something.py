name = input("Enter your name:")
print(name)

genYear = int(input("Enter your birth year:"))
if  1965 <= genYear and genYear >= 1979:
    genType = "Baby Boomer"
elif 1980 <= genYear and genYear >= 1994:
    genType = "Millennial"
elif 1995 <= genYear and genYear >= 2012:
    genType = "Gen Z"
elif 2013 <= genYear and genYear >= 2025:
    genType = "Gen Alphai"
    
print("Hey ",name," you're a ",genType,"!")
