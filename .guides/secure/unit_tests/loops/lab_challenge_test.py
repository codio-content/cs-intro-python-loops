import os
import subprocess
import sys

path = "code/loops"
file = "lab-challenge.py"
student_code = os.path.join(path, file)
expected_output = """XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX
XOXOXOXO
OXOXOXOX"""

def check_output(file):
  student_output = subprocess.check_output(["python3", file]).rstrip()
  if student_output.decode("utf-8") == expected_output:
    return True
  else:
    return False
  
def has_loop(file):
  loop = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "for" in line:
        loop = True
    
  return loop

def has_if(file):
  cond = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if 'if' in line:
        cond = True
    
  return cond

def has_end(file):
  end = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if 'end=' in line:
        end = True
    
  return end
  
if not has_loop(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use a looping structre.")

if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not print the chessboard of 'X' and 'O' like in the example above.")

if not has_if(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use a decision structure.")
  
if not has_end(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did remove newline characters with <code>end=''</code>.")

if has_loop(student_code) and has_end(student_code) and has_if(student_code) and check_output(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)

