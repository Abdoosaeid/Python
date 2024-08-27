# Numpy (Numerical python)


```python
import numpy as np
```


```python
x = np.random.random(10000000)
```


```python
%timeit sum(x) / len(x)
```

    610 ms ± 6.53 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    


```python
%timeit np.mean(x)
```

    9.38 ms ± 71.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    

# Array Creation 

## create Arrays from lists


```python
lst = [1,2,3,4]
lst
```




    [1, 2, 3, 4]



### one Dimensional Array 


```python
x = np.array(lst) 
x
```




    array([1, 2, 3, 4])




```python
z = np.array(['A','B',1])
z
```




    array(['A', 'B', '1'], dtype='<U11')




```python
print(type(z))
```

    <class 'numpy.ndarray'>
    


```python
x.dtype
```




    dtype('int32')




```python
x.shape
```




    (4,)




```python
x = np.array([0,np.pi / 2,np.pi])
x
```




    array([0.        , 1.57079633, 3.14159265])




```python
y = np.sin(x)
y
```




    array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])



### 2 Dimentional Array


```python
y = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y
```




    array([[ 1,  2,  3],
           [ 4,  5,  6],
           [ 7,  8,  9],
           [10, 11, 12]])




```python
y.shape
```




    (4, 3)




```python
y.size
```




    12




```python
x = np.array([1,2.5,4])
print(x.dtype)
```

    float64
    

### Converting Elements Data Types


```python
x = np.array([1.5,2.2,3.7])
print(x)
print(x.dtype)
```

    [1.5 2.2 3.7]
    float64
    


```python
x = np.array([1.5,2.2,3.7],dtype = np.int64)
print(x)
```

    [1 2 3]
    

### saving Array 


```python
x = np.array([1,2,3,4,5])
np.save('my_array',x)
```


```python
y = np.load('my_array.npy')
print(y)
```

    [1 2 3 4 5]
    

### Array Ranks 

- Rank(0)


```python
a0 = 5 
print(a0)
```

    5
    

- Rank(1)


```python
a1 = np.array([1,2,3])
print(a1)
```

    [1 2 3]
    

- Rank(2)


```python
 a2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a2)
```

    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    


```python
a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
a3
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6],
            [ 7,  8,  9]],
    
           [[10, 11, 12],
            [13, 14, 15],
            [16, 17, 18]]])




```python
type(a0),type(a1),type(a2),type(a3)
```




    (int, numpy.ndarray, numpy.ndarray, numpy.ndarray)




```python
a1.shape, a2.shape, a3.shape
```




    ((3,), (4, 3), (2, 3, 3))




```python
a1.ndim, a2.ndim, a3.ndim
```




    (1, 2, 3)



## other Ways to Create Arrays 


```python
x = np.zeros((3,4))
print(x)
```

    [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]]
    


```python
x.dtype
```




    dtype('float64')




```python
x = np.zeros((3,4),dtype = int)
print(x)
```

    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    


```python
x.dtype
```




    dtype('int32')




```python
x = np.ones((4,5))
print(x)
```

    [[1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]
     [1. 1. 1. 1. 1.]]
    


```python
x = np.full((4,3),5)
print(x)
```

    [[5 5 5]
     [5 5 5]
     [5 5 5]
     [5 5 5]]
    

### Identity Matrix 
- very important matrix in linear Algebra 


```python
x = np.eye(5)
print(x)
```

    [[1. 0. 0. 0. 0.]
     [0. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]]
    

- Diagonal Matrix Always square Matrix 


```python
x = np.diag([10,20,30,40])
print(x)
```

    [[10  0  0  0]
     [ 0 20  0  0]
     [ 0  0 30  0]
     [ 0  0  0 40]]
    


```python
x = np.eye(4,dtype = int)
print(x * 10)
```

    [[10  0  0  0]
     [ 0 10  0  0]
     [ 0  0 10  0]
     [ 0  0  0 10]]
    

### number arange 


```python
x = np.arange(10)
print(x)
# Start (0) , stop (10) , Integer Numbers , and 10 is Exclusive 
```

    [0 1 2 3 4 5 6 7 8 9]
    


```python
x = np.arange(4,10)
print(x)
# start (4),stop (10) ,Interger Number , and 10 is Exclusive 
```

    [4 5 6 7 8 9]
    


```python
x = np.arange(1,14,3)
print(x)
# start (4),stop (10) , steps (3) Interger Number , and 10 is Exclusive 
```

    [ 1  4  7 10 13]
    


```python
x = np.linspace(0,25,10)
print(x)
# start (0) ,stop(25),Length(10), Float Numbers,and 25 is inclusive 
```

    [ 0.          2.77777778  5.55555556  8.33333333 11.11111111 13.88888889
     16.66666667 19.44444444 22.22222222 25.        ]
    


```python
x = np.linspace(0,25,num = 10)
print(x)
```

    [ 0.          2.77777778  5.55555556  8.33333333 11.11111111 13.88888889
     16.66666667 19.44444444 22.22222222 25.        ]
    


```python
x = np.linspace(0,25,10,endpoint = False)
print(x)
# start (0) ,stop(25),Length(10), Float Numbers,and 25 is Exclusive 
```

    [ 0.   2.5  5.   7.5 10.  12.5 15.  17.5 20.  22.5]
    


```python
x = np.linspace(-2,2,9)
print(x)
```

    [-2.  -1.5 -1.  -0.5  0.   0.5  1.   1.5  2. ]
    

### Generating random floats from 0 to 1 a uniform Distribution 


```python
x = np.random.rand(3,3)
print(x)
```

    [[0.25657922 0.55967185 0.75891316]
     [0.13364061 0.90177499 0.82465467]
     [0.46599731 0.61004847 0.64807765]]
    

### Generating random floats from 0 to 5 a uniform Distribution 


```python
x = np.random.uniform(0,5,size=(3,3))
print(x)
```

    [[1.56529026 3.32814272 0.80764981]
     [1.56619708 3.80263321 4.23799143]
     [0.86481804 2.21808112 2.01183647]]
    

### Generating random floats from 0 to 1 a random Distribution 


```python
x = np.random.random((3,3))
print(x)
```

    [[0.70678249 0.75633747 0.39561679]
     [0.45532085 0.45195809 0.65723397]
     [0.67576744 0.30040822 0.94009213]]
    

### Generating random integers wihin a range 


```python
x = np.random.randint(4,15,10)
print(x)
# Generating random Integer Start (4) is inclusive , stop (15) is Exclusive , size is (10) numbers 
```

    [ 6  6  9 12 14 10  7 14 12 13]
    


```python
x = np.random.randint(4,15,(3,2))
print(x)
# Generating random Integer Start (4) is inclusive , stop (15) is Exclusive , shape (3,2)
```

    [[ 5 13]
     [14 10]
     [14 12]]
    

### Normal Distribution 


```python
x = np.random.normal(4,15,size=(5,5))
print(x)
# mean(4),standard deviation(15) 
```

    [[  9.47862156  14.25775103  -4.23625637  14.77201356  -8.93220081]
     [ -7.9080588   15.78943572   5.58602907 -21.28246132  10.522889  ]
     [ 10.1136549   12.55241854 -41.9211664   22.74358012 -11.57741791]
     [ 10.49935029   0.81876911   7.49364073 -15.25511388  -0.67485931]
     [-12.96834333 -26.03800724  15.19153283  -4.31684322  28.28643117]]
    

### Standard Normal Distribution 


```python
x = np.random.randn(5,5)
print(x)
```

    [[ 1.0891699   0.52224447 -1.63708381 -1.45662178  1.11800853]
     [ 0.16783882 -1.21117171  0.7936199   0.01096926  0.86065437]
     [-1.40027053  0.68602181 -1.84242959 -0.56904954 -0.42625208]
     [ 0.23907712  0.91721753  0.34981468 -0.84657583  1.86736971]
     [ 0.66511409 -0.25240528  0.39184069 -0.34497922  0.31812262]]
    

### Randomly Selecting Values from an array 


```python
arr_1 = np.array(['A','B','C','D','E'])
random_choices = np.random.choice(arr_1,size = 3)
random_choices
```




    array(['C', 'B', 'A'], dtype='<U1')



### Creating a Random Permutation of an array 


```python
arr_1 = np.arange(5)
print(arr_1)
random_permutation = np.random.permutation(arr_1)
random_permutation
```

    [0 1 2 3 4]
    




    array([4, 1, 0, 3, 2])



# Array Manipulation 


```python
x = np.linspace(0,25,20,endpoint=False)
print(x)
```

    [ 0.    1.25  2.5   3.75  5.    6.25  7.5   8.75 10.   11.25 12.5  13.75
     15.   16.25 17.5  18.75 20.   21.25 22.5  23.75]
    


```python
x = np.reshape(x,(4,5))
print(x)
```

    [[ 0.    1.25  2.5   3.75  5.  ]
     [ 6.25  7.5   8.75 10.   11.25]
     [12.5  13.75 15.   16.25 17.5 ]
     [18.75 20.   21.25 22.5  23.75]]
    


```python
x = np.reshape(x,(10,2))
print(x)
```

    [[ 0.    1.25]
     [ 2.5   3.75]
     [ 5.    6.25]
     [ 7.5   8.75]
     [10.   11.25]
     [12.5  13.75]
     [15.   16.25]
     [17.5  18.75]
     [20.   21.25]
     [22.5  23.75]]
    


```python
y = np.arange(20).reshape(10,2)
print(y)
```

    [[ 0  1]
     [ 2  3]
     [ 4  5]
     [ 6  7]
     [ 8  9]
     [10 11]
     [12 13]
     [14 15]
     [16 17]
     [18 19]]
    


```python
x = np.linspace(0,50,10,endpoint=False).reshape(5,2)
print(x)
```

    [[ 0.  5.]
     [10. 15.]
     [20. 25.]
     [30. 35.]
     [40. 45.]]
    


```python
x = np.arange(1,10).reshape(3,3)
print(x)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    

## Transposed 


```python
Transposed_x = x.T
print(Transposed_x)
```

    [[1 4 7]
     [2 5 8]
     [3 6 9]]
    

## Delete 


```python
x = np.array([1,2,3,4,5])
print(x)
```

    [1 2 3 4 5]
    


```python
x = np.delete(x,[0,4])
print(x)
```

    [2 3 4]
    


```python
y = np.arange(1,10).reshape(3,3)
print(y)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    

- axis = 0 --> row  &&  axis = 1 --> column


```python
w = np.delete(y,0,axis=0)
print(w)
```

    [[4 5 6]
     [7 8 9]]
    


```python
w = np.delete(y,[0,2],axis=1)
print(w)
```

    [[2]
     [5]
     [8]]
    

## Append in Numpy 


```python
x = np.array([1,2,3,4,5])
print(x)
```

    [1 2 3 4 5]
    


```python
x = np.append(x,6)
print(x)
```

    [1 2 3 4 5 6]
    


```python
y = np.arange(1,10).reshape(3,3)
print(y)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
w = np.append(y,[[10,11,12]],axis=0)
print(w)
```

    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    


```python
v = np.append(y,[[10],[11],[12]],axis=1)
print(v)
```

    [[ 1  2  3 10]
     [ 4  5  6 11]
     [ 7  8  9 12]]
    


```python
x = np.array([1,2,5,6,7])
print(x)
```

    [1 2 5 6 7]
    


```python
x = np.insert(x,2,[3,4])
print(x)
```

    [1 2 3 4 5 6 7]
    


```python
print(y)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    


```python
w = np.insert(y,1,[4,5,6],axis=0)
print(w)
```

    [[1 2 3]
     [4 5 6]
     [4 5 6]
     [7 8 9]]
    


```python
w = np.insert(y,1,5,axis=1)
print(w)
```

    [[1 5 2 3]
     [4 5 5 6]
     [7 5 8 9]]
    


```python
x = np.array([1,2])
y = np.array([[3,4],[5,6]])
print('x:',x)
print('y:',y)
```

    x: [1 2]
    y: [[3 4]
     [5 6]]
    


```python
z = np.vstack((x,y))
print(z)
```

    [[1 2]
     [3 4]
     [5 6]]
    


```python
x = x.reshape(2,1)
print(x)
```

    [[1]
     [2]]
    


```python
w = np.hstack((x,y))
print(w)
```

    [[1 3 4]
     [2 5 6]]
    


```python
y = np.arange(1,10).reshape(3,3)
print(y)
splite_arrays = np.split(y,3) # split into 3 equal parts 
print(splite_arrays)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]
    

## checking for NaN (Not a NUmber) values 


```python
arr_1 = np.array([1,2,np.nan,4,5])
print("arr_1: ",arr_1)
nan_arr = np.isnan(arr_1)
print("nan arr: ",nan_arr)
```

    arr_1:  [ 1.  2. nan  4.  5.]
    nan arr:  [False False  True False False]
    

## checking for positive or negative infinity 


```python
arr_1 = np.array([1,2,np.inf,4,-np.inf])
print("arr_1: ",arr_1)
inf_arr = np.isinf(arr_1)
print("inf arr: ",inf_arr)
```

    arr_1:  [  1.   2.  inf   4. -inf]
    inf arr:  [False False  True False  True]
    
