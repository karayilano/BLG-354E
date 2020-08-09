# Oğuzhan Kürşat Karayılan
# 150140011

import numpy as np

def conv(x, h):
	if(x.size > h.size):
		for i in range(x.size - h.size):
			h = np.append(h, [0])
	elif(h.size > x.size):
		for i in range(h.size - x.size):
			x = np.append(x, [0])
	result = np.convolve(x, h)
	return result


x1 = np.array([0,1,2,3])
h1 = np.array([1,1,1,1])

x2 = np.array([0,1,2,3])
h2 = np.array([1])

x3 = np.array([0,1,2,3])
h3 = np.array([0,1,2,3])

x4 = np.array([1,0,1,2,3])
h4 = np.array([1,2])

print("a){}".format(conv(x1,h1)))
print("b){}".format(conv(x2,h2)))
print("c){}".format(conv(x3,h3)))
print("d){}".format(conv(x4,h4)))
