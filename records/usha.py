def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
mytripler = myfunc(3)
print(mydoubler(5))
print(mytripler(5))