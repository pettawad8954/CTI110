#determine the total profit sales 
# 2/5/19
# CTI-110 P2T1 - Sales Prediction
# Darrell Pettaway 

# get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#display the profit.
print('The profit is $', format(profit, ',.2f')) 
