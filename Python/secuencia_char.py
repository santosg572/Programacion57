dd = '''Chapter V introduces the concept of fractal dimension. The fractal dimension of a set is a number that tells how 
densely 
the set occupies the metric space in which it lies. It is invariant under various stretchings and squeezings of the 
underlying space. This makes the fractal dimension meaningful as an experimental observable; it possesses a certain 
robustness and is independent of the measurement units. Various theoretical properties of the fractal dimension, 
including some explicit formulas, are developed. Then the reader is shown how to calculate the fractal dimension of 
real-world data, and an application to a turbulent jet exhaust is described. Lastly the Hausdorff-Besicovitch dimension 
is introduced. This is another number that can be associated with a set. It is more robust and less practical than the 
fractal dimension. Some mathematicians love it; most experimentalists hate it; and we are intrigued.
'''

print('tipo de objeto: '+ str(type(dd)))
print('longitud de dd :'+ str(len(dd)))

print("número de a's : "+ str(dd.count('a')))

# version 1

num=0
for ss in dd:
  if ss == 'a':
    num=num+1

print("número de a's V1 : "+ str(num))

# version 2

num=0
i = 0

for i in range(len(dd)):
  if dd[i] == 'a':
    num=num+1

print("número de a's V2 : "+ str(num))



