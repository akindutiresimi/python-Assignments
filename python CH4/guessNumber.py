def product(*value):
	
	result = math.prod(value)
	return result


number = (4,6,3,6)
result = product(*number)
print(result)