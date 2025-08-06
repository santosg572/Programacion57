s1=''' <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
'''

file = open('dir.txt','r')
filo = open('dir.html', 'w')

datos = file.readlines()

filo.write(s1)

for ss in datos:
   if len(ss) > 1:
     ss = ss.replace('\n', '')
     ssn = '<p>  <a href="' + ss + '">example</a> </p> \n'
     filo.write(ssn)

s2='''
</body>
</html> 
'''

filo.write(s2)
filo.close()
