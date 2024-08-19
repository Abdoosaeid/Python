```python
import pandas as pd

```


```python
data = {('California', 2000): 10000,('California', 2010):15000,
        ('Texas', 2000): 20000,('Texas', 2010): 25000,
        ('New York', 2000): 30000,('New York', 2010): 35000}
df = pd.Series(data)

print(df)

```

    California  2000    10000
                2010    15000
    Texas       2000    20000
                2010    25000
    New York    2000    30000
                2010    35000
    dtype: int64
    

# from_tuples


```python
info = {('A',10),('A',20),('B',10),('B',20),('B',30),('C',10),('C',20),('C',30),('C',40),('F',10)}
index = pd.MultiIndex.from_tuples(info).sort_values()
```


```python
index
 
```




    MultiIndex([('A', 10),
                ('A', 20),
                ('B', 10),
                ('B', 20),
                ('B', 30),
                ('C', 10),
                ('C', 20),
                ('C', 30),
                ('C', 40),
                ('F', 10)],
               )




```python
data = [1,2,3,4,5,6,7,8,9,10]
df = pd.Series(data,index=index)
```


```python
df
```




    A  10     1
       20     2
    B  10     3
       20     4
       30     5
    C  10     6
       20     7
       30     8
       40     9
    F  10    10
    dtype: int64




```python
df['A']
```




    10    1
    20    2
    dtype: int64




```python
df['A'][20]
```




    2



# from_product


```python
import pandas as pd 
import numpy as np 
```


```python
index = pd.MultiIndex.from_product([[2013,2014],[1,2]],names=['years','visit'])

columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'],
                                      ['HR', 'Temp']])
                                     
data = np.round(np.random.randn(4, 6))                                   
                                     
data = pd.DataFrame(data , index = index,columns=columns)
                                     
print(data)                                                                   
```

                 Bob      Guido       Sue     
                  HR Temp    HR Temp   HR Temp
    years visit                               
    2013  1     -1.0  0.0   0.0 -1.0  0.0 -1.0
          2     -1.0 -1.0   1.0  1.0  0.0  0.0
    2014  1     -0.0 -1.0   1.0 -1.0 -1.0 -1.0
          2      0.0  1.0   1.0 -1.0 -1.0 -1.0
    


```python
print(data['Guido','HR'][:2015])
```

    years  visit
    2013   1        0.0
           2        1.0
    2014   1        1.0
           2        1.0
    Name: (Guido, HR), dtype: float64
    

# loc


```python
print(data.loc[:,('Bob')])
```

                  HR  Temp
    years visit           
    2013  1     -1.0   0.0
          2     -1.0  -1.0
    2014  1     -0.0  -1.0
          2      0.0   1.0
    


```python
print(data.loc[:,('Bob','HR')])
```

    years  visit
    2013   1       -1.0
           2       -1.0
    2014   1       -0.0
           2        0.0
    Name: (Bob, HR), dtype: float64
    

# IndexSlice


```python
 idx = pd.IndexSlice
print(type(idx))   
```

    <class 'pandas.core.indexing._IndexSlice'>
    


```python
print(data.
      loc[
          idx[:,1]
          ,idx[:,'HR']
      ]
     )
```

                 Bob Guido  Sue
                  HR    HR   HR
    years visit                
    2013  1     -1.0   0.0  0.0
    2014  1     -0.0   1.0 -1.0
    
# Strings 


```python
import pandas as pd 
```


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

lenth = pd.Series(data).str.len()
print(lenth)
```

    0    5
    1    4
    2    4
    3    2
    4    2
    dtype: int64
    

# startwith & endswith 


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

print(pd.Series(data).str.startswith('P'))
```

    0    False
    1     True
    2    False
    3    False
    4    False
    dtype: bool
    


```python
print(pd.Series(data).str.endswith('Y'))
```

    0    False
    1    False
    2     True
    3    False
    4    False
    dtype: bool
    

# find & rfind 


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

print(pd.Series(data).str.find('t')) # find from left if it not exit return -1 
```

    0    2
    1   -1
    2   -1
    3   -1
    4   -1
    dtype: int64
    


```python
print(pd.Series(data).str.rfind('A')) # find from right 
```

    0   -1
    1   -1
    2    1
    3   -1
    4   -1
    dtype: int64
    

# rjust & ljust


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

print(pd.Series(data).str.rjust(20))  
```

    0                   peter
    1                    Paul
    2                    MARY
    3                      15
    4                        
    dtype: object
    


```python
print(pd.Series(data).str.ljust(50))  
```

    0    peter                                         ...
    1    Paul                                          ...
    2    MARY                                          ...
    3    15                                            ...
    4                                                  ...
    dtype: object
    

# center & zfill


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

print(pd.Series(data).str.center(5)) 
```

    0    peter
    1     Paul
    2     MARY
    3      15 
    4         
    dtype: object
    


```python
print(pd.Series(data).str.zfill(10))  
```

    0    00000peter
    1    000000Paul
    2    000000MARY
    3    0000000015
    4    00000000  
    dtype: object
    

   # isupper & islower & istitle


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

print(pd.Series(data).str.isupper())  
```

    0    False
    1    False
    2     True
    3    False
    4    False
    dtype: bool
    


```python
print(pd.Series(data).str.islower())  
```

    0     True
    1    False
    2    False
    3    False
    4    False
    dtype: bool
    


```python
print(pd.Series(data).str.istitle())  
```

    0    False
    1     True
    2    False
    3    False
    4    False
    dtype: bool
    

# isspace & isdigit & isalpha


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]

print(pd.Series(data).str.isspace())  
```

    0    False
    1    False
    2    False
    3    False
    4     True
    dtype: bool
    


```python
print(pd.Series(data).str.isdigit())  
```

    0    False
    1    False
    2    False
    3     True
    4    False
    dtype: bool
    


```python
print(pd.Series(data).str.isalpha())  
```

    0     True
    1     True
    2     True
    3    False
    4    False
    dtype: bool
    

# isalnum & isdecimal & isnumeric


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]
```


```python
print(pd.Series(data).str.isalnum()) # is it not got any spaces 
```

    0     True
    1     True
    2     True
    3     True
    4    False
    dtype: bool
    


```python
print(pd.Series(data).str.isdecimal())
```

    0    False
    1    False
    2    False
    3     True
    4    False
    dtype: bool
    


```python
print(pd.Series(data).str.isnumeric())
```

    0    False
    1    False
    2    False
    3     True
    4    False
    dtype: bool
    

# upper & capitalize


```python
data = ['peter', 'Paul', 'MARY', '15' , '  ','app']
```


```python
print(pd.Series(data).str.upper())
```

    0    PETER
    1     PAUL
    2     MARY
    3       15
    4         
    5      APP
    dtype: object
    


```python
print(pd.Series(data).str.capitalize()) # make all like "This"
```

    0    Peter
    1     Paul
    2     Mary
    3       15
    4         
    5      App
    dtype: object
    

# lower & swapcase 


```python
print(pd.Series(data).str.lower())
```

    0    peter
    1     paul
    2     mary
    3       15
    4         
    5      app
    dtype: object
    


```python
print(pd.Series(data).str.swapcase()) # switch capital & small 
```

    0    PETER
    1     pAUL
    2     mary
    3       15
    4         
    5      APP
    dtype: object
    
# Date


```python
import pandas as pd
```


```python
date = pd.to_datetime("4th of July, 2018")
print(date)
```

    2018-07-04 00:00:00
    


```python
date = pd.to_datetime("4 July 2018")
print(date)
```

    2018-07-04 00:00:00
    


```python
date = pd.to_datetime("4 7 2018")
print(date)
```

    2018-04-07 00:00:00
    

# Add days 


```python
import numpy as np 

y = pd.to_datetime("4 July 2018")
x = y + pd.to_timedelta(np.arange(20),'D')
print(y)
print(50 * '#')
print(x)
```

    2018-07-04 00:00:00
    ##################################################
    DatetimeIndex(['2018-07-04', '2018-07-05', '2018-07-06', '2018-07-07',
                   '2018-07-08', '2018-07-09', '2018-07-10', '2018-07-11',
                   '2018-07-12', '2018-07-13', '2018-07-14', '2018-07-15',
                   '2018-07-16', '2018-07-17', '2018-07-18', '2018-07-19',
                   '2018-07-20', '2018-07-21', '2018-07-22', '2018-07-23'],
                  dtype='datetime64[ns]', freq=None)
    


```python
y = pd.to_datetime("4 July 2018")
x = y - pd.to_timedelta(np.arange(20),'D')
print(y)
print(50 * '#')
print(x)
```

    2018-07-04 00:00:00
    ##################################################
    DatetimeIndex(['2018-07-04', '2018-07-03', '2018-07-02', '2018-07-01',
                   '2018-06-30', '2018-06-29', '2018-06-28', '2018-06-27',
                   '2018-06-26', '2018-06-25', '2018-06-24', '2018-06-23',
                   '2018-06-22', '2018-06-21', '2018-06-20', '2018-06-19',
                   '2018-06-18', '2018-06-17', '2018-06-16', '2018-06-15'],
                  dtype='datetime64[ns]', freq=None)
    

# Index


```python
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04','2015-08-04'])

date = pd.Series([1,2,3,4],index=index)
print(date)
```

    2014-07-04    1
    2014-08-04    2
    2015-07-04    3
    2015-08-04    4
    dtype: int64
    


```python
index = pd.DatetimeIndex(['2011-03-12', '2012-08-21',
                          '2013-07-11','2014-11-08'])

data = pd.Series([0, 1, 2, 3], index=index)

print(data['2011-01-01':'2012-12-31'])

```

    2011-03-12    0
    2012-08-21    1
    dtype: int64
    


```python
index = pd.DatetimeIndex(['2011-03-12', '2012-08-21',
                          '2013-07-11','2014-11-08'])

data = pd.Series([0, 1, 2, 3], index=index)

print(data['2012'])

```

    2012-08-21    1
    dtype: int64
    


```python
index = pd.DatetimeIndex(['2011-03-12', '2012-08-21',
                          '2013-07-11','2014-11-08'])

data = pd.Series([0, 1, 2, 3], index=index)

print(data['2012-08'])

```

    2012-08-21    1
    dtype: int64
    

# date_range


```python
date = pd.date_range('2011-12-25','2012-01-08')

print(date)
```

    DatetimeIndex(['2011-12-25', '2011-12-26', '2011-12-27', '2011-12-28',
                   '2011-12-29', '2011-12-30', '2011-12-31', '2012-01-01',
                   '2012-01-02', '2012-01-03', '2012-01-04', '2012-01-05',
                   '2012-01-06', '2012-01-07', '2012-01-08'],
                  dtype='datetime64[ns]', freq='D')
    


```python
date = pd.date_range('2011-12-25',periods=8)

print(date)
```

    DatetimeIndex(['2011-12-25', '2011-12-26', '2011-12-27', '2011-12-28',
                   '2011-12-29', '2011-12-30', '2011-12-31', '2012-01-01'],
                  dtype='datetime64[ns]', freq='D')
    


```python
date = pd.date_range('2011-12-25',periods=8,freq='H') # add hours

print(date)
```

    DatetimeIndex(['2011-12-25 00:00:00', '2011-12-25 01:00:00',
                   '2011-12-25 02:00:00', '2011-12-25 03:00:00',
                   '2011-12-25 04:00:00', '2011-12-25 05:00:00',
                   '2011-12-25 06:00:00', '2011-12-25 07:00:00'],
                  dtype='datetime64[ns]', freq='H')
    


```python
date = pd.date_range('2011-12-25',periods=8,freq='M') # add Months

print(date)
```

    DatetimeIndex(['2011-12-31', '2012-01-31', '2012-02-29', '2012-03-31',
                   '2012-04-30', '2012-05-31', '2012-06-30', '2012-07-31'],
                  dtype='datetime64[ns]', freq='M')
    

# timedelta_range


```python
date = pd.timedelta_range(0,periods=8,freq='H')

print(date)
```

    TimedeltaIndex(['0 days 00:00:00', '0 days 01:00:00', '0 days 02:00:00',
                    '0 days 03:00:00', '0 days 04:00:00', '0 days 05:00:00',
                    '0 days 06:00:00', '0 days 07:00:00'],
                   dtype='timedelta64[ns]', freq='H')
    


```python
 date = pd.timedelta_range(0,periods=9,freq='2H30T40S')

print(date)
```

    TimedeltaIndex(['0 days 00:00:00', '0 days 02:30:40', '0 days 05:01:20',
                    '0 days 07:32:00', '0 days 10:02:40', '0 days 12:33:20',
                    '0 days 15:04:00', '0 days 17:34:40', '0 days 20:05:20'],
                   dtype='timedelta64[ns]', freq='9040S')
    


```python
import pandas as pd
from pandas.tseries.offsets import BDay

data = pd.date_range('2018-07-01', periods=5, freq=BDay())# work days

print(data)

```

    DatetimeIndex(['2018-07-02', '2018-07-03', '2018-07-04', '2018-07-05',
                   '2018-07-06'],
                  dtype='datetime64[ns]', freq='B')
    
 
# Read CSV Files


```python
import pandas as pd
```


```python
df = pd.read_csv("Iris.csv")
```


```python
df.head()
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
      <th>Id</th>
      <th>SepalLengthCm</th>
      <th>SepalWidthCm</th>
      <th>PetalLengthCm</th>
      <th>PetalWidthCm</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv("Iris.csv",index_col='SepalWidthCm')
df.head()
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
      <th>Id</th>
      <th>SepalLengthCm</th>
      <th>PetalLengthCm</th>
      <th>PetalWidthCm</th>
      <th>Species</th>
    </tr>
    <tr>
      <th>SepalWidthCm</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3.5</th>
      <td>1</td>
      <td>5.1</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>2</td>
      <td>4.9</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3.2</th>
      <td>3</td>
      <td>4.7</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3.1</th>
      <td>4</td>
      <td>4.6</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3.6</th>
      <td>5</td>
      <td>5.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



# save csv


```python
import pandas as pd


w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})

grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})

print(grades)

grades.to_csv('grades1.csv')
```

       Math  Physics  French  Chemistry
    a     1        6      11         16
    b     2        7      12         17
    c     3        8      13         18
    d     4        9      14         19
    e     5       10      15         20
    

# save Excal


```python
import pandas as pd

w = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
x = pd.Series({'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10})
y = pd.Series({'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15})
z = pd.Series({'a': 16, 'b': 17, 'c': 18, 'd': 19, 'e': 20})

grades = pd.DataFrame({'Math': w, 'Physics': x, 'French': y, 'Chemistry': z})

print(grades)
grades.to_excel('grades2.xlsx', sheet_name='Sheet 1')

```

       Math  Physics  French  Chemistry
    a     1        6      11         16
    b     2        7      12         17
    c     3        8      13         18
    d     4        9      14         19
    e     5       10      15         20
    

# read Excal 


```python
data = pd.read_excel('grades2.xlsx')

print(data)
```

      Unnamed: 0  Math  Physics  French  Chemistry
    0          a     1        6      11         16
    1          b     2        7      12         17
    2          c     3        8      13         18
    3          d     4        9      14         19
    4          e     5       10      15         20
    

# add columns name


```python
from pandas import read_csv
filename = 'grades1.csv'
names = ['a', 'b', 'c', 'd', 'e']
data = read_csv(filename,names=names) 
    
print(data)

```

         a     b        c       d          e
    0  NaN  Math  Physics  French  Chemistry
    1    a     1        6      11         16
    2    b     2        7      12         17
    3    c     3        8      13         18
    4    d     4        9      14         19
    5    e     5       10      15         20
    

# make some option


```python
import pandas as pd
from pandas import read_csv
from pandas import set_option

# Filename
filename = "diabetes.csv"

# Column names
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Read CSV file
data = read_csv(filename, names=names)

# Set display options
set_option('display.width', 100)
set_option('display.precision', 3)

# Get descriptive statistics
description = data.describe()

# Print the description
print(description)
print(50 * '*')
data.head()
```

           preg plas pres skin test mass   pedi  age class
    count   769  769  769  769  769  769    769  769   769
    unique   18  137   48   52  187  249    518   53     3
    top       1  100   70    0    0   32  0.254   22     0
    freq    135   17   57  227  374   13      6   72   500
    **************************************************
    




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
      <th>preg</th>
      <th>plas</th>
      <th>pres</th>
      <th>skin</th>
      <th>test</th>
      <th>mass</th>
      <th>pedi</th>
      <th>age</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Pregnancies</td>
      <td>Glucose</td>
      <td>BloodPressure</td>
      <td>SkinThickness</td>
      <td>Insulin</td>
      <td>BMI</td>
      <td>DiabetesPedigreeFunction</td>
      <td>Age</td>
      <td>Outcome</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>148</td>
      <td>72</td>
      <td>35</td>
      <td>0</td>
      <td>33.6</td>
      <td>0.627</td>
      <td>50</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>85</td>
      <td>66</td>
      <td>29</td>
      <td>0</td>
      <td>26.6</td>
      <td>0.351</td>
      <td>31</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>183</td>
      <td>64</td>
      <td>0</td>
      <td>0</td>
      <td>23.3</td>
      <td>0.672</td>
      <td>32</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>89</td>
      <td>66</td>
      <td>23</td>
      <td>94</td>
      <td>28.1</td>
      <td>0.167</td>
      <td>21</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



# groupby


```python
from pandas import read_csv
filename = "diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
class_counts = data.groupby('class').size()
print(class_counts)

```

    class
    0          500
    1          268
    Outcome      1
    dtype: int64
    

# correlations


```python
import pandas as pd
from pandas import read_csv
from pandas import set_option

# Filename
filename = "diabetes.csv"

# Column names
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Read CSV file, skipping the original header
data = read_csv(filename, names=names, header=0)

# Set display options
set_option('display.width', 100)
set_option('display.precision', 3)

# Calculate correlations
correlations = data.corr(method='pearson')

# Print the correlations
print(correlations)

```

            preg   plas   pres   skin   test   mass   pedi    age  class
    preg   1.000  0.129  0.141 -0.082 -0.074  0.018 -0.034  0.544  0.222
    plas   0.129  1.000  0.153  0.057  0.331  0.221  0.137  0.264  0.467
    pres   0.141  0.153  1.000  0.207  0.089  0.282  0.041  0.240  0.065
    skin  -0.082  0.057  0.207  1.000  0.437  0.393  0.184 -0.114  0.075
    test  -0.074  0.331  0.089  0.437  1.000  0.198  0.185 -0.042  0.131
    mass   0.018  0.221  0.282  0.393  0.198  1.000  0.141  0.036  0.293
    pedi  -0.034  0.137  0.041  0.184  0.185  0.141  1.000  0.034  0.174
    age    0.544  0.264  0.240 -0.114 -0.042  0.036  0.034  1.000  0.238
    class  0.222  0.467  0.065  0.075  0.131  0.293  0.174  0.238  1.000
    
