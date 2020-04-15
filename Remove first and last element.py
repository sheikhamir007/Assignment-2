tuplex = "car","bike","truck"
print(tuplex)
listx = list (tuplex)
listx.remove("car")
listx.remove("truck")
tuplex = tuple (listx)
print(tuplex)
    
