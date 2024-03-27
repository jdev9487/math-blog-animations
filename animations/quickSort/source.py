from manim import *

LIST = [3, 1, 7, 2, 10, 6, 5, 4, 9, 8]

class Source(MovingCameraScene):
    def construct(self):
        elements = [Element(Tex(str(x)).shift(RIGHT * index), index, x) for (index, x) in enumerate(LIST)]
        self.play(*[Write(x.display) for x in elements])
        self.play(self.camera.frame.animate.move_to([5,0,0]))
        self.wait()
        self.node = Node(elements, None, None, None, None, None)
        self.quick_sort(self.node)
        self.play(*[x.display.animate.shift(DOWN * (x.display.get_y())) for x in elements])

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
        self.play(*[x.display.animate.shift(DOWN) for x in elements])
        self.wait(2)
        pivot = elements[-1]
        i = -1
        for j in range(len(elements)):
            if elements[j].value <= pivot.value:
                i = i + 1
                if (j > i):
                    (elements[i].x_position, elements[j].x_position) = (elements[j].x_position, elements[i].x_position)
                    self.play(elements[i].display.animate.shift(RIGHT * (j - i)),
                              elements[j].display.animate.shift(RIGHT * (i - j)))
                    self.wait()
                    (elements[i], elements[j]) = (elements[j], elements[i])
        return elements[i], elements[:i], elements[i + 1:]
        
        
class Element():
    def __init__(self, mObject, x_position, value):
        self.display = mObject
        self.x_position = x_position
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