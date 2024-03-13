from manim import *
import numpy as np

X_SQUARED_LENGTH = 2
TEXT_BUFFER = 0.4
GAP = 0.1
RECT_WIDTH = 1.5
C_WIDTH = 3
C_X = -5
C_Y = 1.5
INITIAL_EQUATION_HEIGHT = -3

class Source(MovingCameraScene):
    def construct(self):
        (initial_equation, altered_initial_equation) = createInitialEquations()
        (x_squared, x_squared_length_text_1, x_squared_length_text_2, x_squared_area_text) = createXSquaredObjects()
        (rect_initial, rect1, rect2, rect_initial_width_text, rect_initial_area_text, rect_width_text_1, rect_width_text_2, rect_area_text_1, rect_area_text_2) = createRectangleObjects()
        (completer, completer_area_text) = createCompleterObjects()
        (c, adjusted, c_area_text, adjusted_c_area_text) = createAdjustedObjects()
        (completed, completed_length_text_1, completed_length_text_2, completed_area_text) = createCompletedObjects()
        final = createFinalEquations()
        self.play(Write(initial_equation))
        self.wait(2)
        self.play(Transform(initial_equation, altered_initial_equation, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        self.play(Create(x_squared), Write(x_squared_length_text_1), Write(x_squared_length_text_2))
        self.wait(2)
        self.play(Write(x_squared_area_text))
        self.wait()
        self.play(Wiggle(x_squared_area_text, scale_value=1.4), Wiggle(altered_initial_equation[0], scale_value=1.4))
        self.wait()
        self.play(Create(rect_initial), Write(rect_initial_width_text))
        self.wait(2)
        self.play(Write(rect_initial_area_text))
        self.wait()
        self.play(Wiggle(rect_initial_area_text, scale_value=1.4), Wiggle(altered_initial_equation[2], scale_value=1.4))
        self.wait(2)
        self.play(Create(c), Write(c_area_text))
        self.wait()
        self.play(Wiggle(c_area_text, scale_value=1.4), Wiggle(altered_initial_equation[4], scale_value=1.4))
        self.wait(3)
        self.play(Uncreate(rect_initial),
                  Unwrite(rect_initial_width_text),
                  Unwrite(rect_initial_area_text),
                  Create(rect1),
                  Create(rect2),
                  Write(rect_width_text_1),
                  Write(rect_width_text_2))
        self.wait()
        self.play(Write(rect_area_text_1), Write(rect_area_text_2))
        self.wait(3)
        self.play(Rotate(rect1, angle=PI/2, about_point=ORIGIN),
                  rect2.animate.shift(LEFT * (GAP + RECT_WIDTH)),
                  rect_width_text_1.animate.shift((LEFT + UP)*(2 + GAP + RECT_WIDTH/2 + TEXT_BUFFER)),
                  rect_width_text_2.animate.shift(LEFT * (GAP + RECT_WIDTH)),
                  rect_area_text_1.animate.shift((LEFT + UP) * (1 + GAP + RECT_WIDTH/2)),
                  rect_area_text_2.animate.shift(LEFT * (GAP + RECT_WIDTH)))
        self.wait(3)
        self.play(GrowFromCenter(completer),
                  Transform(c, adjusted, replace_mobject_with_target_in_scene=True),
                  Transform(c_area_text, adjusted_c_area_text, replace_mobject_with_target_in_scene=True),
                  Write(completer_area_text))
        self.wait(4)
        self.play(Create(completed))
        self.play(Uncreate(x_squared),
                  Uncreate(x_squared_area_text),
                  Uncreate(x_squared_length_text_1),
                  Uncreate(x_squared_length_text_2),
                  Uncreate(rect1),
                  Uncreate(rect2),
                  Uncreate(rect_width_text_1),
                  Uncreate(rect_width_text_2),
                  Uncreate(rect_area_text_1),
                  Uncreate(rect_area_text_2),
                  Uncreate(completer),
                  Uncreate(completer_area_text)
                  )
        self.play(Write(completed_length_text_1), Write(completed_length_text_2))
        self.wait()
        self.play(Write(completed_area_text))
        self.wait(4)
        self.play(Uncreate(adjusted),
                  Uncreate(completed),
                  Uncreate(completed_length_text_1),
                  Uncreate(completed_length_text_2))
        self.wait()
        self.play(Transform(completed_area_text, final[0][0]),
                  Transform(adjusted_c_area_text, final[0][2]),
                  Unwrite(altered_initial_equation))
        self.play(Write(final[0][1]), Write(final[0][3]))
        self.wait(2)
        self.play(Write(final[1]),
                  self.camera.frame.animate.move_to(final[1]))
        self.wait(2)
        self.play(Write(final[2]),
                  self.camera.frame.animate.move_to(final[2]))
        self.wait(2)
        self.play(Write(final[3]),
                  self.camera.frame.animate.move_to(final[3]))
        self.wait(3)
    
def createXSquaredObjects():
    return (
        Square(X_SQUARED_LENGTH, color=RED),
        MathTex('x').shift(LEFT * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)),
        MathTex('x').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)),
        MathTex('x^2')
        )

def createRectangleObjects():
    return (
        Rectangle(height=2, width=2*RECT_WIDTH+GAP, color=GREEN).shift(RIGHT * (1 + RECT_WIDTH + GAP*3/2)),
        Rectangle(height=2, width=RECT_WIDTH, color=GREEN).shift(RIGHT * (1 + GAP + RECT_WIDTH/2)),
        Rectangle(height=2, width=RECT_WIDTH, color=GREEN).shift(RIGHT * (1 + 2*GAP + 3*RECT_WIDTH/2)),
        MathTex('\\tfrac{b}{a}').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)).shift(RIGHT * (1 + RECT_WIDTH + GAP*3/2)),
        MathTex('\\frac{b}{a}x').shift(RIGHT * (1 + RECT_WIDTH + GAP*3/2)),
        MathTex('\\tfrac{b}{2a}').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)).shift(RIGHT * (1 + GAP + RECT_WIDTH/2)),
        MathTex('\\tfrac{b}{2a}').shift(DOWN * (X_SQUARED_LENGTH/2 + TEXT_BUFFER)).shift(RIGHT * (1 + 2*GAP + 3*RECT_WIDTH/2)),
        MathTex('\\frac{b}{2a}x').shift(RIGHT * (1 + GAP + RECT_WIDTH/2)),
        MathTex('\\frac{b}{2a}x').shift(RIGHT * (1 + 2*GAP + 3*RECT_WIDTH/2))
    )

def createCompleterObjects():
    return (
        Square(RECT_WIDTH, color=BLUE).shift((RIGHT+UP)*(1 + GAP + RECT_WIDTH/2)),
        MathTex('\\frac{b^2}{4a^2}').shift((RIGHT + UP) * (1 + GAP + RECT_WIDTH/2))
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
        Polygon(*unadjustedPoints, color=BLUE),
        Polygon(*adjustedPoints, color=BLUE),
        MathTex('\\frac{c}{a}').shift(RIGHT*C_X).shift(UP*C_Y),
        MathTex('\\frac{c}{a}-\\frac{b^2}{4a^2}').shift(RIGHT*C_X).shift(UP*C_WIDTH/4)
    )

def createInitialEquations():
    return (
        MathTex('ax^2', '+', 'bx', '+', 'c', '=0', color=YELLOW).shift(UP * INITIAL_EQUATION_HEIGHT),
        MathTex('x^2', '+', '\\frac{b}{a}x', '+', '\\frac{c}{a}', '=0', color=YELLOW).shift(UP * INITIAL_EQUATION_HEIGHT),
    )

def createCompletedObjects():
    return (
        Square(X_SQUARED_LENGTH + GAP + RECT_WIDTH, color=PURPLE).shift((UP+RIGHT)*(-X_SQUARED_LENGTH/2 + (X_SQUARED_LENGTH + GAP + RECT_WIDTH)/2)),
        MathTex('x + \\tfrac{b}{2a}').shift(RIGHT * (-X_SQUARED_LENGTH/2 + (X_SQUARED_LENGTH + GAP + RECT_WIDTH)/2)).shift(DOWN*(X_SQUARED_LENGTH/2 + TEXT_BUFFER)),
        MathTex('x + \\tfrac{b}{2a}').shift(UP * (-X_SQUARED_LENGTH/2 + (X_SQUARED_LENGTH + GAP + RECT_WIDTH)/2)).shift(LEFT*(X_SQUARED_LENGTH/2 + TEXT_BUFFER*2)),
        MathTex('\\left(x + \\frac{b}{2a}\\right)^2').shift((UP+RIGHT)*(-X_SQUARED_LENGTH/2 + (X_SQUARED_LENGTH + GAP + RECT_WIDTH)/2))
    )

def createFinalEquations():
    return (
        MathTex('\\left(x + \\frac{b}{2a}\\right)^2', '+', '\\frac{c}{a}-\\frac{b^2}{4a^2}}', '=0'),
        MathTex('\\left(x + \\frac{b}{2a}\\right)^2', '=', '\\frac{b^2-4ac}{4a^2}}').shift(DOWN*1.5),
        MathTex('x + \\frac{b}{2a}', '=', '\\frac{\\pm\\sqrt{b^2-4ac}}{2a}}').shift(DOWN*3),
        MathTex('x', '=', '\\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}}').shift(DOWN*4.5)
    )