def load_file(program_file):
    program_file = open(program_file,'r')
    program_code = program_file.read()
    return program_code

