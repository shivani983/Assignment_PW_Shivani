#product_mangement module
import os,sys
from os.path import dirname,join,abspath
parent_path=abspath(join(dirname(__file__),'..'))
sys.path.insert(0,parent_path)
from ecommerce import order_processing
print(order_processing.take_orders(50))
print(order_processing.take_orders(-10))