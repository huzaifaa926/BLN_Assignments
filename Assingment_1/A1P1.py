import time
import hashlib
from random import randint


def check_zeros(input_str):
	count=0
	for char in input_str:
		if char=='0':
			count+=1
	if count==3:
		return True
	return False

if __name__=="__main__":
	start_time = time.time()
	nounce = randint(0, 9999)
#	input_str = input("")
	input_str = "this is a block chain course"
	input_str += str(nounce)	
	result = hashlib.md5(input_str.encode())
	print(result.hexdigest())
	while(not check_zeros(str(result.hexdigest()))):
		nounce+=1
		input_str += str(nounce) + str('SomeRandom123')
		result = hashlib.md5(input_str.encode())
		print(result.hexdigest())
	end_time = time.time()
	start_time_verify = time.time()
	end_time_verify = 0
	result = hashlib.md5(input_str.encode())
	if check_zeros(str(result.hexdigest())):
		end_time_verify = time.time()
	print("Total Time Elapsed (compute): " + '{0:.16f}'.format(end_time - start_time))
	print("Total Time Elapsed (verify): " + '{0:.16f}'.format(end_time_verify - start_time_verify))

