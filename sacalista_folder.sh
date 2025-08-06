#!/bin/bash

dir=$1
lista=$(ls $dir)

for ss in $lista
do
  echo $ss >> dir.txt
done


