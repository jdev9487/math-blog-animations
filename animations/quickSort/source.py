from manim import *

LIST = [3, 1, 6, 2, 9, 5, 4, 8, 7]

class Source(MovingCameraScene):
    def construct(self):
        elements = [Element(VGroup(Tex(str(x)).shift(RIGHT * index), Rectangle(height=1, width=1).shift(RIGHT * index)).set_color(YELLOW_D), x) for (index, x) in enumerate(LIST)]
        self.top = Dot(radius=0.1, color=GREEN_E)
        self.bottom = Dot(radius=0.1, color=PURPLE_E)
        self.container = VGroup(*[x.display for x in elements], self.top, self.bottom)
        self.wait()
        self.play(self.camera.auto_zoom(self.container, margin=2))
        self.play(*[Write(x.display) for x in elements])
        self.wait()
        # key = Tex("unsorted\\\\", "pivot\\\\", "sorted").scale_to_fit_width(self.camera.frame.width * 0.1)
        # key[0].set_color(YELLOW_D)
        # key[1].set_color(BLUE)
        # key[2].set_color(RED)
        # key.align_to(self.camera.frame, UP + LEFT).shift((DOWN + RIGHT) * self.camera.frame.height * 0.1)
        # self.play(FadeIn(key))
        # key.add_updater(self.lock_to_frame)
        # self.node = Node(elements, None, None, None, None, None)
        # self.quick_sort(self.node)
        # self.raise_objects()
        # self.wait(3)

    def lock_to_frame(self, mob):
        mob.scale_to_fit_width(self.camera.frame.width * 0.1)
        mob.align_to(self.camera.frame, UP).align_to(self.camera.frame, LEFT).shift((DOWN + RIGHT) * self.camera.frame.height * 0.1)

    def quick_sort(self, node):
        if node is None: return

        if node.leftUnsorted and len(node.leftUnsorted) != 0 and node.get_depth() != 0: self.show_recursive_processes(node.leftUnsorted)
        leftPivot, leftLeftUnsorted, leftRightUnsorted = self.partition(node.leftUnsorted)
        node.leftPivot = Node(leftLeftUnsorted, leftRightUnsorted, None, None, node, leftPivot)
        if ((leftLeftUnsorted and len(leftLeftUnsorted) != 0) or
            (leftRightUnsorted and len(leftRightUnsorted) != 0)):
            self.quick_sort(node.leftPivot)

        if node.rightUnsorted and len(node.rightUnsorted) != 0 and node.get_depth() != 0: self.show_recursive_processes(node.rightUnsorted)
        rightPivot, rightLeftUnsorted, rightRightUnsorted = self.partition(node.rightUnsorted)
        node.rightPivot = Node(rightLeftUnsorted, rightRightUnsorted, None, None, node, rightPivot)
        if ((rightLeftUnsorted and len(rightLeftUnsorted) != 0) or
            (rightRightUnsorted and len(rightRightUnsorted) != 0)):
            self.quick_sort(node.rightPivot)

    def partition(self, elements):
        if elements is None or len(elements) == 0: return None, None, None
        if len(elements) == 1:
            self.drop_objects(elements)
            self.lock(elements[0])
            return elements[0], None, None
        if len(self.node.leftUnsorted) != len(elements):
            self.drop_objects(elements)
        pivot = elements[-1]
        self.highlight_pivot(pivot)
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
        self.lock(elements[i])
        return elements[i], elements[:i], elements[i + 1:]

    def lock(self, element):
        element.display.set_color(RED).set_z_index(100)
        self.wait()

    def show_recursive_processes(self, elements):
        if len(elements) <= 1: return
        group = VGroup(*[x.display for x in elements])
        brace = Brace(group, sharpness=1, direction=UP)
        description = Text("quicksort()", font="Monospace").next_to(brace, UP).scale(0.7).shift(DOWN*0.3)
        if description.width > 0.8 * brace.width:
            description = description.scale(0.8/(description.width/brace.width))
        self.brace_group = VGroup(brace, description)
        if (self.camera.frame_center[0] + self.camera.frame_height/2) > (self.brace_group.get_x() + self.brace_group.height/2):
            self.play(Write(self.brace_group))
        else:
            self.play(Write(self.brace_group), self.camera.auto_zoom([self.container, self.brace_group], margin=2))
        self.wait()
        self.play(FadeOut(self.brace_group))

    def highlight_pivot(self, pivotElement):
        self.play(pivotElement.display.animate.set_color(BLUE))

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

    def swap_objects(self, first_element, second_element, first_index, second_index):
        path_arc = -1.5
        left_element, right_element = (first_element, second_element) \
            if first_index <= second_index \
            else (second_element, first_element)
        y = first_element.display.get_y()
        left_x = left_element.display.get_x()
        right_x = right_element.display.get_x()
        top_path = Line((UP * y) + (RIGHT * left_x), (UP * y) + (RIGHT * right_x), path_arc=path_arc)
        bottom_path = Line((UP * y) + (RIGHT * right_x), (UP * y) + (RIGHT * left_x), path_arc=path_arc)
        self.play(MoveAlongPath(left_element.display, top_path), MoveAlongPath(right_element.display, bottom_path))
        self.wait(0.5)
    
    def drop_objects(self, elements):
        self.play(*[x.display.animate.shift(DOWN) for x in elements])
        self.play(self.camera.auto_zoom(self.container, margin=2))
        self.wait()

    def raise_objects(self):
        self.play(*[x.display.animate.shift(DOWN * (x.display.get_y())) for x in self.node.leftUnsorted],
                  self.camera.frame.animate.move_to([len(LIST)/2 - 1/2, 0, 0]))

        
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
            return 1 + self.parent.get_depth()