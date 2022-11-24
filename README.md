# Tower of Hanoi

This article is about the math disc game.

The Tower of Hanoi (also called The problem of Benares Temple or Tower of Brahma or Lucas' Tower and sometimes pluralized as Towers, or simply pyramid puzzle) is a mathematical game or puzzle consisting of three rods and a number of disks of various diameters, which can slide onto any rod. The puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape. The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:

Only one disk may be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
No disk may be placed on top of a disk that is smaller than it.
With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.

## Origins
The puzzle was introduced to the West by the French mathematician Édouard Lucas in 1883. Numerous myths regarding the ancient and mystical nature of the puzzle popped up almost immediately,including one about an Indian temple in Kashi Vishwanath containing a large room with three time-worn posts in it, surrounded by 64 golden disks. Acting out the command of an ancient prophecy, Brahmin priests have been moving these disks in accordance with the immutable rules of Brahma since that time. The puzzle is therefore also known as the Tower of Brahma. According to the legend, when the last move of the puzzle is completed, the world will end.

If the legend were true, and if the priests were able to move disks at a rate of one per second, using the smallest number of moves, it would take them 264 − 1 seconds or roughly 585 billion years to finish, which is about 42 times the current age of the universe.

There are many variations on this legend. For instance, in some tellings, the temple is a monastery, and the priests are monks. The temple or monastery may be in various locales including Hanoi, and may be associated with any religion. In some versions, other elements are introduced, such as the fact that the tower was created at the beginning of the world, or that the priests or monks may make only one move per day.

# Solution
The puzzle can be played with any number of disks, although many toy versions have around 7 to 9 of them. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2n − 1, where n is the number of disks.

Iterative solution

Animation of an iterative algorithm solving 6-disk problem
A simple solution for the toy puzzle is to alternate moves between the smallest piece and a non-smallest piece. When moving the smallest piece, always move it to the next position in the same direction (to the right if the starting number of pieces is even, to the left if the starting number of pieces is odd). If there is no tower position in the chosen direction, move the piece to the opposite end, but then continue to move in the correct direction. For example, if you started with three pieces, you would move the smallest piece to the opposite end, then continue in the left direction after that. When the turn is to move the non-smallest piece, there is only one legal move. Doing this will complete the puzzle in the fewest moves.

Simpler statement of iterative solution
For an even number of disks:

make the legal move between pegs A and B (in either direction),
make the legal move between pegs A and C (in either direction),
make the legal move between pegs B and C (in either direction),
repeat until complete.
For an odd number of disks:

make the legal move between pegs A and C (in either direction),
make the legal move between pegs A and B (in either direction),
make the legal move between pegs B and C (in either direction),
repeat until complete.
In each case, a total of 2n − 1 moves are made.

Equivalent iterative solution
Another way to generate the unique optimal iterative solution:

Number the disks 1 through n (largest to smallest).

If n is odd, the first move is from peg A to peg C.
If n is even, the first move is from peg A to peg B.
Now, add these constraints:

No odd disk may be placed directly on an odd disk.
No even disk may be placed directly on an even disk.
There will sometimes be two possible pegs: one will have disks, and the other will be empty. Place the disk on the non-empty peg.
Never move a disk twice in succession.
Considering those constraints after the first move, there is only one legal move at every subsequent turn.

The sequence of these unique moves is an optimal solution to the problem equivalent to the iterative solution described above.

Recursive solution

Illustration of a recursive solution for the Towers of Hanoi puzzle with 4 disks. In the SVG file, click a grey button to expand or collapse it
The key to solving a problem recursively is to recognize that it can be broken down into a collection of smaller sub-problems, to each of which that same general solving procedure that we are seeking applies, and the total solution is then found in some simple way from those sub-problems' solutions. Each of these created sub-problems being "smaller" guarantees that the base case(s) will eventually be reached. Thence, for the Towers of Hanoi:

label the pegs A, B, C,
let n be the total number of disks,
number the disks from 1 (smallest, topmost) to n (largest, bottom-most).
Assuming all n disks are distributed in valid arrangements among the pegs; assuming there are m top disks on a source peg, and all the rest of the disks are larger than m, so they can be safely ignored; to move m disks from a source peg to a target peg using a spare peg, without violating the rules:

Move m − 1 disks from the source to the spare peg, by the same general solving procedure. Rules are not violated, by assumption. This leaves the disk m as a top disk on the source peg.
Move the disk m from the source to the target peg, which is guaranteed to be a valid move, by the assumptions — a simple step.
Move the m − 1 disks that we have just placed on the spare, from the spare to the target peg by the same general solving procedure, so they are placed on top of the disk m without violating the rules.
The base case is to move 0 disks (in steps 1 and 3), that is, do nothing – which obviously doesn't violate the rules.
The full Tower of Hanoi solution then consists of moving n disks from the source peg A to the target peg C, using B as the spare peg.

This approach can be given a rigorous mathematical proof with mathematical induction and is often used as an example of recursion when teaching programming.

Logical analysis of the recursive solution
As in many mathematical puzzles, finding a solution is made easier by solving a slightly more general problem: how to move a tower of h (height) disks from a starting peg f = A (from) onto a destination peg t = C (to), B being the remaining third peg and assuming t ≠ f. First, observe that the problem is symmetric for permutations of the names of the pegs (symmetric group S3). If a solution is known moving from peg A to peg C, then, by renaming the pegs, the same solution can be used for every other choice of starting and destination peg. If there is only one disk (or even none at all), the problem is trivial. If h = 1, then simply move the disk from peg A to peg C. If h > 1, then somewhere along the sequence of moves, the largest disk must be moved from peg A to another peg, preferably to peg C. The only situation that allows this move is when all smaller h − 1 disks are on peg B. Hence, first all h − 1 smaller disks must go from A to B. Then move the largest disk and finally move the h − 1 smaller disks from peg B to peg C. The presence of the largest disk does not impede any move of the h − 1 smaller disks and can be temporarily ignored. Now the problem is reduced to moving h − 1 disks from one peg to another one, first from A to B and subsequently from B to C, but the same method can be used both times by renaming the pegs. The same strategy can be used to reduce the h − 1 problem to h − 2, h − 3, and so on until only one disk is left. This is called recursion. This algorithm can be schematized as follows.

Identify the disks in order of increasing size by the natural numbers from 0 up to but not including h. Hence disk 0 is the smallest one, and disk h − 1 the largest one.

The following is a procedure for moving a tower of h disks from a peg A onto a peg C, with B being the remaining third peg:

If h > 1, then first use this procedure to move the h − 1 smaller disks from peg A to peg B.
Now the largest disk, i.e. disk h can be moved from peg A to peg C.
If h > 1, then again use this procedure to move the h − 1 smaller disks from peg B to peg C.
By means of mathematical induction, it is easily proven that the above procedure requires the minimal number of moves possible and that the produced solution is the only one with this minimal number of moves. Using recurrence relations, the exact number of moves that this solution requires can be calculated by: {\displaystyle 2^{h}-1}2^h - 1. This result is obtained by noting that steps 1 and 3 take {\displaystyle T_{h-1}}T_{h-1} moves, and step 2 takes one move, giving {\displaystyle T_{h}=2T_{h-1}+1}T_h = 2T_{h-1} + 1.

# Description
This program is written in two programming languages

1- Python 
2- C

Python file:
The Python file is a game and does not run automatically

In this program, you enter the number of disks that you want to implement in the game, as well as the calculation of the number of movements and displacement of the disks
Then the game runs the number of inputs (disks) received from the user, and the user can start the game and move the disks.

*Library pyttsx3 created as a sound output for the user

C file:
After running the C file and entering the number of disks by the user, it runs automatically and moves the disks.


## Installation

Use the [pip] package manager to install the libraries.

```bash
pip install pygame
```
```bash
pip install pyttsx3
```

## Usage

```python
import pygame
import pyttsx3

## pyttsx3
Using the library pyttsx3 in two ways
import pyttsx3

text = ("text")
sound = pyttsx3.init()
sound.setProperty('range', 110)
sound.say(text)
sound.runAndWait()

or

import pyttsx3 as pt

pt.speak("text")
