from manim import *
import numpy as np

class Source(MovingCameraScene):
    def construct(self):
        self.construct_conversion_legend()
        self.wait()
        self.construct_initial_equation()
        # first = MathTex("0.414", "=", "{a_1", r"\over", "16", "^1}", "+", "{a_2", r"\over", "16", "^2}", "+", "{a_3", r"\over", "16", "^3}")
        # second = MathTex("6.627", "=", "{a_1", r"\over", "16", "^0}", "+", "{a_2", r"\over", "16", "^1}", "+", "{a_3", r"\over", "16", "^2}")
        # self.add(first)
        # self.wait(1)
        # # self.play(*[Transform(first[i], second[i]) for i in range(len(first))])
        # self.play(Transform(first, second))
        self.wait()

    def construct_initial_equation(self):
        sqrt2 = str(np.sqrt(2))[:8]
        sqrt2_minus_1 = str(np.sqrt(2) - 1)[:8]
        pre1 = MathTex(r"\sqrt{2}", "", "=", sqrt2, r"\hdots").align_to(self.camera.frame, UP).shift(DOWN * 2)
        self.play(Write(pre1))
        pre2 = MathTex(r"\sqrt{2}", "-1", "=", sqrt2_minus_1, r"\hdots").align_to(self.camera.frame, UP).shift(DOWN * 2)
        self.play(Transform(pre1, pre2))
        self.wait()
        initial = MathTex(sqrt2_minus_1, r"\hdots", "=", "{a_1", r"\over", "16", "^1}", "+", "{a_2", r"\over", "16", "^2}", "+", "{a_3", r"\over", "16", "^3}", r"\hdots")
        self.play(pre2[3].animate.shift(UP * (initial[0].get_y() - pre2[3].get_y())).shift(RIGHT * (initial[0].get_x() - pre2[3].get_x())),
                  pre2[4].animate.shift(UP * (initial[1].get_y() - pre2[4].get_y())).shift(RIGHT * (initial[1].get_x() - pre2[4].get_x())))
        self.play(FadeIn(initial[1:]))

    def construct_conversion_legend(self):
        self.legend = create_legend()
        legend_group = VGroup(*[x.scale(1/2) for x in self.legend])
        legend_group.arrange(DOWN, buff=SMALL_BUFF)
        box = SurroundingRectangle(legend_group, buff=MED_SMALL_BUFF)
        box_group = VGroup(box, legend_group)
        for (index, x) in enumerate(self.legend):
            self.play(FadeIn(x), run_time=1 - index/len(self.legend))
        self.play(Create(box))
        self.wait()
        self.play(box_group.animate.align_to(self.camera.frame, UP + RIGHT).shift((DOWN + LEFT) * 0.1))

def create_legend():
    return [
        MathTex(r"0_{\textrm{d}} = 0_{\textrm{h}}"),
        MathTex(r"1_{\textrm{d}} = 1_{\textrm{h}}"),
        MathTex(r"2_{\textrm{d}} = 2_{\textrm{h}}"),
        MathTex(r"3_{\textrm{d}} = 3_{\textrm{h}}"),
        MathTex(r"4_{\textrm{d}} = 4_{\textrm{h}}"),
        MathTex(r"5_{\textrm{d}} = 5_{\textrm{h}}"),
        MathTex(r"6_{\textrm{d}} = 6_{\textrm{h}}"),
        MathTex(r"7_{\textrm{d}} = 7_{\textrm{h}}"),
        MathTex(r"8_{\textrm{d}} = 8_{\textrm{h}}"),
        MathTex(r"9_{\textrm{d}} = 9_{\textrm{h}}"),
        MathTex(r"10_{\textrm{d}} = \textrm{a}_{\textrm{h}}"),
        MathTex(r"11_{\textrm{d}} = \textrm{b}_{\textrm{h}}"),
        MathTex(r"12_{\textrm{d}} = \textrm{c}_{\textrm{h}}"),
        MathTex(r"13_{\textrm{d}} = \textrm{d}_{\textrm{h}}"),
        MathTex(r"14_{\textrm{d}} = \textrm{e}_{\textrm{h}}"),
        MathTex(r"15_{\textrm{d}} = \textrm{f}_{\textrm{h}}")
    ]