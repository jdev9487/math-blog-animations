from manim import *

LIST = [3, 1, 7, 2, 10, 6, 5, 4, 9, 8]

class Source(MovingCameraScene):
    def construct(self):
        elements = [Element(Tex(str(x)), {0 : index}) for (index, x) in enumerate(LIST)]
        self.node = Node(elements, None, None, None, None)
        self.quick_sort(self.node)

    def quick_sort(self, node):
        leftPivot, leftLeftUnsorted, leftRightUnsorted = self.partition(node.leftUnsorted)
        node.leftPivot = Node(leftLeftUnsorted, leftRightUnsorted, None, None, node, leftPivot)
        rightPivot, rightLeftUnsorted, rightRightUnsorted = self.partition(node.righUnsorted)
        node.rightPivot = Node(rightLeftUnsorted, rightRightUnsorted, None, None, node, rightPivot)
        self.quick_sort(node.leftPivot)
        self.quick_sort(node.rightPivot)

    def partition(self, elements):
        return pivot, leftUnsorted, rightUnsorted
        
        
class Element():
    def __init__(self, mObject, x_position_dict):
        self.display = mObject
        self.x_position = x_position_dict

class Node():
    def __init__(self, leftUnsorted, rightUnsorted, leftPivot, rightPivot, parent, element):
        self.leftUnsorted = leftUnsorted
        self.rightUnsorted = rightUnsorted
        self.leftPivot = leftPivot
        self.rightPivot = rightPivot
        self.parent = parent
        self.element = element