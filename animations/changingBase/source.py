from manim import *
import numpy as np

class Source(Scene):
    def construct(self):
        srt = np.sqrt(2)
        first = MathTex("0.414", "=", "{a_1", r"\over", "16", "^1}", "+", "{a_2", r"\over", "16", "^2}", "+", "{a_3", r"\over", "16", "^3}")
        second = MathTex("6.627", "=", "{a_1", r"\over", "16", "^0}", "+", "{a_2", r"\over", "16", "^1}", "+", "{a_3", r"\over", "16", "^2}")
        self.add(first)
        self.wait(1)
        # self.play(*[Transform(first[i], second[i]) for i in range(len(first))])
        self.play(Transform(first, second))
        self.wait(1)
