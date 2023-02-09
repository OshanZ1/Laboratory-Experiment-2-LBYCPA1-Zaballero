#Display of TotalTax for the user input
def calculate(amount, percent):
    print("Total Tax applicable is" , (amount * percent / 100))
    return 0
  
   #function for calculating the tax rate for each annual income
def calculate_income_tax(monthlyinc):
     
    if monthlyinc <= 250000:
        print("Total Tax applicable is",(monthlyinc))
        return 0

    elif monthlyinc <= 400000:  
        return calculate(monthlyinc -  250000, 15)

    elif monthlyinc <= 800000:
        return calculate(monthlyinc -  400000, 20) + 22500

    elif monthlyinc <= 2000000:
        return calculate(monthlyinc - 800000, 25) + 102500
        
    elif monthlyinc <= 8000000:
        return calculate(monthlyinc - 2000000, 30) + 402500
        
    elif monthlyinc > 8000000:
        return calculate(monthlyinc - 8000000, 35) + 2202500

#user input
monthlyinc = input ("Enter your monthly income: ")
calculate_income_tax(float(monthlyinc))