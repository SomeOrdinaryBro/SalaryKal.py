class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

PRHR = input('How Much Do You Get Paid Per-Hour: ')
HRSPD = input('How Many Hours do you Work Per-day: ')
PRDAYSAL = float(PRHR) * float(HRSPD) 

DYSLBR = input('How manys did you work this month? ')

MTHLYPAY = int(PRDAYSAL) * int(DYSLBR)

#NOT USING THIS SINCE IM USING A ASCII OUTPUT BELOW... SORT OF..
#print(PRDAYSAL, (color.GREEN + 'is your per-day salary' + color.END))
#print(MTHLYPAY, (color.GREEN + 'is your Monthly Salary' + color.END))

print("\n\n")
print("     Y O U R - S A L A R Y - D E T A I L S ")
print("==============================================")
print("YOUR PER-DAY SALARY: ", float(PRDAYSAL), (color.GREEN + 'is your per-day salary' + color.END))
print("YOUR MONTHLY SALARY: ", int(MTHLYPAY), (color.GREEN + 'is your Monthly Salary' + color.END))
print("==============================================")
