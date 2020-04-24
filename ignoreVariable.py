a = ('jai','1988','12','10','Aligarh','Up','India')

# name = a[0]
# year = a[1]
# city = a[4]
# state = a[5]
# country = a[6]

#above commented line we can write this way, it is for only show in good way
name,year,*_,city,state,country = a # we can use any name at place of _ like(name,year,*ignoreVariables,city,state,country = a)

b = name,year,*_,city,state,country
print(b)
print(_) #it gives the list of variables that are ignored 

