""" 
We use the library textx for parse and the grammar is in arduino_basic/basic.tx.
"""

from textx import metamodel_from_file

basic_model = metamodel_from_file('arduino_basic/basic.tx')

def cname(o):
    return o.__class__.__name__

def program_parser(code):
    return basic_model.model_from_str(code)

  