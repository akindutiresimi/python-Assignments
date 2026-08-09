#def square (number):
#	return number ** 2

#print (square(7))
#print(square(6))
#print(square(2))


#def maximum(number1, number2, number3):
#	max_number = number1
#	if number2 > max_number:
#		max_number = number2
#	if number3 > max_number:
#		max_number = number3
#	return max_number

#print(maximum(2, 4, 8))
#print(maximum(10, 100, 1000))
#print(maximum('yellow', 'red', 'blue'))
#print(maximum(13.5, -4, 0))


#import random

#for roll in range(10):

#	print(random.randrange(1,7), end=' ')

#for roll in range(10):

#	print(random.randrange(1,7), end=' ')





""" 6_000_000 die row """


#import random 

#frequency1 = 0
#frequency2 = 0
#frequency3 = 0
#frequency4 = 0
#frequency5 = 0
#frequency6 = 0

#for roll in range(6_000_000):
#	face = random.randrange(1,7)

#	if face == 1:
#		frequency1 += 1
#	elif face == 2:
#		frequency2 += 1
#	elif face == 3:
#		frequency3 += 1
#	elif face == 4:
#		frequency4 += 1
#	elif face == 5:
#		frequency5 += 1
#	elif face == 6:
#		frequency6 += 1

#print(f'face{"frequency":>13}')
#print(f'{1:>4}{frequency1:>13}')
#print(f'{2:>4}{frequency2:>13}')
#print(f'{3:>4}{frequency3:>13}')
#print(f'{4:>4}{frequency4:>13}')
#print(f'{5:>4}{frequency5:>13}')
#print(f'{6:>4}{frequency6:>13}')


#"""""my method but has a bug not runing proparlly"""
#import random
#T = 0
#H = 0
#for coin in range(20):
#	face = random.randrange(1,3)
#	if face == 0:
#		T += 1
#	elif face != 0:
#		H += 1
#print(T)
#print(H)



#
#import random

#for coin in range(20):
#	print('H' if random.randrange(2) == 0 else 'T', end=' ')




#"""use of arbitrary argument (operator *) to do calculation and return the result"""
#def average(*args):
#	return sum(args) / len(args)



#grade = (88, 75, 96, 55, 83)

#result = average(*grade)
#print(result)













