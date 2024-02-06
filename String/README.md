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
    
