#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.
var_int = 9856
#Create a variable "sum_even" and assign it 0.
sum_even = 0
#Find the sum of the even digits in the variable "var_int".
a = var_int%10
var_int = var_int//10

b = var_int%10
var_int = var_int//10

c = var_int%10
var_int = var_int//10

d = var_int%10
var_int = var_int//10

print((a+c))
