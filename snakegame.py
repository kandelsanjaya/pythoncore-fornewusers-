# Simple Snake Game (Terminal Version)
# Controls:
# W = Up
# S = Down
# A = Left
# D = Right

import random
import os
import time

width = 20
height = 10

snake = [[5, 5]]
direction = "RIGHT"

food = [random.randint(0, width - 1), random.randint(0, height - 1)]

score = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw():
    clear()

    for y in range(height):
        for x in range(width):

            if [x, y] == food:
                print("*", end=" ")

            elif [x, y] in snake:
                print("O", end=" ")

            else:
                print(".", end=" ")

        print()

    print("\nScore:", score)


while True:

    draw()

    move = input("Move (W/A/S/D): ").upper()

    if move == "W":
        direction = "UP"

    elif move == "S":
        direction = "DOWN"

    elif move == "A":
        direction = "LEFT"

    elif move == "D":
        direction = "RIGHT"

    head = snake[0][:]

    if direction == "UP":
        head[1] -= 1

    elif direction == "DOWN":
        head[1] += 1

    elif direction == "LEFT":
        head[0] -= 1

    elif direction == "RIGHT":
        head[0] += 1

    # Wall collision
    if (
        head[0] < 0
        or head[0] >= width
        or head[1] < 0
        or head[1] >= height
    ):
        print("Game Over!")
        break

    # Self collision
    if head in snake:
        print("Game Over!")
        break

    snake.insert(0, head)

    # Food eaten
    if head == food:
        score += 1
        food = [random.randint(0, width - 1), random.randint(0, height - 1)]
    else:
        snake.pop()

    time.sleep(0.1)

print("Final Score:", score)