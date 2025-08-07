#!/bin/bash

lista1="wc ls pwd"
lista2="rsync sed awk grep tr"

for ss in $lista2
do
  echo "========================== "$ss" ========================== " 
  ./man_comando.sh $ss
done

