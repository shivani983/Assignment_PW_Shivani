import os,sys
from os.path import dirname,join,abspath
file_path=abspath(join(dirname(__file__),'..'))
sys.path.insert(0,file_path)
from  assignment_questions import file_operations
print('reading the text file :',file_operations.read_file())
print('total_expenses :',file_operations.calculate_expenses())

