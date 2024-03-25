from manim import *

LIST = [3, 1, 7, 2, 10, 6, 5, 4, 9, 8]

class Source(MovingCameraScene):
    def construct(self):
        self.list_tex = [Tex(str(x)).shift(RIGHT*index/2) for (index, x) in enumerate(LIST)]
        self.play(*[Write(x) for x in self.list_tex])
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
    
    def partition(self, array, low, high):

        # Choose the rightmost element as pivot
        pivot = array[high]

        # Pointer for greater element
        i = low - 1

        # Traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            self.compare(j, high)
            if array[j] <= pivot:

                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])
                self.swap(i, j)

        # Swap the pivot element with
        # the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        self.swap(i + 1, high)

        # Return the position from where partition is done
        return i + 1


    # Function to perform quicksort
    def quickSort(self, array, low, high):
        if low < high:

            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(array, low, high)

            # Recursive call on the left of pivot
            self.quickSort(array, low, pi - 1)

            # Recursive call on the right of pivot
            self.quickSort(array, pi + 1, high)