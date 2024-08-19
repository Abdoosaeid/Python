# DataFrame
### It is a tool dedicated to creating tables of rows and columns of data.


```python
import pandas as pd 
import numpy as np
```


```python
myarray = np.array([[6,9,8,5,4,2],[0,2,5,6,3,9],
                    [8,5,4,1,2,3],[6,9,8,5,4,2],
                    [0,5,3,6,9,8],[8,7,4,5,2,3],[9,3,6,3,1,2]])
```


```python
rownames = ['a', 'b','c','d','e','f','g']
colnames = ['one', 'two', 'three','four','five','six']

df = pd.DataFrame(myarray,index=rownames,columns=colnames)
print(df)
```

       one  two  three  four  five  six
    a    6    9      8     5     4    2
    b    0    2      5     6     3    9
    c    8    5      4     1     2    3
    d    6    9      8     5     4    2
    e    0    5      3     6     9    8
    f    8    7      4     5     2    3
    g    9    3      6     3     1    2
    


```python
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})

grades = pd.DataFrame({"Math":w,"physics":x,"French":y,"chemistry":z})

print(grades)
```

       Math  physics  French  chemistry
    a     1        6      11         16
    b     2        7      12         17
    c     3        8      13         18
    d     4        9      14         19
    e     5       10      15         20
    


```python
print(grades["chemistry"])
```

    a    16
    b    17
    c    18
    d    19
    e    20
    Name: chemistry, dtype: int64
    


```python
print(grades.T)
```

                a   b   c   d   e
    Math        1   2   3   4   5
    physics     6   7   8   9  10
    French     11  12  13  14  15
    chemistry  16  17  18  19  20
    


```python
print(grades.values)
```

    [[ 1  6 11 16]
     [ 2  7 12 17]
     [ 3  8 13 18]
     [ 4  9 14 19]
     [ 5 10 15 20]]
    


```python
print(grades.keys())
```

    Index(['Math', 'physics', 'French', 'chemistry'], dtype='object')
    

<hr style="border: 1px solid black;">




```python
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})

grades = pd.DataFrame({"Math":w,"physics":x,"French":y,"chemistry":z})

print("Math" in grades.keys())
print("math" in grades.keys())
print(12 in grades.values)
print(55 in grades.values)
```

    True
    False
    True
    False
    


```python
print(grades.stack())
```

    a  Math          1
       physics       6
       French       11
       chemistry    16
    b  Math          2
       physics       7
       French       12
       chemistry    17
    c  Math          3
       physics       8
       French       13
       chemistry    18
    d  Math          4
       physics       9
       French       14
       chemistry    19
    e  Math          5
       physics      10
       French       15
       chemistry    20
    dtype: int64
    

<hr style="border: 1px solid black;">



## Index Location (iloc)


```python
print(grades.iloc[0])  # Select the first row
print(grades.iloc[0:2])# Select the first two rows
```

    Math          1
    physics       6
    French       11
    chemistry    16
    Name: a, dtype: int64
       Math  physics  French  chemistry
    a     1        6      11         16
    b     2        7      12         17
    


```python
print(grades.iloc[:3,:2])
```

       Math  physics
    a     1        6
    b     2        7
    c     3        8
    

## Location


```python
print(grades.loc['b':'c',"Math":])
```

       Math  physics  French  chemistry
    b     2        7      12         17
    c     3        8      13         18
    
