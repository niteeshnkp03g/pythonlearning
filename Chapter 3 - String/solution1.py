# Write a python program to display a user entered name followed by Good Afternoon using input () function.

name = input(" Enter your Name : ")
str = " Good afternoon ! userinputname "
newstr = str.replace("userinputname", name)
print(newstr)