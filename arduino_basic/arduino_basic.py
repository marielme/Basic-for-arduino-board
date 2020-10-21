"""
    arduino_basic

    The file with the basic code is loaded.
    Then it is parsed to be interpreted by python. And finally it is running
    at the arduino board, and depending of the coding could be interact throught 
    the terminal.

"""
from .basic_parser import program_parser, cname
from .arduino_board import Arduino_Board
from .basic_tools import load_file
import time

class ArBasProgram():
    """
    ArBasProgram is a Basic interpreter for Arduino board.

    This class have the following methods:
    * parse_code --> parse Basic code.
    * load_file  --> load the program with Basic.
    * run        --> run a Basic program in the arduino.
    """

    def __init__(self, program=None, arduino=None):
        self.code = None
        self.program = None
        self.variables = {}
        self.arduino_board = Arduino_Board(arduino)

    def parse_code(self):
    """
    Parse the code.

    The code in Basic is parse, create AST graph object and it keeped in self.program.
    """
        self.program =  program_parser(self.code)

    def load_file(self, file_name=None):
    """
    Load the file with Basic code and call the method parse.

    The load Basic code is loaded at self.code and then parse it.

    Parameters
    ----------
    commands : list of commads
       list of basic language commads

    """
        self.code = load_file(file_name)
        self.parse_code()

    def run(self, commands=None):
    """
    run each Basic command in the arduino or in computer terminal.

    Parameters
    ----------
    commands : list of commads
       list of basic language commads

    """
        if not commands:
            commands = self.program.commands

        for command in commands:
            command_name = cname(command)

            if command_name == "var_STRING":
                self.variables[command.var_name]= {"value":command.var_value, "type": "STRING"}
            elif command_name == "var_INTEGER":
                self.variables[command.var_name]= {"value":command.var_value, "type": "INTEGER"}
            elif command_name == "BYTE":
                self.variables[command.var_name]= {"value":command.var_value, "type": "BYTE"}
            elif command_name == "DEBUG":
                print(command.text)
            elif command_name == "PAUSE":
                time.sleep(command.pause_time * 0.01)
            elif command_name == "HIGH":
                self.arduino_board.high(command.pin)
            elif command_name == "LOW":
                self.arduino_board.low(command.pin)
            elif command_name == "DO":
                while True:
                    self.run(command.commands)

            elif command_name == "FOR":
                for count in range(command.count_init, command.count_final+1):
                    self.variables[command.counter_name]= {"value":count, "type": "INTEGER"}
                    self.run(command.commands)

            elif command_name == "READPIN":
                self.variables[command.var_name]= self.arduino_board.readpin(command.pin)

   

