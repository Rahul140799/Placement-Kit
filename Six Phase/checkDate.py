import datetime
dmy = input()
arr = dmy.split("/")
d = arr[0]
m = arr[1]
y = arr[2]
isValidDate = True
try:
    datetime.datetime(int(y),int(m),int(d))
except:
    isValidDate = False

if isValidDate:
    print("Valid")
else:
    print("Invalid")
