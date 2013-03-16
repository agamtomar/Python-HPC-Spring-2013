# # Lists, Tuples and Numpy 
# 
# Thomas Hauser (thomas.hauser@colorado.edu)
# 

# ## Working with a CSV data file
# ### IPthon can work as a better shell

# In[1]:
files = !ls *.csv

# In[2]:
print files

# Out[2]:
#     ['data_file.csv', 'timings.csv']
# 
# Our first list

# In[3]:
!cat {files[1]}

# Out[3]:
#     numProcs numJobs time
#     2 10 30.0811908245
#     4 30 30.0843958855
#     8 70 30.0985591412
#     16 150 30.1254658699
#     32 310 30.1745619774
#     64 630 30.2706680298
#     128 1270 30.4968237877
#     256 2550 31.0896470547
#     512 5110 32.0129721165
#     1024 10230 32.6434509754
#     2048 20470 32.6491119862
#     4096 40950 34.5213968754
#     8192 81910 44.4184248447
# 
# ### Reading in the file
# - We will create three empty lists, one for each column
# - The lists will contain strings
# - we then store each of the list data in a dictionary with the column header as the key

# In[4]:
procs = []
jobs = []
times = []

# In[5]:
print procs

# Out[5]:
#     []
#     
# 
# ### Open file and read data
# Try to open the file. If it does not exist, print the IOError we catch.

# In[6]:
try:
    infile = open(files[1],'r')
except IOError as e:
    print e

# In[7]:
for line in infile:
    tmp = line.split()
    if len(tmp) == 3:
        procs.append(tmp[0])
        jobs.append(tmp[1])
        times.append(tmp[2])

# In[8]:
print procs

# Out[8]:
#     ['numProcs', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192']
# 
# Lists can contain a mix of element types

# ## Storing the data in a dictionary
# - Create an empty dictionary
# - Extract the data and the key out of our 3 lists
# - Convert the data to integers and floating point numbers
# - Add some meta data with the key `description`

# In[9]:
jobData = {}

# In[10]:
print jobData

# Out[10]:
#     {}
# 
# In[189]:
jobData[procs[0]] = map(int, procs[1:])
jobData[jobs[0]] = map(int, jobs[1:])
jobData[times[0]] = map(float, times[1:])
jobData['description'] = "Job data per process"

# - All lists and arrays are 0 based in python
# - Slices give your portions of a list or array

# In[190]:
print jobData

# Out[190]:
#     {'description': 'Job data per process', 'numProcs': [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192], 'time': [30.0811908245, 30.0843958855, 30.0985591412, 30.1254658699, 30.1745619774, 30.2706680298, 30.4968237877, 31.0896470547, 32.0129721165, 32.6434509754, 32.6491119862, 34.5213968754, 44.4184248447], 'numJobs': [10, 30, 70, 150, 310, 630, 1270, 2550, 5110, 10230, 20470, 40950, 81910]}
# 
# In[13]:
jobData['numProcs']

# Out[13]:
#     [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]


# ## Tuples
# - Similar to lists but you can't change the elements of a tuple

# In[14]:
myList = jobData['numProcs']
myTuple = tuple(myList)
myList[2] = 'Not valid'
print myList
print jobData['numProcs']

# Out[14]:
#     [2, 4, 'Not valid', 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
#     [2, 4, 'Not valid', 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
# 
# In[15]:
print myTuple

# Out[15]:
#     (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192)
# 
# In[16]:
myTuple[2] = 'not valid'

# Out[16]:
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-16-55a85696325d> in <module>()
    ----> 1 myTuple[2] = 'not valid'
    
    TypeError: 'tuple' object does not support item assignment

# # Numpy - arrays in Python
# 
# The `numpy` module ifor fast numerical computations in Python. It provides array, matrices where operations on whole matrices are implemented in C and Fortran and are therefor very fast. Import the `numpy` module.
# 

# In[191]:
import numpy as nb

# In the `numpy` package the terminology used for vectors, matrices and higher-dimensional data sets is *array*. 
# 
# 

# ## Creating `numpy` arrays
# 
# Arrays can be created from
# 
# * lists or tuples
# * using functions 
# * reading data from files
# 
# ### From lists
# 
# Use the `numpy.array` function to create an array from lists are tuples
# 

# In[195]:
t = array(jobData['time'])
t

# Out[195]:
#     array([ 30.08119082,  30.08439589,  30.09855914,  30.12546587,
#             30.17456198,  30.27066803,  30.49682379,  31.08964705,
#             32.01297212,  32.64345098,  32.64911199,  34.52139688,  44.41842484])


# In[196]:
# a 3x2 array
M = array([[1, 2, 3], [4, 5, 6]])
M

# Out[196]:
#     array([[1, 2, 3],
#            [4, 5, 6]])


# Arrays are of type `ndarray` that the `numpy` module provides.

# In[19]:
type(v), type(M)

# Out[19]:
#     (numpy.ndarray, numpy.ndarray)


# Arrays have shapes. This is a property of an array

# In[197]:
t.shape

# Out[197]:
#     (13,)


# In[198]:
M.shape

# Out[198]:
#     (2, 3)


# The number of elements in the array is available through the `ndarray.size` property:

# In[199]:
M.size

# Out[199]:
#     6


# Equivalently, we could use the function `numpy.shape` and `numpy.size`

# In[200]:
nb.shape(M)

# Out[200]:
#     (2, 3)


# In[201]:
nb.size(M)

# Out[201]:
#     6


# ## Why user arrays?
# 
# 
# * List are general, can hold different data types
# * Numpy arrays are **statically typed** and **homogeneous**. 
# * Numpy arrays are memory efficient.
# * Fast implementation of mathematical functions such as multiplication and addition of `numpy` arrays because of static type
# 
# The `dtype` (data type) property 

# In[202]:
M.dtype

# Out[202]:
#     dtype('int64')


# We get an error if we try to assign a value of the wrong type to an element in a numpy array:

# In[26]:
M[0,0] = "hello"

# Out[26]:
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-26-a09d72434238> in <module>()
    ----> 1 M[0,0] = "hello"
    
    ValueError: invalid literal for long() with base 10: 'hello'

# ## Data types for array elements
# 
# If we want, we can explicitly define the type of the array data when we create it, using the `dtype` keyword argument: 

# In[204]:
Mc = nb.array([[1, 2], [3, 4]], dtype=complex)

Mc

# Out[204]:
#     array([[ 1.+0.j,  2.+0.j],
#            [ 3.+0.j,  4.+0.j]])


# Data types for arrays
# 
# * `int` and also `int16`
# * `float` also `float128
# * `complex` also `complex128`
# * `bool`
# * `object`, etc.
# 

# ### Using array-generating functions
# 
# For larger arrays it is inpractical to initialize the data manually, using explicit pythons lists. Instead we can use one of the many functions in `numpy` that generates arrays of different forms. Some of the more common are:

# #### arange

# In[205]:
# create a range

x = nb.arange(0, 10, 1) # arguments: start, stop, step

x

# Out[205]:
#     array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[206]:
x = nb.arange(-1, 1, 0.1)

x

# Out[206]:
#     array([ -1.00000000e+00,  -9.00000000e-01,  -8.00000000e-01,
#             -7.00000000e-01,  -6.00000000e-01,  -5.00000000e-01,
#             -4.00000000e-01,  -3.00000000e-01,  -2.00000000e-01,
#             -1.00000000e-01,  -2.22044605e-16,   1.00000000e-01,
#              2.00000000e-01,   3.00000000e-01,   4.00000000e-01,
#              5.00000000e-01,   6.00000000e-01,   7.00000000e-01,
#              8.00000000e-01,   9.00000000e-01])


# #### linspace and logspace

# In[207]:
# using linspace, both end points ARE included
nb.linspace(0, 10, 25)

# Out[207]:
#     array([  0.        ,   0.41666667,   0.83333333,   1.25      ,
#              1.66666667,   2.08333333,   2.5       ,   2.91666667,
#              3.33333333,   3.75      ,   4.16666667,   4.58333333,
#              5.        ,   5.41666667,   5.83333333,   6.25      ,
#              6.66666667,   7.08333333,   7.5       ,   7.91666667,
#              8.33333333,   8.75      ,   9.16666667,   9.58333333,  10.        ])


# In[208]:
nb.logspace(0, 10, 10, base=e)

# Out[208]:
#     array([  1.00000000e+00,   3.03773178e+00,   9.22781435e+00,
#              2.80316249e+01,   8.51525577e+01,   2.58670631e+02,
#              7.85771994e+02,   2.38696456e+03,   7.25095809e+03,
#              2.20264658e+04])


# #### random data

# In[211]:
from numpy import random

# In[212]:
# uniform random numbers ini [0,1]
random.rand(5,5)

# Out[212]:
#     array([[ 0.50030474,  0.23161661,  0.75112596,  0.43577698,  0.23254737],
#            [ 0.55005928,  0.12946658,  0.47300875,  0.75031758,  0.87944104],
#            [ 0.20460273,  0.85787102,  0.62709432,  0.19337771,  0.86560913],
#            [ 0.9438643 ,  0.77329475,  0.43295579,  0.50254874,  0.631721  ],
#            [ 0.96223957,  0.07674404,  0.76319945,  0.49379107,  0.79215773]])


# In[37]:
# standard normal distributed random numbers
random.randn(5,5)

# Out[37]:
#     array([[-1.7481186 ,  0.23314059, -0.79571273,  0.98731918, -1.70567045],
#            [ 0.01466557, -0.77158617,  0.61049673, -2.0021754 , -0.89958161],
#            [ 0.87349961, -1.59764627,  0.17355193, -2.05903027, -0.90854175],
#            [ 1.01447915, -0.38388898, -1.6641756 ,  0.19661176,  0.21267152],
#            [ 0.16952214, -0.43690138, -1.14330842,  0.19217729,  1.71121092]])


# #### zeros and ones

# In[40]:
zeros((3,3))

# Out[40]:
#     array([[ 0.,  0.,  0.],
#            [ 0.,  0.,  0.],
#            [ 0.,  0.,  0.]])


# In[41]:
ones((3,3))

# Out[41]:
#     array([[ 1.,  1.,  1.],
#            [ 1.,  1.,  1.],
#            [ 1.,  1.,  1.]])


# ## File I/O
# 
# 
# ### Comma-separated values (CSV)
# 
# Reading our data with `numpy`

# In[213]:
np, nj, rt = numpy.genfromtxt(files[1], delimiter=' ', skip_header=1,unpack=1) 

# In[214]:
np

# Out[214]:
#     array([  2.00000000e+00,   4.00000000e+00,   8.00000000e+00,
#              1.60000000e+01,   3.20000000e+01,   6.40000000e+01,
#              1.28000000e+02,   2.56000000e+02,   5.12000000e+02,
#              1.02400000e+03,   2.04800000e+03,   4.09600000e+03,
#              8.19200000e+03])


# Using the `numpy.savetxt` we can store a Numpy array to a file in CSV format:

# In[215]:
rt

# Out[215]:
#     array([ 30.08119082,  30.08439589,  30.09855914,  30.12546587,
#             30.17456198,  30.27066803,  30.49682379,  31.08964705,
#             32.01297212,  32.64345098,  32.64911199,  34.52139688,  44.41842484])


# In[216]:
nb.savetxt("testTimes.csv", rt)

# In[217]:
!cat testTimes.csv

# Out[217]:
#     3.008119082449999837e+01
#     3.008439588550000110e+01
#     3.009855914119999909e+01
#     3.012546586990000108e+01
#     3.017456197739999979e+01
#     3.027066802979999949e+01
#     3.049682378769999858e+01
#     3.108964705469999856e+01
#     3.201297211650000207e+01
#     3.264345097540000040e+01
#     3.264911198619999766e+01
#     3.452139687540000068e+01
#     4.441842484469999874e+01
# 
# In[218]:
nb.savetxt("testTimes.csv", rt, fmt='%.5f') # fmt specifies the format

!cat testTimes.csv

# Out[218]:
#     30.08119
#     30.08440
#     30.09856
#     30.12547
#     30.17456
#     30.27067
#     30.49682
#     31.08965
#     32.01297
#     32.64345
#     32.64911
#     34.52140
#     44.41842
# 
# ## Manipulating arrays

# ### Indexing
# 
# Simlar to lists:

# In[219]:
# v is a vector, and has only one dimension, taking one index
rt[0]

# Out[219]:
#     30.081190824499998


# In[220]:
# M is a matrix, or a 2 dimensional array, taking two indices 
M[1,1]

# Out[220]:
#     5


# If we omit an index of a multidimensional array it returns the whole row (or, in general, a N-1 dimensional array) 

# In[221]:
M

# Out[221]:
#     array([[1, 2, 3],
#            [4, 5, 6]])


# In[222]:
M[1]

# Out[222]:
#     array([4, 5, 6])


# The same thing can be achieved with using `:` instead of an index: 

# In[223]:
M[1,:] # row 1

# Out[223]:
#     array([4, 5, 6])


# In[224]:
M[:,1] # column 1

# Out[224]:
#     array([2, 5])


# We can assign new values to elements in an array using indexing:

# In[225]:
M[0,0] = -1

# In[226]:
M

# Out[226]:
#     array([[-1,  2,  3],
#            [ 4,  5,  6]])


# In[227]:
# also works for rows and columns
M[1,:] = 0
M[:,2] = -1

# In[228]:
M

# Out[228]:
#     array([[-1,  2, -1],
#            [ 0,  0, -1]])


# ## Index slicing
# 
# Index slicing is the technical name for the syntax `M[lower:upper:step]` to extract part of an array:

# In[229]:
rt[1:3]

# Out[229]:
#     array([ 30.08439589,  30.09855914])


# Array slices are *mutable*: if they are assigned a new value the original array from which the slice was extracted is modified:

# In[230]:
rt[1:3] = [-2,-3]
rt

# Out[230]:
#     array([ 30.08119082,  -2.        ,  -3.        ,  30.12546587,
#             30.17456198,  30.27066803,  30.49682379,  31.08964705,
#             32.01297212,  32.64345098,  32.64911199,  34.52139688,  44.41842484])


# We can omit any of the three parameters in `M[lower:upper:step]`:

# In[231]:
rt[::] # lower, upper, step all take the default values

# Out[231]:
#     array([ 30.08119082,  -2.        ,  -3.        ,  30.12546587,
#             30.17456198,  30.27066803,  30.49682379,  31.08964705,
#             32.01297212,  32.64345098,  32.64911199,  34.52139688,  44.41842484])


# In[232]:
rt[::2] # step is 2, lower and upper defaults to the beginning and end of the array

# Out[232]:
#     array([ 30.08119082,  -3.        ,  30.17456198,  30.49682379,
#             32.01297212,  32.64911199,  44.41842484])


# In[233]:
rt[:3] # first three elements

# Out[233]:
#     array([ 30.08119082,  -2.        ,  -3.        ])


# In[234]:
rt[3:] # elements from index 3

# Out[234]:
#     array([ 30.12546587,  30.17456198,  30.27066803,  30.49682379,
#             31.08964705,  32.01297212,  32.64345098,  32.64911199,
#             34.52139688,  44.41842484])


# Negative indices counts from the end of the array (positive index from the begining):

# In[235]:
rt[-1] # the last element in the array

# Out[235]:
#     44.418424844699999


# In[236]:
rt[-3:] # the last three elements

# Out[236]:
#     array([ 32.64911199,  34.52139688,  44.41842484])


# Index slicing works exactly the same way for multidimensional arrays:

# ### Fancy indexing
# 
# Using an array or list in-place of an index: 

# In[237]:
id = [0, 1, 5, -1]
rt[id]

# Out[237]:
#     array([ 30.08119082,  -2.        ,  30.27066803,  44.41842484])


# We can also index masks: If the index mask is an Numpy array of with data type `bool`, then an element is selected (True) or not (False) depending on the value of the index mask at the position each element: 

# In[238]:
B = array([n for n in range(5)])
B

# Out[238]:
#     array([0, 1, 2, 3, 4])


# In[239]:
row_mask = array([True, False, True, False, False])
B[row_mask]

# Out[239]:
#     array([0, 2])


# This feature is very useful to conditionally select elements from an array, using for example comparison operators:

# In[81]:
x = arange(0, 10, 0.5)
x

# Out[81]:
#     array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,
#             5.5,  6. ,  6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5])


# In[82]:
mask = (5 < x) * (x < 7.5)

mask

# Out[82]:
#     array([False, False, False, False, False, False, False, False, False,
#            False, False,  True,  True,  True,  True, False, False, False,
#            False, False], dtype=bool)


# In[83]:
x[mask]

# Out[83]:
#     array([ 5.5,  6. ,  6.5,  7. ])


# ## Linear algebra
# 
# Express operations in terms of arrays and matrics to get optimal speed (compiled functions).
# 

# ### Scalar-array operations
# 
# We can use the usual arithmetic operators to multiply, add, subtract, and divide arrays with scalar numbers.

# In[93]:
v1 = arange(0, 5)

# In[94]:
v1 * 2

# Out[94]:
#     array([0, 2, 4, 6, 8])


# In[241]:
v1 + 2

# Out[241]:
#     array([2, 3, 4, 5, 6])


# ### Element-wise array-array operations
# 
# When we add, subtract, multiply and divide arrays with each other, the default behaviour is **element-wise** operations:

# In[244]:
v1 * v1

# Out[244]:
#     array([ 0,  1,  4,  9, 16])


# ### Matrix algebra
# 

# In[245]:
dot(v1, v1)

# Out[245]:
#     30


# ### Data computations
# 
# Often it is useful to store datasets in Numpy arrays. Numpy provides a number of functions to calculate statistics of datasets in arrays. 
# 

# In[248]:
shape(rt)
rt

# Out[248]:
#     array([ 30.08119082,  -2.        ,  -3.        ,  30.12546587,
#             30.17456198,  30.27066803,  30.49682379,  31.08964705,
#             32.01297212,  32.64345098,  32.64911199,  34.52139688,  44.41842484])


# #### mean

# In[247]:
mean(rt[:])

# Out[247]:
#     27.191054949400002


# #### min and max

# In[249]:
rt.min()

# Out[249]:
#     -3.0


# In[250]:
rt.max()

# Out[250]:
#     44.418424844699999


# Many other functions and methods in the `array` and `matrix` classes accept the same (optional) `axis` keyword argument.

# ## Copy and "deep copy"
# 
# To achieve high performance, assignments in Python usually do not copy the underlaying objects. This is important for example when objects are passed between functions, to avoid an excessive amount of memory copying when it is not necessary (techincal term: pass by reference). 

# In[164]:
A = array([[1, 2], [3, 4]])

A

# Out[164]:
#     array([[1, 2],
#            [3, 4]])


# In[165]:
# now B is referring to the same array data as A 
B = A 

# In[166]:
# changing B affects A
B[0,0] = 10

B

# Out[166]:
#     array([[10,  2],
#            [ 3,  4]])


# In[167]:
A

# Out[167]:
#     array([[10,  2],
#            [ 3,  4]])


# If we want to avoid this behavior, so that when we get a new completely independent object `B` copied from `A`, then we need to do a so-called "deep copy" using the function `copy`:

# In[168]:
B = copy(A)

# In[169]:
# now, if we modify B, A is not affected
B[0,0] = -5

B

# Out[169]:
#     array([[-5,  2],
#            [ 3,  4]])


# In[170]:
A

# Out[170]:
#     array([[10,  2],
#            [ 3,  4]])


# ## Further reading
# 
# * http://numpy.scipy.org
# * http://scipy.org/Tentative_NumPy_Tutorial
# * http://scipy.org/NumPy_for_Matlab_Users - A Numpy guide for MATLAB users.
