# h5py
An HDF5 file is a container for two kinds of objects: **datasets**, which are array-like collections of data, and **groups**, which are folder-like containers that hold datasets and other groups. The most fundamental thing to remember when using h5py is:
                    **Groups work like dictionaries, and datasets work like NumPy arrays**
Suppose someone has sent you a HDF5 file, mytestfile.hdf5. 
The very first thing you’ll need to do is to open the file for reading:
```
>>> import h5py
>>> f = h5py.File('mytestfile.hdf5', 'r')
```
The File object is your starting point. What is stored in this file? Remember h5py.File acts like a Python dictionary, thus we can check the keys,
```
>>> list(f.keys())
['mydataset']
```
Based on our observation, there is one data set, mydataset in the file. Let us examine the data set as a Dataset object
```
>>> dset = f['mydataset']
```
The object we obtained isn’t an array, but an HDF5 dataset. Like NumPy arrays, datasets have both a shape and a data type:
```
>>> dset.shape
(100,)
>>> dset.dtype
dtype('int32')
```
They also support array-style slicing. This is how you read and write data from a dataset in the file:
```
>>> dset[...] = np.arange(100)
>>> dset[0]
0 /n
>>> dset[10]
10 /n
>>> dset[0:100:10]
array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
```

# scipy
SciPy (pronounced “Sigh Pie”) is open-source software for mathematics, science, and engineering. The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The SciPy library is built to work with NumPy arrays, and provides many user-friendly and efficient numerical routines such as routines for numerical integration and optimization. 

主要包括下面这些包:
```
scipy.integrate：数值积分例程和微分方程求解器
scipy.linalg：扩展了由numpy.linalg提供的线性代数例程和矩阵分解功能
scipy.optimize：函数优化器（最小化器）以及跟查找算法
scipy.signal：信号处理工具
scipy.sparse：稀疏矩阵和系数线性系统求解器
scipy.special：SPECFUN(这是一个实现了许多常用数学函数（如伽马函数）的Fortran库)的包装器
scipy.stats：标准连续和离散概率分布（如密度函数、采样器、连续分布函数等）、各种统计检验方法，以及更好的描述统计法
scipy.weave：利用内联C++代码加速数组计算的工具
```
详情可参考：https://blog.csdn.net/sunsetrain/article/details/79065962

# PIL
The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities.
PIL可以做很多和图像处理相关的事情:
```
**图像归档**(Image Archives)。PIL非常适合于图像归档以及图像的批处理任务。你可以使用PIL创建缩略图，转换图像格式，打印图像等等。
**图像展示**(Image Display)。PIL较新的版本支持包括Tk PhotoImage，BitmapImage还有Windows DIB等接口。PIL支持众多的GUI框架接口，可以用于图像展示。
**图像处理**(Image Processing)。PIL包括了基础的图像处理函数，包括对点的处理，使用众多的卷积核(convolution kernels)做过滤(filter),还有颜色空间的转换。PIL库同样支持图像的大小转换，图像旋转，以及任意的仿射变换。PIL还有一些直方图的方法，允许你展示图像的一些统计特性。这个可以用来实现图像的自动对比度增强，还有全局的统计分析等。
```
详情可参考： https://www.cnblogs.com/lyrichu/p/9124504.html


