# h5py
An HDF5 file is a container for two kinds of objects: datasets, which are array-like collections of data, and groups, which are folder-like containers that hold datasets and other groups. The most fundamental thing to remember when using h5py is:
                    Groups work like dictionaries, and datasets work like NumPy arrays
Suppose someone has sent you a HDF5 file, mytestfile.hdf5. 
The very first thing you’ll need to do is to open the file for reading:

>>> import h5py
>>> f = h5py.File('mytestfile.hdf5', 'r')

The File object is your starting point. What is stored in this file? Remember h5py.File acts like a Python dictionary, thus we can check the keys,

>>> list(f.keys())
['mydataset']

Based on our observation, there is one data set, mydataset in the file. Let us examine the data set as a Dataset object

>>> dset = f['mydataset']

The object we obtained isn’t an array, but an HDF5 dataset. Like NumPy arrays, datasets have both a shape and a data type:

>>> dset.shape
(100,)
>>> dset.dtype
dtype('int32')

They also support array-style slicing. This is how you read and write data from a dataset in the file:

>>> dset[...] = np.arange(100) /n
>>> dset[0] /n
0 /n
>>> dset[10] /n
10 /n
>>> dset[0:100:10] /n
array([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) /n


