# Ardunio Basic Language

This project try to bring a very basic support of Basic Language for Arduino Boards.

You can create your Basic file, with arduino extendended commands (abp, arduino basic program).

To run "my_basic_program.abp", write in the command line of the terminal:

🚀 
> python run_bas_in_arduino.py my_basic_program.abp

At the repository, there is a example of a Basic program called "demo.abp"

Time to try 👩🏻‍💻 👨‍💻 👾 !!

## Commands Supported:

  HIGH pin_number

  LOW pin_number

  DEBUG text_to_show_at_terminal

  PAUSE pause_time_in_ms

  READPIN pin_number var_name = 'value'

  Loops:

    DO  
    | commands
    LOOP

    FOR counter_name= 'value' = count_init TO count_final 
    | commands
    NEXT
  
### define variables:

  STRING var_name = 'value'

  INTEGER var_name = value

  BYTE var_name = value


### requirements

install the dependencies: 

> pip install -r requirements.txt

  Python      https://www.python.org/downloads/

  textx       https://pypi.org/project/textX/

  pyfirmata   https://pypi.org/project/pyFirmata/

### MIT License

Copyright 2020 Maria de los Angeles Martinez

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




