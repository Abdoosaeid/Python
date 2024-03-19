hight=float(input("Enter your height in centimeters: "))
weight=float(input("Enter your Weight in Kg: "))
BMI=weight/((hight/100)**2)

print("Your Body Mass Index is:",BMI)

if BMI > 1:
    if BMI < 16:
        print("Severe Thinness") 
    elif   BMI < 17:
        print("Moderate Thinness")  
    elif BMI < 18.5:
        print("Mild Thinness")       
    elif BMI < 25:
        print("Normal")        
    elif BMI < 30:
        print("Overweight")     
    elif BMI < 35:
        print("Obese Class I")
    elif BMI < 40:
        print("Obese Class II")
    else:
        print("Obese Class III")

else :
    ("enter valid details")        
        