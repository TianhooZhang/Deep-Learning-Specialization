import numpy as np

x = np.array([1, 2, 3])
print(np.exp(x))
print(x+3)

def sigmoid(x):
	s = 1/(1+np.exp(-x))
	return s

print(sigmoid(x)) #说明了通过numpy 不需要循环 便可以处理矩阵

def sigmoid_derivative(x):
	# sigmoid的导数 ds = s * (1-s)  -- s = 1/(1+np.exp(-x))
	s = 1/(1+np.exp(-x))
	ds = s*(1-s)
	return ds

def image2vector(image):
	# 将RGB图像reshape成一个向量
	v = image.reshape((image.shape[0]*image.shape[1]*image.shape[2]),1)
	return v

def normalizeRows(x):
	# 对数据线性归一化，输出每行元素的平方和为1
	# x = [[0 3 4],[2 6 4]] normalizeRows(x) = [[0,3/5,4/5],[2/sqrt(65),6/sqrt(65),4/sqrt(65)]]
	x_norm = np.linalg.norm(x,axis=1,keepdims=True)
	x = x/x_norm
	return x

x = np.array([[0,3,4],[1,6,4]])
#同时输出字符串信息和列表信息时，对列表应该str操作
print("normalizeRows(x) = " + str(normalizeRows(x)))

def softmax(x):
	#softmax(x) = softmax([0,1],[2,3]) = [[e0/e0+e1 , e1/e0+e1],[e2/e2+e3, e3/e2+e3]]
	x_exp = np.exp(x)
	x_sum = np.sum(x_exp, axis=1, keepdims=True) #对每一行求和
	s = x_exp/x_sum
	return s

# 对向量化的优势做一个测试

# 非向量化
import time

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]
# a = np.random.rand(10000)
# b = np.random.rand(10000)

#	求对应元素和 x11^2 + x21^2 + ...
tic = time.process_time() # 返回当前进程执行CPU的时间总和，不包含睡眠时间．由于返回值的基准点是未定义的，所以只有连续调用的结果之间的差才是有效的
dot = 0
for i in range(len(x1)):
	dot += x1[i]*x2[i]
toc = time.process_time()
print("dot = " + str(dot) + "\n --- Computation time = " + str(1000*(toc-tic)) + "ms")

#	求一个x1长，x2宽的矩阵 相当于 x1.T * x2 
tic = time.process_time()
outer = np.zeros((len(x1),len(x2)))
for i in range(len(x1)):
	for j in range(len(x2)):
		outer[i,j] = x1[i]*x2[j]
toc = time.process_time()
print("outer = " + str(outer) + "\n --- Computation time = " + str(1000 * (toc-tic)) + "ms")

#	对应元素相乘放在一个矩阵里
tic = time.process_time()
mul = np.zeros(len(x1))
for i in range(len(x1)):
	mul[i] = x1[i] * x2[i]
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n --- Computation time = " + str(1000*(toc - tic)) + "ms" )

#	求每行的加权和
W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array
tic = time.process_time()
gdot = np.zeros(W.shape[0])
for i in range(W.shape[0]):
	for j in range(len(x1)):
		gdot[i] += W[i,j] * x1[j]
toc = time.process_time()
print("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

#`向量化 
# np.dot()是对应元素相乘
tic = time.process_time()
dot = np.dot(x1,x2)
toc = time.process_time()
print("dot = " + str(dot) + "\n --- Computation time = " + str(1000*(toc-tic)) + "ms") #对比可以发现 当数据量大时 向量化会节省时间

# np.outer(a,b)是建立一个a*b的矩阵W wij = ai*bj
tic = time.process_time()
outer = np.outer(x1, x2)
toc = time.process_time()
print("outer = " + str(outer) + "\n --- Computation time = " + str(1000 * (toc-tic)) + "ms")

# np.multiply(a,b) 矩阵元素为a,b对应元素相乘 对其求和就是np.dot
tic = time.process_time()
mul = np.multiply(x1,x2)
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n --- Computation time = " + str(1000*(toc - tic)) + "ms" )

tic = time.process_time()
dot = np.dot(W,x1)
toc = time.process_time()
print("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")


# L1：
def L1(yhat, y):
	loss = sum(abs(y-yhat))
	return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat,y)))

# L2：
def L2(yhat, y):
	loss = np.dot(y-yhat, y-yhat)
	return loss
	
print("L2 = " + str(L2(yhat,y)))






