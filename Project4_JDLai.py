# Name: Joshua Lai
# Project 4
# Completed 5/7/23

from typing import *
from turtle import Turtle, Screen
import turtle
from typing import Tuple

class Pair:
    x : int
    y : int
    def __init__(self, new_x = 0, new_y = 0) -> None:
        self.x = new_x
        self.y = new_y
    def __str__(self) -> str:
        return f"<{self.x}, {self.y}>"
    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)
    def __mul__(self, other):
        return Pair(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Pair(self.x * self.y - other.x * other.y, self.x * other.x - self.y * other.y)

def main_one():
    p1 = Pair(3, 2)
    p2 = Pair(1, 5)
    p3 = Pair(4, 3)

    print(f"p1 is: {p1}")
    print(f"p2 is: {p2}")
    print(f"p3 is: {p3}\n")

    print(f"p1 + p2 = {p1 + p2}")
    print(f"p1 * p2 = {p1 * p2}")
    print(f"p1 / p2 = {p1 / p2}")
    print(f"p1 + p2 * p3 = {p1 + p2 * p3}")
    print(f"p1 * p2 / p3 + p1 = {p1 * p2 / p3 + p1}")

    p1 = Pair(10.5, 24.1274)
    p2 = Pair(0, 0)
    p3 = Pair(999, 999)

    print(f"\np1 is: {p1}")
    print(f"p2 is: {p2}")
    print(f"p3 is: {p3}\n")

    print(f"p1 + p2 + p3 = {p1 + p2 + p3}")
    print(f"p3 * p2 = {p3 * p2}")
    print(f"p3 / p2 / p1 / p2= {p3 / p2 / p1 / p2}")
    print(f"p1 + p2 * p3 / p1 = {p1 + p2 * p3 / p1}")
    print(f"p1 * p2 / p3 + p1 = {p1 * p2 / p3 + p1}")
    
    

# TASK ONE OUTPUT:
# p1 is: <3, 2>
# p2 is: <1, 5>
# p3 is: <4, 3>

# p1 + p2 = <4, 7>
# p1 * p2 = <3, 10>
# p1 / p2 = <1, -7>
# p1 + p2 * p3 = <7, 17>
# p1 * p2 / p3 + p1 = <21, -16>

# p1 is: <10.5, 24.1274>
# p2 is: <0, 0>
# p3 is: <999, 999>

# p1 + p2 + p3 = <1009.5, 1023.1274>
# p3 * p2 = <0, 0>
# p3 / p2 / p1 / p2= <-2654728418.34585, -0.0>
# p1 + p2 * p3 / p1 = <-242.8377, 24.1274>
# p1 * p2 / p3 + p1 = <-997990.5, 24.1274>



class Polygon:
    _point_list : List[Tuple[int, int]]
    def __init__(self, *point : Tuple[int, int]) -> None:
        self._point_list = list(point)
    def add_point(self, new_point : Tuple[int, int], index = -1) -> None:
        if(index < 0):
            self._point_list.append(new_point)
        else:
            self._point_list.insert(new_point, index)
    def get_point(self, index : int) -> Tuple[int, int]:
        return self._point_list[index]
    def display_side(self) -> int:
        return len(self._point_list)
    def draw_polygon(self) -> None:
        wn = Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

        turtle.TurtleScreen._RUNNING = True

        pen = Turtle()
        pen.hideturtle()
        pen.speed("fastest")
        last_point = self._point_list[len(self._point_list) - 1]
        pen.up()
        pen.setpos(last_point[0], last_point[1])
        pen.down()
        for point in self._point_list:
            pen.setpos(point[0], point[1])
        
        wn.mainloop()

class Rectangle(Polygon):
    _lower_left = Tuple[int, int]
    _upper_right = Tuple[int, int]
    def __init__(self, lower_left : Tuple[int, int], upper_right: Tuple[int, int]) -> None:
        super().__init__(lower_left, (lower_left[0], upper_right[1]), upper_right, (upper_right[0], lower_left[1]))
        self._lower_left = lower_left
        self._upper_right = upper_right
    def get_lower_left(self) -> Tuple[int, int]:
        return self._lower_left
    def get_upper_right(self) -> Tuple[int, int]:
        return self._upper_right

def main_two():
    pentagon = Polygon((-100, 0), (100, 0), (150, 200), (0, 300), (-150, 200))
    print(f"This polygon has {pentagon.display_side()} sides.")
    pentagon.draw_polygon()

    rectangle = Rectangle((-200, -100), (200, 100))
    print(f"Lower left: {rectangle.get_lower_left()}")
    print(f"Upper right: {rectangle.get_upper_right()}")
    rectangle.draw_polygon()

# TASK TWO OUTPUT:
# Which task would you like to run? Type 1 or 2: 2
# This polygon has 5 sides.
# Lower left: (-200, -100)
# Upper right: (200, 100)

# SEE .pdf FOR PICTURES

if __name__ == "__main__":
    selection = int(input("Which task would you like to run? Type 1 or 2: "))
    if (selection == 1):
        main_one()
    elif (selection == 2):
        main_two()