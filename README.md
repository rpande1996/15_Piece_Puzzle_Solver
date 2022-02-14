## 15_Piece_Puzzle_Solver
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
---
## Overview

This code utilizes BFS goal detection algorithm to solve a 15 piece puzzle with a user-inputted initial state.

For example:

The ideal/goal state would be: 
  
```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0
```
Which would be represented as follows:
  
  <img src="https://github.com/rpande1996/15_Piece_Puzzle_Solver/blob/main/media/visualization/Puzzle.png" width="240" height="240"/>

## Softwares

* Recommended IDE: PyCharm 2021.2

## Libraries

* Numpy 1.21.2
* OpenCV 3.4.8.29
* MoviePy 1.0.3

## Programming Languages

* Python 3.8.12

## License 

```
MIT License

Copyright (c) 2021 Rajan Pande

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
```
## Demo

Following demo is for following test case:

```
Enter input state: 5 1 2 3 6 7 11 4 13 9 10 8 14 15 0 12
```
[15 Piece Puzzle Solver: ](https://youtu.be/huRGa8ODMVQ)

<img src="https://github.com/rpande1996/15_Piece_Puzzle_Solver/blob/main/media/gif/Vis.gif" width="240" height="240"/>


## Build

```
git clone https://github.com/rpande1996/15_Piece_Puzzle_Solver
cd 15_Piece_Puzzle_Solver/src
python 15_Piece_Puzzle_Solver.py
```
Enter the following parameters (Order would be row-wise) :-
```
Enter input state:
```
For visualization, run:
```
python visualization.py
```
