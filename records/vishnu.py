def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
print(mytripler(5))
mydoubler = myfunc(2)
