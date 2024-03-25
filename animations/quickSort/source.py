from manim import *
import numpy as np

LIST = [3, 1, 7, 2, 10, 6, 5, 4, 9, 8]

class Source(MovingCameraScene):
    def construct(self):
        self.list_tex = [Tex(str(x)).shift(RIGHT*index/2) for (index, x) in enumerate(LIST)]
        self.play(*[Write(x) for x in self.list_tex])
        self.low = Tex("L").shift(RIGHT * self.list_tex[1].get_x()).shift(DOWN * 1/2)
        self.high = Tex("H").shift(RIGHT * self.list_tex[-1].get_x()).shift(DOWN * 1/2)
        pivotStart = (self.list_tex[0].get_x())*RIGHT + (self.list_tex[0].get_y() + 3)*UP
        pivotEnd = (self.list_tex[0].get_x())*RIGHT + (self.list_tex[0].get_y() + 1/2)*UP
        self.pivot = Arrow(start=pivotStart, end=pivotEnd)
        self.play(Write(self.pivot))
        self.play(Write(self.low), Write(self.high))
        self.quickSort(LIST, 0, 9)

    def swap(self, low, high):
        highHold = self.list_tex[high].get_x()
        lowHold = self.list_tex[low].get_x()
        self.play(self.list_tex[high].animate.shift(RIGHT*(lowHold - highHold)),
                  self.list_tex[low].animate.shift(RIGHT*(highHold - lowHold)), run_time=0.4)
        hold = self.list_tex[high]
        self.list_tex[high] = self.list_tex[low]
        self.list_tex[low] = hold

    def compare(self, a, b):
        self.play(Wiggle(self.list_tex[a], scale_value=2), Wiggle(self.list_tex[b], scale_value=2))

    def setPivot(self, newIndex):
        self.play(self.pivot.animate.shift(RIGHT * (self.list_tex[newIndex].get_x() - self.pivot.get_x())))

    def addLock(self, index):
        lock = Tex("\^").shift(RIGHT * (self.list_tex[index].get_x())).shift(DOWN)
        self.play(Create(lock))

    # def shiftLow(self, newIndex):
    #     if newIndex >= len(self.list_tex):
    #         return
    #     self.play(self.low.animate.shift(RIGHT * (self.list_tex[newIndex].get_x() - self.low.get_x())))

    # def shiftHigh(self, newIndex):
    #     self.play(self.high.animate.shift(RIGHT * (self.list_tex[newIndex].get_x() - self.high.get_x())))

    def shiftLimits(self, lowIndex, highIndex):
        lowShift = 0 if lowIndex >= len(self.list_tex) else RIGHT * (self.list_tex[lowIndex].get_x() - self.low.get_x())
        highShift = 0 if highIndex < 0 else RIGHT * (self.list_tex[highIndex].get_x() - self.high.get_x())
        self.play(self.low.animate.shift(lowShift), self.high.animate.shift(highShift))
    
    def partition(self, array, start, end):
        pivot = array[start]
        self.setPivot(start)
        low = start + 1
        high = end
        self.shiftLimits(low, high)

        while True:
            # If the current value we're looking at is larger than the pivot
            # it's in the right place (right side of pivot) and we can move left,
            # to the next element.
            # We also need to make sure we haven't surpassed the low pointer, since that
            # indicates we have already moved all the elements to their correct side of the pivot
            while low <= high and array[high] >= pivot:
                self.compare(high, low)
                high = high - 1
                self.shiftLimits(low, high)

            # Opposite process of the one above
            while low <= high and array[low] <= pivot:
                self.compare(low, high)
                low = low + 1
                self.shiftLimits(low, high)

            # We either found a value for both high and low that is out of order
            # or low is higher than high, in which case we exit the loop
            if low <= high:
                array[low], array[high] = array[high], array[low]
                self.swap(low, high)
                # The loop continues
            else:
                # We exit out of the loop
                break

        array[start], array[high] = array[high], array[start]
        self.swap(start, high)

        return high


    # Function to perform quicksort
    def quickSort(self, array, start, end):
        if start >= end:
            return

        p = self.partition(array, start, end)
        self.addLock(p)
        self.quickSort(array, start, p-1)
        self.quickSort(array, p+1, end)