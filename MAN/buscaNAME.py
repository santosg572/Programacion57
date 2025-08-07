import sys
#print "test1"
#print sys.argv[0]
file = sys.argv[1]
#print(len(sys.argv))

#def buscaNAME(file=''):

print(file)

filin = open(file, 'r')
datos = filin.readlines()

i = 0
while  i<10 :
    if 'NAME' in datos[i]:
      k = i
      i = 10
    else :
      i = i+1

print(datos[0])
print(datos[k+1])


