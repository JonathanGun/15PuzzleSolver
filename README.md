# 15Puzzle Solver
made using Python 3 using Branch and Bound Algorithm

## Prerequisite
1. Python 3.5+

## Installing
1. Clone this repo

## Running
1. Go to src `cd src`
1. `python main.py -i [relative filepath]` or `python3 main.py` then input filepath

Example:
```
python main.py -i ../test/solve_easy.txt
```
-----
```
==== Initial matrix ====
board size: (4, 4)
empty at: (3, 0)
cost is: 15
┌───┬───┬───┬───┐
|5  |1  |7  |3  │
├───┼───┼───┼───┤
|9  |2  |11 |4  │
├───┼───┼───┼───┤
|13 |6  |15 |8  │
├───┼───┼───┼───┤
|0  |10 |14 |12 │
└───┴───┴───┴───┘

Kurang(1): 0
Kurang(2): 0
Kurang(3): 1
Kurang(4): 0
Kurang(5): 4
Kurang(6): 0
Kurang(7): 4
Kurang(8): 0
Kurang(9): 4
Kurang(10): 0
Kurang(11): 4
Kurang(12): 0
Kurang(13): 4
Kurang(14): 1
Kurang(15): 4
Kurang(16): 3
Total Kurang: 29
Total Kurang + X: 30

Time needed to run 'solveUtil'  15.61 ms
========= Steps =========
... (cut out for brevity)

Step 15:
┌───┬───┬───┬───┐
|1  |2  |3  |4  │
├───┼───┼───┼───┤
|5  |6  |7  |8  │
├───┼───┼───┼───┤
|9  |10 |11 |12 │
├───┼───┼───┼───┤
|13 |14 |15 |0  │
└───┴───┴───┴───┘

33 nodes generated to solve the puzzle
```

## Contributing
Feel free to do pull request

## Acknowledgement
This project is made to fulfill IF2211 Algorithm and Strategy.

This Algorithm is not best for solving this puzzle. Solving a medium puzzle may take an hour or more.
