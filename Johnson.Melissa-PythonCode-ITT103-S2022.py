# Author: Melissa Johnson
#Date Created:April-25- 2022
# Course: ITT103
# Purpose: To create a program using python that can  accurately calculate the commission received by a salesperson at JamEx Limited.
sales_amount=int(input("please enter sales amount"))
class1  = int(input("please enter class"))
if class1 == 1:
    if sales_amount <= 1000:
        rate=0.06
    elif sales_amount > 1000 and sales_amount < 2000:
        rate=0.07
    else:
        rate=0.1
elif class1 == 2:
    if sales_amount <= 1000:
      rate=0.04
    else:
        rate=0.06
elif class1 == 3:
    rate=0.045
else:
    print('Error!')
commission_rec = sales_amount*rate
print(f'commission_rec= {commission_rec}')
