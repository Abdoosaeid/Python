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
    
```python
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})

grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})

#print(grades.loc[grades.Math > 3])
print(grades.loc[grades["Math"] > 3])
```

       Math  Physics  French  Chemistry
    d     4        9      14         19
    e     5       10      15         20
    


```python
print(grades.loc[grades["Math"] > 3 , ['French','Math']])
```

       French  Math
    d      14     4
    e      15     5
    

# Sort


```python
print(grades.sort_values(['Math'],ascending=False))
```

       Math  Physics  French  Chemistry
    e     5       10      15         20
    d     4        9      14         19
    c     3        8      13         18
    b     2        7      12         17
    a     1        6      11         16
    


```python
print(grades.sort_values(['French'],ascending=True))
```

       Math  Physics  French  Chemistry
    a     1        6      11         16
    b     2        7      12         17
    c     3        8      13         18
    d     4        9      14         19
    e     5       10      15         20
    


```python
print(grades.max())
print(20 * '#')
print(grades.min())
print(20 * '#')
print(grades.mean())
print(20 * '#')
print(grades.std())
```

    Math          5
    Physics      10
    French       15
    Chemistry    20
    dtype: int64
    ####################
    Math          1
    Physics       6
    French       11
    Chemistry    16
    dtype: int64
    ####################
    Math          3.0
    Physics       8.0
    French       13.0
    Chemistry    18.0
    dtype: float64
    ####################
    Math         1.581139
    Physics      1.581139
    French       1.581139
    Chemistry    1.581139
    dtype: float64
    


```python
print(grades["Math"].max())
print(20 * '#')
print(grades["French"].min())
print(20 * '#')
print(grades["Physics"].mean())
print(20 * '#')
print(grades["Chemistry"].std())
```

    5
    ####################
    11
    ####################
    8.0
    ####################
    1.5811388300841898
    

# corr


```python
import numpy as np 

df = pd.DataFrame(np.random.rand(5,3),columns=['A','B','C'])

print(df)

print(df.corr())
```

              A         B         C
    0  0.274713  0.773795  0.548408
    1  0.277038  0.554168  0.335822
    2  0.150049  0.174010  0.382024
    3  0.399421  0.213939  0.898824
    4  0.047823  0.371983  0.133913
              A         B         C
    A  1.000000  0.116482  0.895262
    B  0.116482  1.000000 -0.143480
    C  0.895262 -0.143480  1.000000
    

# skew


```python
print(df.skew())
```

    A   -0.249189
    B    0.666546
    C    0.856754
    dtype: float64
    

<hr style="border: 1px solid black;">


```python
data = [{'square':i**2} for i in range(10)]
d = pd.DataFrame(data)
print(d)
```

       square
    0       0
    1       1
    2       4
    3       9
    4      16
    5      25
    6      36
    7      49
    8      64
    9      81
    


```python
data = [{'square':i**2 , 'cube':i**3,'root':i**0.5} for i in range(10)]
d = pd.DataFrame(data)
print(d)
```

       square  cube      root
    0       0     0  0.000000
    1       1     1  1.000000
    2       4     8  1.414214
    3       9    27  1.732051
    4      16    64  2.000000
    5      25   125  2.236068
    6      36   216  2.449490
    7      49   343  2.645751
    8      64   512  2.828427
    9      81   729  3.000000
    


```python
d = pd.DataFrame([{'a':1,'b':2},{'a':3,'b':4},{'a':5,'b':6}])

print(d)

```

       a  b
    0  1  2
    1  3  4
    2  5  6
    


```python
d = pd.DataFrame([{'a':1,'b':2},{'b':3,'c':4},{'d':5,'e':6}])

print(d)

```

         a    b    c    d    e
    0  1.0  2.0  NaN  NaN  NaN
    1  NaN  3.0  4.0  NaN  NaN
    2  NaN  NaN  NaN  5.0  6.0
    


```python

```
```python
import pandas as pd
import numpy as np 
```


```python
data = pd.DataFrame(
    np.random.rand(3,2),
    columns=['food','drink'],
    index=['a','b','c']
)

print(data)
```

           food     drink
    a  0.796781  0.450826
    b  0.741455  0.870008
    c  0.867741  0.046827
    

# create a new column


```python
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})

grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
 
grades['Total'] = (grades['Math'] + grades['French'] + 
      grades['Chemistry']+ grades['Physics']) /100


print(grades)

```

       Math  Physics  French  Chemistry  Total
    a     1        6      11         16   0.34
    b     2        7      12         17   0.38
    c     3        8      13         18   0.42
    d     4        9      14         19   0.46
    e     5       10      15         20   0.50
    


```python
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])

result = (df['A'] + df['B']) / (df['C'] - 1)

print(df)
print(result)

```

              A         B         C
    0  0.979880  0.567226  0.824624
    1  0.893897  0.941644  0.871107
    2  0.429491  0.735036  0.711452
    3  0.209637  0.778535  0.415848
    4  0.050554  0.704991  0.441381
    0    -8.821669
    1   -14.240791
    2    -4.035814
    3    -1.691633
    4    -1.352522
    dtype: float64
    

# eval


```python
result =  pd.eval("(df.A + df.B) / (df.C - 1)")

print(df)
print(result)
```

              A         B         C
    0  0.979880  0.567226  0.824624
    1  0.893897  0.941644  0.871107
    2  0.429491  0.735036  0.711452
    3  0.209637  0.778535  0.415848
    4  0.050554  0.704991  0.441381
    0    -8.821669
    1   -14.240791
    2    -4.035814
    3    -1.691633
    4    -1.352522
    dtype: float64
    

# query


```python
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
result = df.query('A < 0.5 and B < 0.5')
print(df)
print(result)
```

              A         B         C
    0  0.211736  0.984552  0.177816
    1  0.670696  0.916496  0.914339
    2  0.409523  0.014376  0.646163
    3  0.875244  0.452305  0.182727
    4  0.711645  0.494744  0.690766
              A         B         C
    2  0.409523  0.014376  0.646163
    

# condition 


```python
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
temp1 = df.A < 0.5
temp2 = df.B < 0.5
temp3 = temp1 & temp2
result = df[temp3]

print(df)
print(result)
```

              A         B         C
    0  0.985698  0.256001  0.097107
    1  0.973312  0.616169  0.814549
    2  0.488721  0.836216  0.972975
    3  0.153523  0.042650  0.010157
    4  0.264185  0.858797  0.926854
              A        B         C
    3  0.153523  0.04265  0.010157
    

# function 


```python
def make_df(cols,indexs):
    data = {c:[str(c) + str(i) for i in indexs] for c in cols}
    return pd.DataFrame(data,indexs)

print(make_df('ABC',range(3)))

```

        A   B   C
    0  A0  B0  C0
    1  A1  B1  C1
    2  A2  B2  C2
    


```python

```
```python
import pandas as pd 

```


```python
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering',
                              'Engineering', 'HR']})

df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})

```


```python
print(df1)
print(50 * '*')
print(df2)
```

      employee        group
    0      Bob   Accounting
    1     Jake  Engineering
    2     Lisa  Engineering
    3      Sue           HR
    **************************************************
      employee  hire_date
    0     Lisa       2004
    1      Bob       2008
    2     Jake       2012
    3      Sue       2014
    

# merge 


```python
df3 =  pd.merge(df1,df2)
```


```python
print(df3)
```

      employee        group  hire_date
    0      Bob   Accounting       2008
    1     Jake  Engineering       2012
    2     Lisa  Engineering       2004
    3      Sue           HR       2014
    


```python
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
print(df4)

```

             group supervisor
    0   Accounting      Carly
    1  Engineering      Guido
    2           HR      Steve
    


```python
df5 = pd.merge(df3, df4)
print(df5)
```

      employee        group  hire_date supervisor
    0      Bob   Accounting       2008      Carly
    1     Jake  Engineering       2012      Guido
    2     Lisa  Engineering       2004      Guido
    3      Sue           HR       2014      Steve
    

# move columns in data frame 


```python
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})

df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})

```


```python
print(df1)
print(df3)

```

      employee        group
    0      Bob   Accounting
    1     Jake  Engineering
    2     Lisa  Engineering
    3      Sue           HR
       name  salary
    0   Bob   70000
    1  Jake   80000
    2  Lisa  120000
    3   Sue   90000
    


```python
print(pd.merge(df1,df3,left_on="employee",right_on="name"))
```

      employee        group  name  salary
    0      Bob   Accounting   Bob   70000
    1     Jake  Engineering  Jake   80000
    2     Lisa  Engineering  Lisa  120000
    3      Sue           HR   Sue   90000
    

# drop


```python
print(pd.merge(df1,df3,left_on="employee",right_on="name").drop('name',axis=1))
```

      employee        group  salary
    0      Bob   Accounting   70000
    1     Jake  Engineering   80000
    2     Lisa  Engineering  120000
    3      Sue           HR   90000
    

# set_index


```python
print(df1)
```

      employee        group
    0      Bob   Accounting
    1     Jake  Engineering
    2     Lisa  Engineering
    3      Sue           HR
    


```python
df2 = df1.set_index('employee')
print(df2)
```

                    group
    employee             
    Bob        Accounting
    Jake      Engineering
    Lisa      Engineering
    Sue                HR
    

# merge


```python
df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])

df2 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['cola', '7 up']},
                    columns=['name', 'drink'])

```


```python
print(df1)
print(50 * '*')
print(df2)
```

        name   food
    0  Peter   fish
    1   Paul  beans
    2   Mary  bread
    **************************************************
         name drink
    0    Mary  cola
    1  Joseph  7 up
    


```python
#df3 = pd.merge(df1,df2,how='inner')
df3 = pd.merge(df1,df2)
print(df3) #He takes what is common between them
```

       name   food drink
    0  Mary  bread  cola
    

# outer


```python
df3 = pd.merge(df1,df2,how='outer')
print(df3)
```

         name   food drink
    0   Peter   fish   NaN
    1    Paul  beans   NaN
    2    Mary  bread  cola
    3  Joseph    NaN  7 up
    

# right 


```python
df3 = pd.merge(df1,df2,how='right')
print(df3) # He will take the second one in any case
```

         name   food drink
    0    Mary  bread  cola
    1  Joseph    NaN  7 up
    

# left


```python
df3 = pd.merge(df1,df2,how='left')
print(df3)# He will take the first one in any case
```

        name   food drink
    0  Peter   fish   NaN
    1   Paul  beans   NaN
    2   Mary  bread  cola
    

# means for columns


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': np.random.rand(10),'B': np.random.rand(10)})
print(df)
print('------------------------------')
print(df.mean(axis='columns'))

```

              A         B
    0  0.354372  0.975776
    1  0.277095  0.282279
    2  0.022062  0.751670
    3  0.869930  0.601288
    4  0.970985  0.514810
    5  0.399348  0.801975
    6  0.215024  0.458350
    7  0.336082  0.581840
    8  0.301763  0.042026
    9  0.572530  0.835639
    ------------------------------
    0    0.665074
    1    0.279687
    2    0.386866
    3    0.735609
    4    0.742898
    5    0.600662
    6    0.336687
    7    0.458961
    8    0.171894
    9    0.704085
    dtype: float64
    

# groupby


```python
df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])

print(df)

```

      key  data
    0   A     0
    1   B     1
    2   C     2
    3   A     3
    4   B     4
    5   C     5
    


```python
print(df.groupby('key').sum())
```

         data
    key      
    A       3
    B       5
    C       7
    


```python
print(df.groupby('key').describe())
```

         data                                         
        count mean      std  min   25%  50%   75%  max
    key                                               
    A     2.0  1.5  2.12132  0.0  0.75  1.5  2.25  3.0
    B     2.0  2.5  2.12132  1.0  1.75  2.5  3.25  4.0
    C     2.0  3.5  2.12132  2.0  2.75  3.5  4.25  5.0
    


```python
print(df.groupby('key').describe().unstack())
```

                 key
    data  count  A      2.00000
                 B      2.00000
                 C      2.00000
          mean   A      1.50000
                 B      2.50000
                 C      3.50000
          std    A      2.12132
                 B      2.12132
                 C      2.12132
          min    A      0.00000
                 B      1.00000
                 C      2.00000
          25%    A      0.75000
                 B      1.75000
                 C      2.75000
          50%    A      1.50000
                 B      2.50000
                 C      3.50000
          75%    A      2.25000
                 B      3.25000
                 C      4.25000
          max    A      3.00000
                 B      4.00000
                 C      5.00000
    dtype: float64
    

# aggregate


```python
import numpy as np

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])

print(df)
df2 = df.groupby('key').aggregate({'data1': 'min','data2': 'max'})
print(df2)

```

      key  data1  data2
    0   A      0      6
    1   B      1      1
    2   C      2      8
    3   A      3      9
    4   B      4      5
    5   C      5      8
         data1  data2
    key              
    A        0      9
    B        1      5
    C        2      8
    

# filter


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])

print(df)
def filter_func(x):
    return x['data2'].std() > 4

df2 = df.groupby('key').filter(filter_func)
print(df2)

```

      key  data1  data2
    0   A      0      0
    1   B      1      6
    2   C      2      2
    3   A      3      1
    4   B      4      8
    5   C      5      3
    Empty DataFrame
    Columns: [key, data1, data2]
    Index: []
    

# transform


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])

print(df)

df2 = df.groupby('key').transform(lambda x: x**2)

print(df2)

```

      key  data1  data2
    0   A      0      4
    1   B      1      7
    2   C      2      1
    3   A      3      5
    4   B      4      0
    5   C      5      3
       data1  data2
    0      0     16
    1      1     49
    2      4      1
    3      9     25
    4     16      0
    5     25      9
    
 
# MultiIndex


```python
import pandas as pd
```


```python
index = [('California', 2000),('California', 2010),
         ('New York', 2000),('New York', 2010),
         ('Texas', 2000),('Texas', 2010)]

populations = [10000,15000,
               20000,25000,
               30000,35000]

```


```python
index = pd.MultiIndex.from_tuples(index)
index
```




    MultiIndex([('California', 2000),
                ('California', 2010),
                (  'New York', 2000),
                (  'New York', 2010),
                (     'Texas', 2000),
                (     'Texas', 2010)],
               )




```python
pop = pd.Series(populations,index=index)
pop
```




    California  2000    10000
                2010    15000
    New York    2000    20000
                2010    25000
    Texas       2000    30000
                2010    35000
    dtype: int64




```python
pop = pop.reindex(index)
print(pop)
```

    California  2000    10000
                2010    15000
    New York    2000    20000
                2010    25000
    Texas       2000    30000
                2010    35000
    dtype: int64
    


```python
print(pop[:,2010])
```

    California    15000
    New York      25000
    Texas         35000
    dtype: int64
    


```python
print(pop.unstack())
```

                 2000   2010
    California  10000  15000
    New York    20000  25000
    Texas       30000  35000
    


```python
pop_2 = pd.DataFrame({'total':pop,'under18':[9267089, 9284094,4687374,
                                  4318033,5906301, 6879014]})
pop_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>total</th>
      <th>under18</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">California</th>
      <th>2000</th>
      <td>10000</td>
      <td>9267089</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>15000</td>
      <td>9284094</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">New York</th>
      <th>2000</th>
      <td>20000</td>
      <td>4687374</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>25000</td>
      <td>4318033</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Texas</th>
      <th>2000</th>
      <td>30000</td>
      <td>5906301</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>35000</td>
      <td>6879014</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_2["total"]["California"]
```




    2000    10000
    2010    15000
    Name: total, dtype: int64




```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'],
                         [1, 2, 1, 2]],columns=['income', 'profit'])

print(df)

```

           income    profit
    a 1  0.792975  0.182464
      2  0.620677  0.349973
    b 1  0.116269  0.951808
      2  0.767064  0.415084
    


 