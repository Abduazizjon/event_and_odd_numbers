#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 5861
#Create a variable "sum_odd" and assign it 0.
sum_odd = 0
#Find the sum of the odd digits in the variable "var_int".
a = var_int%10
var_int = var_int//10

b = var_int%10
var_int = var_int//10

c = var_int%10
var_int = var_int//10

d = var_int%10
var_int = var_int//10

print((d+a))