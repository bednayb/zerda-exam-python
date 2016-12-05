# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

Check flowchart.png
### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

First of all we need to import the Tkinter into our file. It's a Graphical User Interface) package. After that we need to call it and make a canvas "screen" where we can add the screen height, width,background etc. Last we need to call a create_rectangle in the canvas like that:
canvas.create_rectangle(i, j, i+100, j+100, fill="black")

The i,j i+100 j+100 is the four cordinate of the rectangle.

### What does V stand for in MVC? [2p]
#### Your answer:

The MVC is a software design pattern. it has 3 big part M-model, V-view, C-controller. In the View you can manage the output, so what can see the user on his screen.
