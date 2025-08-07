#!/bin/bash

dir=$(ls -1 datos/)

for ss in $dir
do
  echo $ss
  python buscaNAME.py datos/$ss
done


