import numpy as np
import h5py

def load_dataset():
	train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")	# 从train.h5 中读取数据
	train_set_x_orig = np.array(train_dataset["train_set_x"][:])	# 读取train 数据
	train_set_y_orig = np.array(train_dataset["train_set_y"][:])	# 读取train 标签

	test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
	test_set_x_orig = np.array(test_dataset["test_set_x"][:])
	test_set_y_orig = np.array(test_dataset["test_set_y"][:])

	classes = np.array(test_dataset["list_classes"][:])	# 标签的种类数量

	train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
	test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

	return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


if __name__ == "__main__":
	train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")	# 从train.h5 中读取数据	
	train_set_x_orig = np.array(train_dataset["train_set_x"][:])	# 把train数据读取出来	（209，64，64，3）
	train_set_y_orig = np.array(train_dataset["train_set_y"][:])	# 读取train 标签  （209，）

	test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")	# test.h5py
	test_set_x_orig = np.array(test_dataset["test_set_x"][:])		# （50，64，64，3）
	test_set_y_orig = np.array(test_dataset["test_set_y"][:])		# （50，）

	classes = np.array(test_dataset["list_classes"][:])	# 标签的种类 2  相当于有 0 1 两类 [b'non-cat' b'cat']

	train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))	# 将y标签数据reshape 为（1，209）
	test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))	# 将y标签数据reshape 为（1，50）

	print(test_set_y_orig.shape)