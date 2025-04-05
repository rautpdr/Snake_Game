# SNAKE GAME

A Python implementation of the classic Snake Game using the Turtle graphics module. This project utilizes Object-Oriented Programming (OOP) principles to manage the game elements such as the snake, food, and scoreboard.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

The Snake Game is a console-based arcade game where the player controls a snake to collect food. Each time the snake eats the food, it grows in length and the score increases. The objective is to survive as long as possible without colliding with the wall or the snake’s own body.

This project highlights how OOP concepts can be applied in a game development scenario using Python.

## How it Works

1. **Start the Game**: Run the `main.py` file to start playing.
2. **Control the Snake**: Use the arrow keys:
   - `w`: Move up
   - `s`: Move down
   - `a`: Move left
   - `d`: Move right
3. **Collect Food**: Guide the snake to the food to earn points and grow longer.
4. **Avoid Collisions**:
   - Do not hit the walls.
   - Do not run into your own tail.
5. **Game Over**: If a collision happens, the game ends and displays your final score.

## Technologies Used

- **Python**: Core language for game logic and structure
- **Turtle**: Graphics module used for drawing and animating game elements
- **OOP (Object-Oriented Programming)**: For organizing code into reusable and maintainable classes

## Lessons Learned

Working on this project helped solidify concepts such as:

- **Class Design**: Creating and interacting with multiple classes (`Snake`, `Food`, `Scoreboard`)
- **Game Loop**: Using `while` loops and `time.sleep()` for real-time game control
- **Event Handling**: Managing key inputs for smooth user control
- **Collision Detection**: Implementing logic for both wall and self-collisions
- **Encapsulation**: Keeping responsibilities clean and scoped within their respective classes
