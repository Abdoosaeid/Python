```python
import numpy as np
```

# sorting and Searching 


```python
x = np.array([4,2,8,5,1,7,6,3])
print(x)
```

    [4 2 8 5 1 7 6 3]
    

## sorting Ascending 


```python
print(np.sort(x))
```

    [1 2 3 4 5 6 7 8]
    


```python
print(x)
```

    [4 2 8 5 1 7 6 3]
    


```python
x.sort()
```


```python
print(x)
```

    [1 2 3 4 5 6 7 8]
    

## sorting Descending 


```python
x = np.array([4,2,8,5,1,7,6,3])
print(x)
```

    [4 2 8 5 1 7 6 3]
    


```python
print(np.sort(x)[::-1])
```

    [8 7 6 5 4 3 2 1]
    

## indices of sorted elements 


```python
print(x)
print(np.array([0,1,2,3,4,5,6,7]))
indices_of_sorted = np.argsort(x)
indices_of_sorted
```

    [4 2 8 5 1 7 6 3]
    [0 1 2 3 4 5 6 7]
    




    array([4, 1, 7, 0, 3, 6, 5, 2], dtype=int64)



## sorting by a specific column 


```python
x = np.random.randint(1,11,size=(5,5))
print(x)
```

    [[ 4  3  2  3  6]
     [ 6  4  2  3  8]
     [ 9  8  4  4  4]
     [ 9  3  3 10  6]
     [ 8  5  1  1  9]]
    


```python
sorted_x = x[x[:,0].argsort()] # sort column 0
print(sorted_x) 
```

    [[ 4  3  2  3  6]
     [ 6  4  2  3  8]
     [ 8  5  1  1  9]
     [ 9  8  4  4  4]
     [ 9  3  3 10  6]]
    


```python
print(np.sort(x,axis=0)) # sort the rows 
```

    [[ 4  3  1  1  4]
     [ 6  3  2  3  6]
     [ 8  4  2  3  6]
     [ 9  5  3  4  8]
     [ 9  8  4 10  9]]
    


```python
print(np.sort(x,axis=1))# sort the columns 
```

    [[ 2  3  3  4  6]
     [ 2  3  4  6  8]
     [ 4  4  4  8  9]
     [ 3  3  6  9 10]
     [ 1  1  5  8  9]]
    

# Searching 


```python
print(x)
```

    [[ 4  3  2  3  6]
     [ 6  4  2  3  8]
     [ 9  8  4  4  4]
     [ 9  3  3 10  6]
     [ 8  5  1  1  9]]
    

## finding the index of the maximum value 


```python
max_index = np.argmax(x)
print(max_index)
```

    18
    


```python
max_index = np.argmin(x)
print(max_index)
```

    22
    

# Mathematical Operations 


```python
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
print(x)
print(y)
```

    [1 2 3 4]
    [5 6 7 8]
    


```python
print(x+y)
print(np.add(x,y))
```

    [ 6  8 10 12]
    [ 6  8 10 12]
    


```python
print(x-y)
print(np.subtract(x,y))
```

    [-4 -4 -4 -4]
    [-4 -4 -4 -4]
    


```python
print(x*y)
print(np.multiply(x,y))
```

    [ 5 12 21 32]
    [ 5 12 21 32]
    


```python
print(x/y)
print(np.divide(x,y))
```

    [0.2        0.33333333 0.42857143 0.5       ]
    [0.2        0.33333333 0.42857143 0.5       ]
    


```python
x = np.array([1,2,3,4])
print(x)
```

    [1 2 3 4]
    


```python
print(np.sqrt(x))
```

    [1.         1.41421356 1.73205081 2.        ]
    


```python
print(np.exp(x))
```

    [ 2.71828183  7.3890561  20.08553692 54.59815003]
    


```python
print(np.power(x,2))
```

    [ 1  4  9 16]
    

# Mean and Sum 


```python
x = np.arange(4).reshape(2,2)
print(x)
```

    [[0 1]
     [2 3]]
    


```python
print("average of all: ",x.mean())
print("average of columns: ",x.mean(axis = 0))
print("average of rows: ",x.mean(axis = 1))
```

    average of all:  1.5
    average of columns:  [1. 2.]
    average of rows:  [0.5 2.5]
    


```python
print("sum of all: ",x.sum())
print("sum of columns: ",x.sum(axis = 0))
print("average of rows: ",x.sum(axis = 1))
```

    sum of all:  6
    sum of columns:  [2 4]
    average of rows:  [1 5]
    


```python
print(3 + x)
```

    [[3 4]
     [5 6]]
    


```python
x = np.arange(3)
y = np.arange(9).reshape(3,3)
print("x: ",x)
print("y: ",y)
```

    x:  [0 1 2]
    y:  [[0 1 2]
     [3 4 5]
     [6 7 8]]
    


```python
print(x + y) # add x for all rows 
```

    [[ 0  2  4]
     [ 3  5  7]
     [ 6  8 10]]
    


```python
x = np.arange(3).reshape(3,1)
print(x)
```

    [[0]
     [1]
     [2]]
    


```python
print(x + y) # add x for all columns  
```

    [[ 0  1  2]
     [ 4  5  6]
     [ 8  9 10]]
    

# Linear Algebra 


```python
x = np.arange(9).reshape(3,3)
y = np.arange(9).reshape(3,3)
print("x: ",x)
print("y: ",y)
```

    x:  [[0 1 2]
     [3 4 5]
     [6 7 8]]
    y:  [[0 1 2]
     [3 4 5]
     [6 7 8]]
    


```python
dot_prodouct_result = np.dot(x,y)
print(dot_prodouct_result)
```

    [[ 15  18  21]
     [ 42  54  66]
     [ 69  90 111]]
    


```python
matrix_multiplication = np.matmul(x,y)
print(matrix_multiplication)
```

    [[ 15  18  21]
     [ 42  54  66]
     [ 69  90 111]]
    

## Determinant value


```python
x = np.array([[1,2],[3,4]])
Det = np.linalg.det(x)
print(Det)
```

    -2.0000000000000004
    

## matrix Inversion 


```python
Inv = np.linalg.inv(x)
Inv
```




    array([[-2. ,  1. ],
           [ 1.5, -0.5]])



## EigenValues and EigenVectors 


```python
eigenvalues , eigenvectors = np.linalg.eig(x)
print('eigenvalues: ',eigenvalues)
print('eigenvectors: ',eigenvectors)
```

    eigenvalues:  [-0.37228132  5.37228132]
    eigenvectors:  [[-0.82456484 -0.41597356]
     [ 0.56576746 -0.90937671]]
    

# Statistics Operations


```python
print(x.mean())
print(np.mean(x))
```

    2.5
    2.5
    


```python
print(x.var())
print(np.var(x))
```

    1.25
    1.25
    


```python
print(x.std())
print(np.std(x))
```

    1.118033988749895
    1.118033988749895
    


```python
#print(x.median())
print(np.median(x))
```

    2.5
    


```python
print(x.max())
print(np.max(x))
```

    4
    4
    


```python
print(x.sum())
print(np.sum(x))
```

    10
    10
    


```python
x = np.random.randint(1,11,size = (5,5))
print(x)
```

    [[ 8  2  2  3  1]
     [ 3  1  9  9  1]
     [ 1  4  8  2  9]
     [ 2  2  3  5  4]
     [ 8  6  2  3 10]]
    


```python
unique_values , value_counts = np.unique(x,return_counts=True)
print("unique Values: ",unique_values)
print("values Count: ",value_counts)
```

    unique Values:  [ 1  2  3  4  5  6  8  9 10]
    values Count:  [4 6 4 2 1 1 3 3 1]
    

## correlation matrix


```python
correlation = np.corrcoef(x)
correlation
```




    array([[ 1.        , -0.035169  , -0.75337126, -0.42841224,  0.16690807],
           [-0.035169  ,  1.        , -0.07530715,  0.48651277, -0.88210791],
           [-0.75337126, -0.07530715,  1.        ,  0.17217245,  0.10061677],
           [-0.42841224,  0.48651277,  0.17217245,  1.        , -0.21771589],
           [ 0.16690807, -0.88210791,  0.10061677, -0.21771589,  1.        ]])



## covariance matrix 


```python
covariance_matrix = np.cov(x)
covariance_matrix
```




    array([[  7.7 ,  -0.4 ,  -7.45,  -1.55,   1.55],
           [ -0.4 ,  16.8 ,  -1.1 ,   2.6 , -12.1 ],
           [ -7.45,  -1.1 ,  12.7 ,   0.8 ,   1.2 ],
           [ -1.55,   2.6 ,   0.8 ,   1.7 ,  -0.95],
           [  1.55, -12.1 ,   1.2 ,  -0.95,  11.2 ]])


