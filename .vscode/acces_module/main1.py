#main.py module to import sting_utils module
import os,sys
from os.path import dirname,join,abspath
shivi=abspath(join(dirname(__file__),'..'))
sys.path.insert(0,shivi)
from assignment_questions import string_utils
print(" capitalizing string :",string_utils.make_capital('shivani virang'))
print('revrsing the given string :',string_utils.reverse("shivani"))