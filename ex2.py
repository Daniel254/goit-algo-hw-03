import turtle


# def koch_curve(t: turtle.Turtle, length: float, level: int) -> None:
def koch_curve(t: turtle.Turtle, order: float, size: float) -> None:
    """Draw a Koch curve recursively.

    Args:
        t: Turtle object for drawing.
        order: Recursion order.
        size: Length of the curve segment.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    """Draw a Koch snowflake (3 Koch curves forming a triangle).

    Args:
        order: Recursion level.
        size: Length of each side of the triangle.
    """
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch Snowflake (recursion level: {order})")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    # Position turtle to center the snowflake
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Draw 3 Koch curves to form a snowflake (triangle)
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    level = int(input("Enter recursion level (recommended 0-5): "))
    draw_koch_snowflake(level)