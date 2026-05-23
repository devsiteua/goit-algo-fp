import turtle


def get_recursion_level():
    try:
        level = int(input("Enter recursion level: "))
    except ValueError:
        print("Incorrect value. Recursion level 7 will be used.")
        level = 7

    if level < 0:
        print("Recursion level cannot be negative. Level 0 will be used.")
        level = 0

    return level


def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    turtle.left(45)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)

    turtle.right(90)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)

    turtle.left(45)
    turtle.backward(branch_length)


def main():
    level = get_recursion_level()

    turtle.title("Pythagoras Tree")
    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.backward(250)
    turtle.pendown()

    draw_pythagoras_tree(120, level)

    turtle.done()


if __name__ == "__main__":
    main()
