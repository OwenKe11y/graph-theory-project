# Graph Theory Project - G00366614 - Owen Kelly

## Introduction
For this Graph Theory project, a script file must be developed using the Python 3 programming language to search a text file using a regular expression. The program must take a regular expression and the name or path of the file as command line arguments and output the lines of the file matching the regular expression. 

This project must contain:
* A script.py file which contains the algorithm used to read a text file.
* A text file for the script to read. 
* A necessary README.md file describing the program, steps to run and test it, an explaination of the algorithm, and the answers to the following questions:
  * What is a regular expression?
  * How do regular expressions differ across implementations?
  * Can all formal languages be encoded as regular expressions?

Research has been conducted to understand the following:
* Understand and be able to code using the Python 3 programming language.
* Understand the term "regular expression" and how it can be applied to the project.
* Understand how to test the regular expression so that it works on a sensible example list of inputs

## Instructions 
...

## Algorithm Explaination
...


## Independent Research
This section details the thoughts and troubles the developer faced throughout the creation of this project. Here the developer logs key points that were learned to complete the project as well as answer the questions in the next section. The developers thoughts are detailed below.

#### Project start and preparation 
In preparation of this project, I made sure to completely understand the tast that has been given to me and started my README.md file to begin an introduction. I gave myself a list of clear aims to achieve whilst I make progress with the rest of this project. In order to gain a firm understanding of the topic, I rewatched lecture content explaining key consepts in relation to the tasks we were given such as understanding finite automata, concepts of formal languages and Turing machines and regular expressions

I also revisited lab content to aid me in completing the coding side of this project. All labs that I've accomplised can be found [here.](https://github.com/OwenKe11y/graph-theory-labs) Following the lecture and lab videos has given me the confidence and skills to start my project however there will be a few key consepts I'll have to figure out on my own in order to produce a well established document and script.

#### Python basics and file reading 
From lab content, the basics of python were explained well and the concept of indenting and running scripts were grasped quite easily. However, in order for my program to meet the requirements for the project brief I would have to learn how to handle files in Python and read them. Using resources online, I learned to successfully read a file into my program and to output the content onto the screen. An issue I came across was when the file would only be read if it was inside the project directory and the input that the program asks of the user cannot be a directory e.g "C:/User/Documents/". For the sake of this project, I had decided that this wasn't a huge issue, as we will be providing our own text document to accompany our project.

#### Menu Implementation 
After I got reading my file in working, I decided that having a menu for the user to choose from a list of options would suit my program well. This would include loading a file, inputting an infix regular expression to get a postfix and an option to use that postfix regular expression and search through a file. After a few videos being watch on the subject, my menu was implemented exactly how I wanted it.

#### Shunting yard Algorithm Implementation
Once the menu was implemented, next was to take an infix expression into a postfix expression. This was where my revision of the labs had aided me as we had covered how to convert an infix to postfix in lab content. I reviewed the code to make sure that everything inside the algorithm would apply nicely to my script. After that, I placed the code inside a function and added it to my menu.

#### Thompsons Construction Implementation 
Having implemented the shunting yard algorithm, I had to take the returned postfix expression and convert it into a Non-Finite Automata. Using Thompsons construction from the lab content, I added it into the same function as my shunting yard algorithm and used the same function call in the menu. 


## Answered Questions
### What is a regular expression?

### How do regular expressions differ across implementations?

### Can all formal languages be encoded as regular expressions?

## Conclusions 
...

## Resources 
Learing about strings in python:
https://docs.python.org/2/reference/lexical_analysis.html#string-literals

Reading a file:
https://www.pythontutorial.net/python-basics/python-read-text-file/ 

Creating a Menu:
https://www.youtube.com/watch?v=63nw00JqHo0

