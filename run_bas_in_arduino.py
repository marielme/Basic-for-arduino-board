"""
    run_bas_in_arduino 

    >> python run_bas_in_arduino.py demo.abp

    The extencion .abp means arduino Basic program, it doesn't be use .bas, although it is Basic,
    because finally the code will be parse to be interpreted in python for an arduino.

    Parameters
    ----------
    arg1 : file with Basic code
    """
import sys

from arduino_basic import *  

if __name__ == "__main__":
    file_name = sys.argv[1]
    # file_name = "demo.abp", demo.abp is a file with basic commands
    if not file_name:
        print('You need a input file with basic')
        exit(0)

    # creating an instance of the class ArBasProgram.
    program = ArBasProgram()
    # call an instance load_file with basic code.
    program.load_file(file_name)
    # call an instance run.
    program.run()
    