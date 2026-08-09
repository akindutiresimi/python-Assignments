def products(*args):
	product = 1
	for value in args:
		product *= value
	return product
	

number = (8,7,9,4,5,6)
result = products(*number)
print(result)





#def product(value1, value2, value3):

#	result = value1 * value2 * value3
#	return result
	
	

#print(product(4,6,3))
