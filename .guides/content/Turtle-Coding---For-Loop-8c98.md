----------
Using your knowledge of for loops, try and recreate the images you see below. Remember, click on the tab that reads **Preview https/...** to see your output. Close the window with the turtle output to stop your program.

<details>
  <summary><strong>Customize your turtle</strong></summary>
  <ul>
    <li><code>t.color('red')</code> - Takes a string for the <a href="https://www.w3schools.com/colors/colors_names.asp">color</a></li>
    <li><code>t.shape('turtle')</code> - Takes one of the following strings <code>'turtle'</code>, <code>'circle'</code>, <code>'square'</code>, <code>'arrow'</code>, <code>'classic'</code>, or <code>'triangle'</code>.</li>
    <li><code>t.pensize(4)</code> - Takes a positive number</li>
    <li><code>t.speed(1)</code> - Takes a number in the range 0..10</li>
  </ul>
</details>

### Challenge 1
![Turtle Challenge 1](.guides/images/turtle-challenge-1.png)
{Try it}(bash .guides/bg.sh python3 code/loops/playground-turtle-2.py)

<details>
  <summary><strong>Hint</strong></summary>
  The trick is to find the pattern and then repeat it four times. The pattern is to go forward and then make a smaller square (with right turns) at the end. The pattern should look something like this: <img src=".guides/images/turtle-graphics-pattern-1.png"/><details><summary><strong>Hint 2</strong></summary>If you are stil stuck, use these lines of code to see if it will help you complete the pattern: <code>t.forward(80)</code>, <code>t.rt(90)</code>, <code>t.forward(20)</code>.
  </details>
</details>

### Challenge 2
![Turtle Challenge 2](.guides/images/turtle-challenge-2.png)
{Try it}(bash .guides/bg.sh python3 code/loops/playground-turtle-2.py 2)

<details>
  <summary><strong>Hint</strong></summary>
  Since a circle has 360 degrees, you will need a loop that repeats 360 times. Be careful about how far the turtle walks. The circle can get very big, very quickly.<details><summary><strong>Hint 2</strong></summary>If you are stil stuck, use these lines of code to see if it will help you complete the pattern: <code>t.rt(1)</code>.
  </details>
</details>

### Challenge 3
![Turtle Challenge 3](.guides/images/turtle-challenge-3.png)
{Try it}(bash .guides/bg.sh python3 code/loops/playground-turtle-2.py 3)

<details>
  <summary><strong>Hint</strong></summary>
  The pattern here is to move forward and make a right turn. The trick is, the amount to move forward needs to get bigger as the loop advances. Think of some operators that you can use to make the loop variable get a little bit bigger each iteration.<details><summary><strong>Hint 2</strong></summary>If you are still stuck, multiply the value of <code>i</code> by another number to generate the distance the turtle needs to move forward.
  </details>
</details>

{Check It!|assessment}(fill-in-the-blanks-1775886763)
