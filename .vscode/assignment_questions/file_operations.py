# file_operations module
expenses_list=[{'car':700000,'grocery':20000,'clothes':10000,'makeup and skincare':5000}]
with open('expenses.txt','w') as file:
  file.write(str(expenses_list))
  
    
def read_file():
    with open('expenses.txt','r') as file:
     return file.read()
def calculate_expenses(): 
  total_expenses=0
  for i in expenses_list:    
    for key,value in i.items():
      total_expenses+=value
    return total_expenses
      
 

