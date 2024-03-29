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

This introduction was taken directly from the project brief for ease of use and review purposes

## Instructions 
This project can be run from the windows command prompt, however it was developed using a vitual instance of Debian.

Firstly the user must clone this repository onto their desktop into a new folder. Once all the files are downloaded, navigate to the programs root directory.
```
git clone https://github.com/OwenKe11y/graph-theory-project
cd graph-theory-project
```
the program can be ran by executing the following code
```
python3 regex.py
```
From here a menu will display, prompting the user for an input from a menu. The user has 3 options. They are to:
* Input a text file, a text file is provided named **"input.txt"**
* Enter a regular expression.
* Exit the program.

![Menu](https://github.com/OwenKe11y/graph-theory-labs/blob/main/images/MenuGT.png?raw=true)

The inputted regular expression will automatically search through the inputted file. If no file is entered, the program will prompt the user they have failed to provide an input file.

The sample input file contains the entirety of the novel "Frankenstein" by Mary Shelley. A sample regular expression would be the following:
```
m.o*.d
```
This searches the entirey of the book for the word "mood" and outputs the number of matches.





## Algorithm Explaination
My program operates using two main algorithms to process an inputted regular expression, those two being the shunting yard algorithm and thompsons construction. These two algorithms were focused heavily upon in my lab content and is the backbone to this script. Here, I will explain step by step the processes my program does at each given point and explain how these two algorithms apply.

### Program start and input
When the script is executed, the user is prompted to input a choice for the menu. Since a file hasn't been selected, the user only has option 1 and 0 to select from, as option 1 inputs a text file and option 0 exits the program. Once an input has been made for the text file, the inputted file is taken in by the next function which allows the user to then input a regular expression to search through that text file. Once the user has pressed enter, the main algorithm is called and the user recieves a match or no match.

### The Algorithm
#### Shunting Yard Algorithm 
When the user enters an input for a regular expression, the shunt() function is called which takes in an infix expression. The shunt function converts infix expressions to a postfix expression. It loops through the input one character at a time to look for an operator that hold precedence; being Concatenation( . ), Kleene star( * ) or Union( | ). If the input was none one of those characters it pushes it to the output, however if the input was one of those characaters, it pushes the operater to the operator stack. After reading the expression, pop the operators off the stack and add them to the output. Here is a visual representation of what the shunting yard algorithm does:

![Shunting](https://github.com/OwenKe11y/graph-theory-labs/blob/main/images/Shunting.png?raw=true)

#### Thompsons Construction
Once a postfix has been constructed, the next step is to use that postfix expression and construct a Non-deterministic Finite Automaton or NFA. This NFA will recognise the same language as the regular expression. This algorithm does different things to construct the NFA depending on the character that was read. The function loops over the expression character by character to determine if there is an operator or a non-special character.  
* For a non-special character, it pushes the following fragment to the stack. 
* For concatination,  pop two fragments from the stack and push the following instead.
* For Kleene star, pop a fragment from the stack and push the following instead.
* For Union, pop a fragment from the stack and push the following instead.

![Thomspon](https://github.com/OwenKe11y/graph-theory-labs/blob/main/images/Thompsons.PNG?raw=true)

After reading the expression, the output is an object which contains the NFA.

### Matching
After constructing the NFA, this can be used for our match method. For every word in every line of text in our text file, we call match to return whether or not we've found a match. In order to cycle through each word, we deconstruct the line into each word using the [.split()](https://www.w3schools.com/python/ref_string_split.asp) method to find words seperated by spaces. If the match returns true, add it to a counter. Once the match has finished executing, a counter for the number of matches can be found. 

## Project Research and Development
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

#### Putting it all together with the match function 
After reviewing the latest lab video that was uploaded, I adapted my code to include the match functionality. With this, the converted NFA using the shunting yard algorithm and thompsons consrtuction would be compared to the file that was inputted, outputting if the regular expression matched with any text in the file. However, many problems arose when implementing this function and I ha dto rework how my menu operated. After an embarrassing amount of time attempting to fix the bug by double checking the 3 latest labs, I finally managed to make the match function work, thus completing the main functionality of the project.

#### Extras 
A few extra bit of functionality were added to my program to make it feel unique and fleshed out. Heres a quick list of small things I've added:
* Error handling on menu 
* Error handling for inputting a non existant file 
* Outputs the number of matches when searching with a regex
* Console gets cleared so the CLI doesn't get cluttered after each input. This works for UNIX based systems aswell as Windows.


## Answered Questions
### What is a regular expression?

During the duration of this Graph Theory module, one of the key components to completing the project was to understand the term “regular expression” and what it means in relation to our project.

Before we could even attempt our script file, a solid understanding of regular expressions was needed to produce a high-quality script. Using resources from online websites as well as the lecture videos provided in the course, I managed to construct a reasonable understanding of regular expressions and how to apply it to my project. 

Essentially, a regular expression, or regex, is a string of text that allows you to create patterns that help match, locate, and manage text [[1]](#references). Each character in a regular expression is either a metacharacter which has a special meaning, or a regular character that has a literal meaning. Each of these characters is a character in the string describing its pattern.

A simple example of this would be the following:
If we want to find a reference to a particular year, say 1877, in a document, it’s easy enough to search for that single date. But if we want to find any references to years in latter half of the 19th century, it is impractical to search several dozen times for 1850, 1851, 1852, etc., in turn. By using regular expressions we can use a concise pattern like “18[5-9][0-9]” to effectively match any year from 1850 to 1899 [[2]](#references). 

The history of regular expressions originates in 1951, where mathematician Stephen Cole Kleene described a model, detailing how the human nervous system works, with an algebra notation that he called regular sets/regular expression. Regular expressions first use in the field of computer science dates to 1968, where Ken Thompson a mathematician, implemented regular expression inside the text editor called ed. Alfred Aho, a computer scientist, extended Ken Thompson’s ed text editor with new functionalities and modified syntax named egrep — extended grep. His program was able to translate any regular expression to a deterministic finite automaton [[3]](#references). Put simply, a deterministic finite automaton or DFA is a finite-state machine that accepts or rejects a given string of symbols. 

The formation of regular expressions had a huge impact on the computing world, as they used in any scenario that benefits from full or partial pattern matches on strings. Some of the common use cases for regular expressions include:
* verify the structure of strings
*	extract substrings form structured strings
*	search / replace / rearrange parts of the string
*	split a string into tokens

All of these come up regularly when doing data preparation work [[4]](#references). 

For our Graph Theory project, we were tasked with writing a program in the Python 3 programming language to search a text file using a regular expression. Our program must take in a regular expression to search a text file and out put the lines of the file matching the regular expression.

Having learned that a regular expression is string of text used to create patterns to help match text, I was confident knowing how to apply it to my script file. 
 
### How do regular expressions differ across implementations?
As stated above, my definition of a regular expression would be "is a string of text that allows you to create patterns that help match, locate, and manage text. Each character in a regular expression is either a metacharacter which has a special meaning, or a regular character that has a literal meaning. Each of these characters is a character in the string describing its pattern." However, depending on the language or the program, regular expressions can differ between them.

Here, I’ll explain how regular expressions differ between implementations of programs and languages and give examples of them.
The differences in implementations are usually the way special characters are handled and occasionally substituted. This means that a special character inside one implementation may be slightly, or even drastically different to how it handles in another [[5]](#references).

A quick example of this would be the differences between Visual Studio Code and Visual Studio. If we were given the following string:
```
line1
line2
```
And given the following regex:
```
^(.+)$
```
With the following replacement:
```
$1
```
The regex’s operation means find something that starts with any character with one or more occurrences. The $number language element includes the last substring matched by the number capturing group in the replacement string, where number is the index of the capturing group.

In VSCode, the output would be 
```
"line1",
"line2",
```
However, in Visual Studio the output would be
```
"line1
",
"line2
",
```
This is because of the slight difference in both regex engines. VSCode uses a different flavour of regex compared to Visual Studios .NET regex engine. In VSCode regex patterns, a dot . matches any char but any **line break** character. In .NET regex used in Visual Studio, a dot matches any char but a **newline** character. 

Very slight discrepancies exist on every platform that uses regular expressions and there are many many more examples of slight differences between platforms and languages. However, some regex's meanings can be drastically different to more convential regex engines, such is the case with Vim and PERL regex engines.

Taken directly from the Vim documentation [[6]](#references), it states:
```
Vim and Perl handle newline characters inside a string a bit differently:

In Perl, ^ and $ only match at the very beginning and end of the text,
by default, but you can set the 'm' flag, which lets them match at
embedded newlines as well.

On the other hand, Vim's ^ and $ always match at embedded newlines, and
you get two separate atoms, \%^ and \%$, which only match at the very
start and end of the text, respectively.  Vim solves the second problem
by giving you the \_ "modifier":  put it in front of a . or a character
class, and they will match newlines as well.
```
In conclusion, regex's are not predefined and there is not an unanimous agreement on the syntex of regex's. Every language's regex engine may be based on anothers regex engine or every platform may take features from another. The fact is that not every regex engine is the same. 

### Can all formal languages be encoded as regular expressions?
Before we can answer this question, we must first identify what a formal language is. 

A formal language is a mathematical construction. They are syntax without meaning. It is meant to study the structure of sets of strings defined formally, without usually attaching meaning to those strings. 

This concept makes up the basis of a Turing machine. Alan Turing, created a concept known as an automaton which is a hypothetical machine. A Turing machine is an automaton which is the simplist form of computing which Turing could come up with. The function of a Turing Machine is that it takes in an input, change one symbol at a time from that input and moves left or right with a finite set of rules. 


<img src="https://github.com/OwenKe11y/graph-theory-labs/blob/main/images/TuringMachine.png?raw=true" alt="Machine" width="400" height="250">

Illustration of a Turing machine

The connection between these two concepts is that Turing machines can be used to _define_ formal languages.

For a language, L, if there exists a Turing machine that halts if and only if its input belongs to L, then the language is called Turing-recognizable. Some languages cannot be defined by any Turing machine, which means they are not-computable - no finite process can decide whether an arbitrary string belongs to the language or not.

Formal languages are not the same as Turing machines, but the Turing recognizability does have an interesting place in the study of formal languages. In the [Chomsky hierarchy](https://en.wikipedia.org/wiki/Chomsky_hierarchy#:~:text=In%20formal%20language%20theory%2C%20computer,by%20Noam%20Chomsky%20in%201956.), a Type-0 language is a language that can be enumerated by any formal grammar, and this turns out to be equivalent to being recognizable by a Turing machine. Formal grammars and Turing machines are just two of many models of computation that are all equally powerful.

<img src="https://github.com/OwenKe11y/graph-theory-labs/blob/main/images/Alan.jpg?raw=true" alt="Turing" width="250" height="250">

Alan Turning

#### So the question remains, can formal languages, or Turing machines be encoded with regular expressions? 
All this means is are regular expressions a Turing complete language? Regular expressions are not Turing complete. This is because regular expressions can be turned into a DFA which I explained earlier in this document. DFAs are not Turing complete because as an input string travels between two states, its letters are used up and can never be accessed again. Some key aspects of a Turing Machine are that it can move back and forth and access parts of the input string that it has already visited similar to how programs can write to memory. Anything that a DFA can do, a Turing machine can do. But a Turing machine can determine much more sophisticated languages than a DFA with its added capabilities, so DFAs are not Turing complete.

In conclusion, not all formal languages can be encoded as regular expressions. 

## References 
**[1]** Hope, C., 2020. What is a Regex (Regular Expression)?. 
[online] Computerhope.com. Available at: <https://www.computerhope.com/jargon/r/regex.htm> [Accessed 25 April 2021].

**[2]** Knox, D., 2013. Understanding Regular Expressions. [online] 
Programminghistorian.org. Available at: <https://programminghistorian.org/en/lessons/understanding-regular-expressions> [Accessed 25 April 2021].

**[3]** Murugan, M., 2019. Regular Expression: Part 1. [online] 
Medium. Available at: <https://medium.com/@minisha.mit/regular-expression-part-1-8d75128f6274> [Accessed 25 April 2021].

**[4]** Chodnicki, S., 2019. Everything you need to know about Regular Expressions. [online] 
Medium. Available at: <https://towardsdatascience.com/everything-you-need-to-know-about-regular-expressions-8f622fe10b03> [Accessed 25 April 2021].

**[5]** https://stackoverflow.com/questions/20919403/difference-between-and-in-python-regex

**[6]** http://vimdoc.sourceforge.net/htmldoc/pattern.html#perl-patterns

## Resources 
Here is a list of resources I used to complete this project.

Learing about strings in python:
https://docs.python.org/2/reference/lexical_analysis.html#string-literals

Reading a file:
https://www.pythontutorial.net/python-basics/python-read-text-file/ 

Creating a Menu:
https://www.youtube.com/watch?v=63nw00JqHo0

Clearing the screen, depending on the os:
https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.

Seperating each word:
https://www.w3schools.com/python/ref_string_split.asp

Regex Spread Sheet:
http://www.greenend.org.uk/rjk/tech/regexp.html

Regex Flavour Comparison:
http://www.regular-expressions.info/refflavors.html

Are Turing machines and formal languages the same?:
https://cs.stackexchange.com/questions/62668/are-turing-machines-and-formal-languages-the-same-mathematical-object#

Are regular expressions Turing Complete?:
https://www.quora.com/Are-regular-expressions-a-Turing-complete-language
