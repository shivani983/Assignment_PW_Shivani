#main.py
import os ,sys
from os.path import dirname,join,abspath
parent_dir_path=abspath(join(dirname(__file__),'..'))
sys.path.insert(0,parent_dir_path)

from assignment_questions  import calculator
print("sum of the values:",calculator.addition(2,4,9))
print(" differnce  between numbers",calculator.subtract(4,6))
print(" product of the values:",calculator.multiply(2,8))
print('division value :',calculator.division(9,3))
