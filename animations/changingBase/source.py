from manim import *
import numpy as np

class Source(MovingCameraScene):
    def construct(self):
        self.construct_conversion_legend()
        self.wait()
        self.construct_initial_equation()
        self.loop_digits()
        self.wait()

    def loop_digits(self):
        for i in range(1, 3):
            self.lhs = self.lhs * 16
            self.multiply_by_16(i)
            # wiggle a_i and integer part of lhs
            self.associate_integer_with_a_i()
            a_i = int(self.lhs)
            # integer part of lhs and a_i should "fly" off to left edge of screen
            # leaving 0. something = fraction expansion without first term
            self.lhs = self.lhs - a_i
            # fraction expansions should slide over to the left
    
    def associate_integer_with_a_i(self):
        decimal_point = self.equation[0].tex_string.index('.')
        self.play(*[Wiggle(self.equation[0][i]) for i in range(decimal_point)], Wiggle(self.equation[3]))
    
    def multiply_by_16(self, iteration):
        multiply = MathTex(r"[\times 16]").shift(DOWN)
        self.play(FadeIn(multiply))
        rhs = create_fraction_expansion(iteration, iteration - 1)
        new_equation = MathTex(str(self.lhs)[:8], r"\hdots", "=", *rhs)
        self.play(Transform(self.equation, new_equation))
        old_equation = self.equation
        self.equation = new_equation
        self.add(self.equation)
        self.remove(old_equation)
        self.play(FadeOut(multiply))

    def construct_initial_equation(self):
        self.lhs = np.sqrt(2)
        pre1 = MathTex(r"\sqrt{2}", "", "=", str(self.lhs)[:8], r"\hdots").align_to(self.camera.frame, UP).shift(DOWN * 2)
        self.play(Write(pre1))
        self.lhs = self.lhs - 1
        pre2 = MathTex(r"\sqrt{2}", "-1", "=", str(self.lhs)[:8], r"\hdots").align_to(self.camera.frame, UP).shift(DOWN * 2)
        self.play(Transform(pre1, pre2))
        self.wait()
        self.first_numerator_subscript = 1
        self.first_denominator_superscript = 1
        self.rhs = create_fraction_expansion(self.first_numerator_subscript, self.first_numerator_subscript)
        self.equation = MathTex(str(self.lhs)[:8], r"\hdots", "=", *self.rhs)
        self.play(pre2[3].animate.shift(UP * (self.equation[0].get_y() - pre2[3].get_y())).shift(RIGHT * (self.equation[0].get_x() - pre2[3].get_x())),
                  pre2[4].animate.shift(UP * (self.equation[1].get_y() - pre2[4].get_y())).shift(RIGHT * (self.equation[1].get_x() - pre2[4].get_x())))
        self.play(FadeIn(self.equation), FadeOut(pre2[3]), FadeOut(pre2[4]))

    def construct_conversion_legend(self):
        self.legend = create_legend()
        legend_group = VGroup(*[x.scale(1/2) for x in self.legend])
        legend_group.arrange(DOWN, buff=SMALL_BUFF)
        box = SurroundingRectangle(legend_group, buff=MED_SMALL_BUFF)
        box_group = VGroup(box, legend_group)
        for (index, x) in enumerate(self.legend):
            self.play(Write(x), run_time=1 - index/len(self.legend))
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

def create_fraction_expansion(numerator_subscript, denominator_superscript):
    return [
        f"{{a_{numerator_subscript}",
        r"\over",
        "16",
        f"^{denominator_superscript}}}",
        "+",
        f"{{a_{numerator_subscript + 1}",
        r"\over",
        "16",
        f"^{denominator_superscript + 1}}}",
        "+",
        f"{{a_{numerator_subscript + 2}",
        r"\over",
        "16",
        f"^{denominator_superscript + 2}}}",
        r"\hdots"
    ]

s = Source()
s.construct()