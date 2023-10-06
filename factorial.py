
def factorial(num):
	answer = 1
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		while num > 1:
			answer *= num
			num -=1
	print(answer)
	return answer

