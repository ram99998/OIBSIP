# RK Random password generator using python

#IMPORT RANDOM LIBRARY
import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special="!@#$%^&*(){}_+="
all=lower+upper+numbers+special
length=8
password="".join(random.sample(all,length))
print(password)