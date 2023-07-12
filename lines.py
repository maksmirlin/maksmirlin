def byte_size(string):
    return(len(string.encode('utf-8')))
   
byte_size('Я люблю Python!') 
>>> 11  

print(sys.getsizeof('Я люблю Python!'))
>>> 104 

byte_size('😀')
>>> 4
