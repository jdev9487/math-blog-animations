from manim import *

LIST = [3, 1, 7, 2, 10, 6, 5, 4, 9, 8]

class Source(MovingCameraScene):
    def construct(self):
        elements = [Element(Tex(str(x)).shift(RIGHT * index), x) for (index, x) in enumerate(LIST)]
        self.top = Circle(0.1, color=GREEN, fill_opacity=1)
        self.bottom = Circle(0.1, color=PINK, fill_opacity=1)
        self.play(*[Write(x.display) for x in elements])
        self.play(self.camera.frame.animate.move_to([5,-2,0]))
        self.wait()
        self.node = Node(elements, None, None, None, None, None)
        self.quick_sort(self.node)
        self.raise_objects()

    def quick_sort(self, node):
        if node is None: return
        leftPivot, leftLeftUnsorted, leftRightUnsorted = self.partition(node.leftUnsorted)
        node.leftPivot = Node(leftLeftUnsorted, leftRightUnsorted, None, None, node, leftPivot)
        rightPivot, rightLeftUnsorted, rightRightUnsorted = self.partition(node.rightUnsorted)
        node.rightPivot = Node(rightLeftUnsorted, rightRightUnsorted, None, None, node, rightPivot)

        if ((leftLeftUnsorted and len(leftLeftUnsorted) != 0) or
            (leftRightUnsorted and len(leftRightUnsorted) != 0)):
            self.quick_sort(node.leftPivot)
        if ((rightLeftUnsorted and len(rightLeftUnsorted) != 0) or
            (rightRightUnsorted and len(rightRightUnsorted) != 0)):
            self.quick_sort(node.rightPivot)

    def partition(self, elements):
        if elements is None or len(elements) == 0: return None, None, None
        self.drop_objects(elements)
        # acknowledge pivot
        pivot = elements[-1]
        i = -1
        if len(elements) > 1:
            self.initialise_markers(elements[0].display.get_y(), elements[0].display.get_x())
        for j in range(len(elements)):
            if elements[j].value <= pivot.value:
                i = i + 1
                if len(elements) > 1:
                    self.increment_bottom_marker()
                if (j > i):
                    self.swap_objects(elements[i], elements[j], i, j)
                    (elements[i], elements[j]) = (elements[j], elements[i])
            if len(elements) > 1:
                if j == len(elements) - 1:
                    self.fade_out_markers()
                else: 
                    self.increment_top_marker()
        return elements[i], elements[:i], elements[i + 1:]

    def fade_out_markers(self):
        self.play(FadeOut(self.top, self.bottom))

    def increment_top_marker(self):
        self.play(self.top.animate.shift(RIGHT))

    def increment_bottom_marker(self):
        self.play(self.bottom.animate.shift(RIGHT))

    def initialise_markers(self, depth, start):
        top_destination_x_shift = RIGHT * (start - self.top.get_x())
        bottom_destination_x_shift = RIGHT * (start - 1 - self.bottom.get_x())

        top_destination_y_shift = UP * (depth + 0.5 - self.top.get_y())
        bottom_destination_y_shift = UP * (depth - 0.5 - self.bottom.get_y())
        self.top.shift(top_destination_x_shift + top_destination_y_shift)
        self.bottom.shift(bottom_destination_x_shift + bottom_destination_y_shift)
        self.play(FadeIn(self.top, self.bottom))

        # self.play(self.top.animate.shift(top_destination_x_shift + top_destination_y_shift),
        #           self.bottom.animate.shift(bottom_destination_x_shift + bottom_destination_y_shift))
    
    def swap_objects(self, first_element, second_element, first_index, second_index):
        self.play(first_element.display.animate.shift(RIGHT * (second_index - first_index)),
                  second_element.display.animate.shift(RIGHT * (first_index - second_index)))
        self.wait()
    
    def drop_objects(self, elements):
        self.play(*[x.display.animate.shift(DOWN) for x in elements])
        self.wait(2)

    def raise_objects(self):
        self.play(*[x.display.animate.shift(DOWN * (x.display.get_y())) for x in self.node.leftUnsorted])

        
class Element():
    def __init__(self, mObject, value):
        self.display = mObject
        self.value = value

class Node():
    def __init__(self, leftUnsorted, rightUnsorted, leftPivot, rightPivot, parent, element):
        self.leftUnsorted = leftUnsorted
        self.rightUnsorted = rightUnsorted
        self.leftPivot = leftPivot
        self.rightPivot = rightPivot
        self.parent = parent
        self.element = element

    def get_depth(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.get_depth(self.parent)

s = Source()
s.construct()