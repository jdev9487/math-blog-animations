from manim import *
import numpy as np

X_SQUARED_LENGTH = 2
TEXT_BUFFER = 0.4
GAP = 0.1
RECT_WIDTH = 1.5
C_WIDTH = 1.7
C_X = 6
C_Y = 1.5

class Source(Scene):
    def construct(self):
        (x_squared, x_squared_length_text_1, x_squared_length_text_2, x_squared_area_text) = createXSquaredObjects()
        (rect1, rect2, rect_width_text_1, rect_width_text_2, rect_area_text_1, rect_area_text_2) = createRectangleObjects()
        (completer, completer_area_text) = createCompleterObjects()
        (c, adjusted) = createAdjustedObjects()
        self.play(Create(x_squared))
        self.play(Write(x_squared_length_text_1))
        self.play(Write(x_squared_length_text_2))
        self.play(Write(x_squared_area_text))
        self.play(Create(rect1))
        self.play(Write(rect_width_text_1))
        self.play(Write(rect_area_text_1))
        self.play(Create(rect2))
        self.play(Write(rect_width_text_2))
        self.play(Write(rect_area_text_2))
        self.play(Create(c))
        self.wait()
        self.play(Rotate(rect1, angle=PI/2, about_point=ORIGIN),
                  rect2.animate.shift(LEFT * (GAP + RECT_WIDTH)),
                  rect_width_text_1.animate.shift((LEFT + UP)*(2 + GAP + RECT_WIDTH/2 + TEXT_BUFFER)),
                  rect_width_text_2.animate.shift(LEFT * (GAP + RECT_WIDTH)),
                  rect_area_text_1.animate.shift((LEFT + UP) * (1 + GAP + RECT_WIDTH/2)),
                  rect_area_text_2.animate.shift(LEFT * (GAP + RECT_WIDTH)))
        self.wait()
        self.play(GrowFromCenter(completer), Transform(c, adjusted))
        self.play(Write(completer_area_text))
        self.wait()
    
def createXSquaredObjects():
    return (
        Square(X_SQUARED_LENGTH, color=RED),
        Tex('$x$').shift(LEFT * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)),
        Tex('$x$').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)),
        Tex('$x^2$')
        )

def createRectangleObjects():
    return (
        Rectangle(height=2, width=RECT_WIDTH, color=GREEN).shift(RIGHT * (1 + GAP + RECT_WIDTH/2)),
        Rectangle(height=2, width=RECT_WIDTH, color=GREEN).shift(RIGHT * (1 + 2*GAP + 3*RECT_WIDTH/2)),
        Tex('$\\frac{b}{2a}$').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)).shift(RIGHT * (1 + GAP + RECT_WIDTH/2)),
        Tex('$\\frac{b}{2a}$').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)).shift(RIGHT * (1 + 2*GAP + 3*RECT_WIDTH/2)),
        Tex('$\\frac{b}{2a}x$').shift(RIGHT * (1 + GAP + RECT_WIDTH/2)),
        Tex('$\\frac{b}{2a}x$').shift(RIGHT * (1 + 2*GAP + 3*RECT_WIDTH/2))
    )

def createCompleterObjects():
    return (
        Square(RECT_WIDTH).shift((RIGHT+UP)*(1 + GAP + RECT_WIDTH/2)),
        Tex('$\\frac{b^2}{4a^2}$').shift((RIGHT + UP) * (1 + GAP + RECT_WIDTH/2))
    )

def createAdjustedObjects():
    unadjustedPoints = [
        [C_X-C_WIDTH/2, C_Y-C_WIDTH/2, 0],
        [C_X+C_WIDTH/2, C_Y-C_WIDTH/2, 0],
        [C_X+C_WIDTH/2, C_Y+C_WIDTH/2, 0],
        [C_X-C_WIDTH/2+RECT_WIDTH, C_Y+C_WIDTH/2, 0],
        [C_X-C_WIDTH/2, C_Y+C_WIDTH/2, 0],
        [C_X-C_WIDTH/2, C_Y+C_WIDTH/2-RECT_WIDTH, 0]
    ]
    adjustedPoints = [
        [C_X-C_WIDTH/2, C_Y-C_WIDTH/2, 0],
        [C_X+C_WIDTH/2, C_Y-C_WIDTH/2, 0],
        [C_X+C_WIDTH/2, C_Y+C_WIDTH/2, 0],
        [C_X-C_WIDTH/2+RECT_WIDTH, C_Y+C_WIDTH/2, 0],
        [C_X-C_WIDTH/2+RECT_WIDTH, C_Y+C_WIDTH/2-RECT_WIDTH, 0],
        [C_X-C_WIDTH/2, C_Y+C_WIDTH/2-RECT_WIDTH, 0]
    ]
    return (
        Polygon(*unadjustedPoints),
        Polygon(*adjustedPoints, color=PINK)
    )