# Birthday Paradox Probability Calculator

This repository contains two implementations of the famous **Birthday Problem**. The problem explores the counterintuitive probability that, in a set of $n$ randomly chosen people, at least two will share the same birthday.



## 🧠 The Mathematical Approaches

### 1. Forward Recursive Method (`birthday_problem (forward_method).py`)
This Python script calculates the probability directly using a recursive approach. 
* **Logic**: It calculates the probability of a match by considering the probability of the $(n-1)^{th}$ person and adding the incremental probability introduced by the $n^{th}$ person.
* **Feature**: User-interactive input to check specific group sizes.

### 2. Complementary "Not" Method (`Birthday_Problem_Not_Method.m`)
This MATLAB script uses the "Complementary Probability" approach, which is mathematically more efficient. 
* **Logic**: It calculates the probability that **no one** shares a birthday $P(\text{None})$ and subtracts it from 1:\
    $$P(\text{At least 2}) = 1 - \frac{365!}{(365-n)! \cdot 365^n}$$
* **Goal**: This script runs a `while` loop to find the minimum number of people $n$ required for the probability of shared birthdays to reach a specific threshold.
