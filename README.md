# bookbot

BookBot analyses books and prints statistical reports of the word and character usage found within.

BookBot is a guided project from [Boot.dev](https://www.boot.dev).

## Environment

BookBot requires a standard Python 3 installation.

## Usage

A command line call to the main Python file is required, followed by the path to the text file you wish to analyse. For example:

```console
user:~/bookbot$ python main.py <path-to-.txt-file>
```

### Example Output

```console
user:~/bookbot$ python main.py books/frankenstein.txt
============ BOOKBOT ============ 
Analyzing book found at books/frankenstein.txt...
----------- Word Count ---------- 
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

## Data

The [Project Gutenberg](https://www.gutenberg.org/) library provides free eBooks which can be downloaded as ```.txt``` files and analysed with BookBot.