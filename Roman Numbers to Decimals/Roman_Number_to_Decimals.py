def RomanNumeralToDecimal(romanNumeral):
    dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'0':0}
    ans=0
    romanNumeral=romanNumeral+'0'
    for i in range(len(romanNumeral)-1):
        if dic[romanNumeral[i]]<dic[romanNumeral[i+1]]:
            ans-=dic[romanNumeral[i]]
        else :
            ans+=dic[romanNumeral[i]]

    return  ans

Roman_number=input("Enter the Roman number: ")
print("The Decimal Number:",RomanNumeralToDecimal(Roman_number))