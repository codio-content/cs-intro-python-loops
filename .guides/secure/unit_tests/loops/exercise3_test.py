import os
import subprocess
import sys

path = "code/loops"
file = "exercise-3.py"
student_code = os.path.join(path, file)
expected_output = 5050

def check_output(file):
  student_output = int(subprocess.check_output(["python3", file]).rstrip())
  if student_output == expected_output:
    return True
  else:
    return False
  
def while_true(file):
  loop = False
  with open(file, "r") as code_to_check:
    for line in code_to_check.readlines():
      if "while True:" in line:
        loop = True
    
  return loop
  
if not while_true(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not use: <code>while True:</code>")

if not check_output(student_code):
  print("<h2>Test did not pass</h2>")
  print("Program did not print 5050.")

if while_true(student_code) and check_output(student_code):
  print("<h2>Test passed!</h2>")
  sys.exit(0)
else:
  sys.exit(1)

