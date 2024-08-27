## concatenating Arrays 


```python
import numpy as np 
```


```python
arr1 = np.array([1,2,3]) 
arr2 = np.array([4,5,6])
concatenated_arrays = np.concatenate((arr1,arr2))
concatenated_arrays
```




    array([1, 2, 3, 4, 5, 6])



## checking for elements-wise equality 


```python
arr3 = np.array([1,2,4])
elements_wise_equal = np.array_equal(arr1,arr3)
elements_wise_equal
```




    False



## checking for elements-wise equality


```python
elements_wise_equal = np.equal(arr1,arr3)
elements_wise_equal
```




    array([ True,  True, False])



## checking for elements-wise inequality 
 


```python
elements_wise_not_equal = np.not_equal(arr1,arr3)
elements_wise_not_equal
```




    array([False, False,  True])



# Array Indexing and Slicing 


```python
x = np.arange(0,20).reshape(4,5)
print(x)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    


```python
x[0,0]
```




    0




```python
x[0,1]
```




    1




```python
print(x[2,2])
print(x[2][2])
```

    12
    12
    


```python
x[2]
```




    array([10, 11, 12, 13, 14])




```python
x[0,0] = 20
```


```python
print(x)
```

    [[20  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    


```python
z = x[1:4,2:5]
print(z)
```

    [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
    


```python
z = x[1: , 2: ]
print(z)
```

    [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
    

 ## Take copy


```python
x = np.arange(20).reshape(4,5)
print(x)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    


```python
z = np.copy(x[1:,2:])
print(z)
```

    [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
    


```python
z = x[1:,2:].copy()
print(z)
```

    [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
    

 ## values in the meaning diagonal


```python
print(x)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    


```python
z = np.diag(x)
print(z)
```

    [ 0  6 12 18]
    

## The values in the Top of the mean diagonal


```python
z = np.diag(x,k=1)
print(z)
```

    [ 1  7 13 19]
    


```python
z = np.diag(x,k=2)
print(z)
```

    [ 2  8 14]
    

## The values in the Below of the mean diagonal


```python
z = np.diag(x,k=-1)
print(z)
```

    [ 5 11 17]
    

## Unique 


```python
x = np.array([[1,2,3],[5,2,8],[1,2,3]])
print(x)
```

    [[1 2 3]
     [5 2 8]
     [1 2 3]]
    


```python
print(np.unique(x))
```

    [1 2 3 5 8]
    

# comparison operators


```python
x = np.arange(25).reshape(5,5)
print(x)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]
     [20 21 22 23 24]]
    


```python
print(x > 10)
```

    [[False False False False False]
     [False False False False False]
     [False  True  True  True  True]
     [ True  True  True  True  True]
     [ True  True  True  True  True]]
    


```python
print(x[x>10])
```

    [11 12 13 14 15 16 17 18 19 20 21 22 23 24]
    




    numpy.ndarray




```python
print(x[x<=7])
```

    [0 1 2 3 4 5 6 7]
    


```python
x[(x>10) & (x<17)] = -1
print(x)
```

    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 -1 -1 -1 -1]
     [-1 -1 17 18 19]
     [20 21 22 23 24]]
    


```python
x = np.array([1,2,3,4,5])
y = np.array([6,7,2,8,4])
print(np.intersect1d(x,y))
print(np.setdiff1d(x,y))
print(np.union1d(x,y))
```

    [2 4]
    [1 3 5]
    [1 2 3 4 5 6 7 8]
    
