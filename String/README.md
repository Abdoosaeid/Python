# Python3(String)

## strip


```python
s="      helloPython,world     "
print(s.strip())    
print(s.rstrip())   
print(s.lstrip()) 
```

    helloPython,world
          helloPython,world
    helloPython,world     
    


```python
s="######helloPython,world#######"
print(s.strip('#'))    
print(s.rstrip('#'))   
print(s.lstrip('#'))   

```

    helloPython,world
    ######helloPython,world
    helloPython,world#######
    

##  title


```python
s ="abdullah elsaid"
print("Hello "+s.title()+'!')
b='i love 2d array'
print(b.title()) 
```

    Hello Abdullah Elsaid!
    I Love 2D Array
    

## \t


```python
print("pyhton")       
print("\t\tpython")
```

    pyhton
    		python
    

## capitalize


```python
b='i love 2d array'
print(b.capitalize()) 
```

    I love 2d array
    

## zfill


```python
a,b,c,d='1','11','111','1111'
print(a.zfill(4))   
print(b.zfill(4))  
print(c.zfill(4))   
print(d.zfill(4))
```

    0001
    0011
    0111
    1111
    


```python
message = "One of Python's strengths is its diverse community." 
print(message) 
```

    One of Python's strengths is its diverse community.
    

## split


```python
s="I Love python and php and mysql"
print(s.split())        
print(s.split(' ',2))   
print(s.rsplit(' ',2))  
print("###########")
s="I-Love-python-and-php-and-mysql"
print(s.split('-'))       
print(s.split('-',2))     
print(s.rsplit('-',2))    
s=s.split('-')
print(s)          

```

    ['I', 'Love', 'python', 'and', 'php', 'and', 'mysql']
    ['I', 'Love', 'python and php and mysql']
    ['I Love python and php', 'and', 'mysql']
    ###########
    ['I', 'Love', 'python', 'and', 'php', 'and', 'mysql']
    ['I', 'Love', 'python-and-php-and-mysql']
    ['I-Love-python-and-php', 'and', 'mysql']
    ['I', 'Love', 'python', 'and', 'php', 'and', 'mysql']
    

## center


```python
s="osama"
print(s.center(8,'@'))   #@osama@@
```

    @osama@@
    

## count


```python
s="I love python and php becuse php it's good"
print(s.count('php'))      
print(s.count('php',0,25)) 
```

    2
    1
    

## swapcase


```python
s="AbdooSaid"
print(s.swapcase())    
s="aBDOOsaid"
print(s.swapcase())    
```

    aBDOOsAID
    AbdooSAID
    

## StartWith


```python
s="I love python"
print(s.startswith('I'))         
print(s.startswith('I',7,12))
```

    True
    False
    

## endwith


```python
s="I love python"
print(s.endswith('n'))      
print(s.endswith('e',0,6))   
```

    True
    True
    

## index


```python
s="I love python"
print(s.index('l',0,7))  
```

    2
    

## find


```python
s="I love python"
print(s.find('lo'))
```

    2
    

## rjust ljust


```python
s="python"
print(s.ljust(16,'#'))     
print(s.rjust(16,'#'))     

```

    python##########
    ##########python
    

## splitlines


```python
s="""python
c++
ruby 
"""
print(s.splitlines())    
s="python\nc++\nruby"
print(s.splitlines())    
```

    ['python', 'c++', 'ruby ']
    ['python', 'c++', 'ruby']
    

## expandtabs


```python
s="hello\tword\tI\tpython"
print(s.expandtabs(2))
```

    hello word  I python
    

## checkString


```python
s="I Love Python 3G"
print(s.istitle())   

s="I Love Python 3g"
print(s.istitle())  

s="i love python"
print(s.islower())   

#check valid name or not 

s="osama_py"
print(s.isidentifier()) 

s="osamapy11"
print(s.isidentifier())  

s="osama-py"
print(s.isidentifier()) 

s="aaaabbb"
print(s.isalpha())  

s="aaaabbb11"
print(s.isalpha())   

s="aaaabbb"
print(s.isalnum())   

s="aaaabbb11"
print(s.isalnum())   
```

    True
    False
    True
    True
    True
    False
    True
    False
    True
    True
    

## replace


```python
s="Hello one two three one one "
print(s.replace('one','1'))     

s="Hello one two three one one "
print(s.replace('one','1',2))  
```

    Hello 1 two three 1 1 
    Hello 1 two three 1 one 
    

## join(iterable)


```python
myList=["Abdullah","Elsaid","Ebrahim"]
print('-'.join(myList))   
print(' '.join(myList))   
print(', '.join(myList))  
print(type(', '.join(myList))) 
```

    Abdullah-Elsaid-Ebrahim
    Abdullah Elsaid Ebrahim
    Abdullah, Elsaid, Ebrahim
    <class 'str'>
    

#  Old String Formatting


```python
name ="Abdullah"
age =36
rank= 10
print("My Name is: "+name)
print("My Name is: %s"%"Abdullah")
print("My Name is: %s" % name)
print("My name is: %s and My Age is: %d"%(name,age))
print("My name is: %s and My Age is: %d and My rank is: %f"%(name,age,rank))
```

    My Name is: Abdullah
    My Name is: Abdullah
    My Name is: Abdullah
    My name is: Abdullah and My Age is: 36
    My name is: Abdullah and My Age is: 36 and My rank is: 10.000000
    

# %s => String
# %d => Number
# %f => Float|


```python
n="Abdullah"
l="Python"
y=10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))
```

    My Name is Abdullah Iam Python Developer With 10 Years Exp
    

# Control Floating Point Number


```python
MyNumber=10
print("My Number is: %d"%MyNumber)
print("My Number is: %f"%MyNumber)
print("My Number is: %.2f"%MyNumber)
```

    My Number is: 10
    My Number is: 10.000000
    My Number is: 10.00
    

# Truncate String


```python
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)
```

    Message is Hello Peoples of Elzero Web School I Love You All
    Message is Hello
    

# New String Formatting


```python
name ="Abdullah"
age =36
rank= 10
print("My Name is: "+name)
print("My Name is: {}".format("Abdullah"))
print("My Name is: {}".format(name))
print("My name is: {} and My Age is: {}".format(name,age))
print("My name is: {:s} and My Age is: {:d} and My rank is: {:f}".format(name,age,rank))
```

    My Name is: Abdullah
    My Name is: Abdullah
    My Name is: Abdullah
    My name is: Abdullah and My Age is: 36
    My name is: Abdullah and My Age is: 36 and My rank is: 10.000000
    

# {:s} => String
# {:d} => Number
# {:f} => Float


```python
n="Abdullah"
l="Python"
y=10
print("My Name is {:s} Iam {:s} Developer With {:d} Years Exp".format(n, l, y))

MyNumber=10
print("My Number is: {}".format(MyNumber))
print("My Number is: {:f}".format(MyNumber))
print("My Number is: {:.2f}".format(MyNumber))
```

    My Name is Abdullah Iam Python Developer With 10 Years Exp
    My Number is: 10
    My Number is: 10.000000
    My Number is: 10.00
    

# Truncate String


```python
myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {:s}".format(myLongString))
print("Message is {:.5s}".format( myLongString))
print("Message is {:.13s}".format( myLongString))
```

    Message is Hello Peoples of Elzero Web School I Love You All
    Message is Hello
    Message is Hello Peoples
    

# Format Money


```python
MyMoney=7485934375
print("My Money Is: {:d}".format(MyMoney))
print("My Money Is: {:_d}".format(MyMoney))
print("My Money Is: {:,d}".format(MyMoney))
```

    My Money Is: 7485934375
    My Money Is: 7_485_934_375
    My Money Is: 7,485,934,375
    

# ReArrange Items


```python
a,b,c ="one","Two","Three"
print("Hi {}{}{}".format(a,b,c))
print("Hi {1}{2}{0}".format(a,b,c))
print("Hi {2}{0}{1}".format(a,b,c))

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))
```

    Hi oneTwoThree
    Hi TwoThreeone
    Hi ThreeoneTwo
    Hello 10 20 30
    Hello 20 30 10
    Hello 30.000000 10.000000 20.000000
    Hello 30.00 10.0000 20.00000
    

# Format in Version 3.6+


```python
myName = "Abdullah"
myAge = 19

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")
```

    My Name is : {myName} and My Age is : {myAge}
    My Name is : Abdullah and My Age is : 19
    
