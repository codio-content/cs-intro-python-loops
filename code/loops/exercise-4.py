import turtle # keep this line of code

t = turtle.Turtle()

# Your code goes here

for outer_loop in range(4):
  for inner_loop in range(4):
    t.forward(50)
    t.rt(90)
  t.forward(100)
for last_loop in range(4):
  t.forward(50)
  t.rt(90)

turtle.mainloop() #keep this line of code