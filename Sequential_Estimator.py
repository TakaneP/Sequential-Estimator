import sys
import numpy as np
import math


def Univariate_gaussian_data_generator(mean,variance):
	S = 0.0
	while S >= 1.0 or S == 0.0:
		U = np.random.random_sample() * 2 - 1
		V = np.random.random_sample() * 2 - 1
		S = U**2 + V**2

	multiply = math.sqrt( (-2.0) * math.log(S) / S )
	U = U * multiply
	V = V * multiply

	return mean + math.sqrt(variance) * U, mean +  math.sqrt(variance) * V

def Sequential_estimator(mean,variance):
	print("Data point source function: N(%.1f, %.1f)" %(mean,variance))
	m,_ = Univariate_gaussian_data_generator(mean,variance)
	s = 0
	m2 = 0
	n = 1
	while 1:
		n = n + 1
		new_data,_ = Univariate_gaussian_data_generator(mean,variance)
		print("Add data point: %.10f" %(new_data))
		m_pre = m
		m = m + (new_data-m)/n
		m2 = m2 + (new_data - m) * (new_data - m_pre)
		s = m2/(n-1)
		print("Mean = %.15f   Variance = %f" %(m,s))
		if abs(m - m_pre) < 1e-3:
			break
		

def main():
	argument = sys.argv[1:]
	if len(argument) != 2:
		print("You should input all the arguments")
		sys.exit(1)

	
	#Univariate gaussian data generator
	
	mean = float(argument[0])
	variance = float(argument[1])
	Sequential_estimator(mean,variance)
	

if __name__ == '__main__':
	main()
