############################
#Python3
#sting 
############################strip 
s="      mohmedhesham      "
print(s.strip())   #mohmedhesham
print(s.rstrip())  #      mohmedhesham
print(s.lstrip())  #mohmedhesham 

############################strip
s="######mohmedhesham#######"
print(s.strip('#'))   #mohmedhesham
print(s.rstrip('#'))  #######mohmedhesham
print(s.lstrip('#'))  #mohmedhesham#######

############################
s ="abdullah elsaid"
print("Hello "+s.title()+'!')  #Hello Abdullah Elsaid!

############################
print("pyhton")      #pyhton
print("\t\tpython")  #		  python

############################title
b='i love 2d array'
print(b.title())   #I Love 2D Array

###########################capitalize
b='i love 2d array'
print(b.capitalize())#I love 2d array

###########################zfill
a,b,c,d='1','11','111','1111'
print(a.zfill(4))  #0001
print(b.zfill(4))  #0011
print(c.zfill(4))  #0111
print(d.zfill(4))  #1111

###########################
message = "One of Python's strengths is its diverse community." 
print(message)   #One of Python's strengths is its diverse community.

###########################split
s="I Love python and php and mysql"
print(s.split())        #['I', 'Love', 'python', 'and', 'php', 'and', 'mysql']
print(s.split(' ',2))   #['I', 'Love', 'python and php and mysql']
print(s.rsplit(' ',2))  #['I Love python and php', 'and', 'mysql']

s="I-Love-python-and-php-and-mysql"
print(s.split('-'))      #['I', 'Love', 'python', 'and', 'php', 'and', 'mysql']
print(s.split('-',2))    #['I', 'Love', 'python-and-php-and-mysql']
print(s.rsplit('-',2))   #['I-Love-python-and-php', 'and', 'mysql']
s=s.split('-')
print(s)          #['I', 'Love', 'python', 'and', 'php', 'and', 'mysql']

###########################center
s="osama"
print(s.center(8,'@'))   #@osama@@

###########################count 
s="I love python and php becuse php it's good"
print(s.count('php'))      #2
print(s.count('php',0,25)) #1

###########################swapcase
s="AbdooSaid"
print(s.swapcase())   #aBDOOsAID
s="aBDOOsaid"
print(s.swapcase())   #AbdooSAID

###########################StartWith 
s="I love python"
print(s.startswith('I'))        #True
print(s.startswith('I',7,12))   #False 

###########################endwith
s="I love python"
print(s.endswith('n'))      #True
print(s.endswith('e',0,6))  #True

##########################index
s="I love python"
print(s.index('l',0,7))    #2

##########################find 
s="I love python"
print(s.find('lo'))   #2

#########################rjust ljust 
s="python"
print(s.ljust(16,'#'))    #python##########
print(s.rjust(16,'#'))    # ##########python

########################splitlines
s="""python
c++
ruby 
"""
print(s.splitlines())   #['python', 'c++', 'ruby ']
s="python\nc++\nruby"
print(s.splitlines())   #['python', 'c++', 'ruby']

########################expandtabs
s="hello\tword\tI\tpython"
print(s.expandtabs(2))  #hello word  I python

########################checkString
s="I Love Python 3G"
print(s.istitle())  #True

s="I Love Python 3g"
print(s.istitle())  #False

s="i love python"
print(s.islower())  #True

#check valid name or not 

s="osama_py"
print(s.isidentifier()) #True

s="osamapy11"
print(s.isidentifier()) #True 

s="osama-py"
print(s.isidentifier()) #False

s="aaaabbb"
print(s.isalpha())  #True

s="aaaabbb11"
print(s.isalpha())  #False 

s="aaaabbb"
print(s.isalnum())  #True

s="aaaabbb11"
print(s.isalnum())  #True

########################replace 
s="Hello one two three one one "
print(s.replace('one','1'))    #Hello 1 two three 1 1 

s="Hello one two three one one "
print(s.replace('one','1',2))  #Hello 1 two three 1 one 

########################join(iterable)
myList=["Abdullah","Elsaid","Ebrahim"]
print('-'.join(myList))  #Abdullah-Elsaid-Ebrahim
print(' '.join(myList))  #Abdullah Elsaid Ebrahim
print(', '.join(myList)) #Abdullah, Elsaid, Ebrahim
print(type(', '.join(myList))) #<class 'str'>

#########################
