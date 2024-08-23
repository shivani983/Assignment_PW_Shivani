import os,sys
from os.path import dirname,join,abspath
path=abspath(join(dirname(__file__),'..'))

sys.path.insert(0,path)

from assignment_questions import paragraph
print('reading the file:', paragraph.read_file())
