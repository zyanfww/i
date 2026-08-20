from manimlib import *

class Roman(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        math = Tex(" 19 - 1 = 20")
        math.set_color(color)
        math.shift(2 * UP)

        self.play(Write(math[:5]))

        roman = Tex("XIX - I")
        roman.set_color(GOLD)
        roman.next_to(math, DOWN, LARGE_BUFF * 1.5, aligned_edge=LEFT)

        sur_math1 = SurroundingRectangle(math[:2], stroke_color=color, stroke_width=3).round_corners(0.05)
        sur_roman1 = SurroundingRectangle(roman[:3], stroke_color=color, stroke_width=3).round_corners(0.05)

        self.play(
            FadeIn(roman[:3], UP * 0.5),
            ShowCreation(sur_math1),
        )
        self.play(
            ReplacementTransform(sur_math1, sur_roman1),
            roman[:3].animate.set_color(color)
        )
        self.play(
            Uncreate(sur_roman1),
            roman[:3].animate.set_color(GOLD)
        )

        one_and_i_rect = VGroup(
            SurroundingRectangle(math["1"][1], stroke_color=color, stroke_width=3).round_corners(0.05),
            SurroundingRectangle(roman["I"][1], stroke_color=color, stroke_width=3).round_corners(0.05),
        )

        self.play(
            ShowCreation(one_and_i_rect[0]),
        )
        self.play(
            ReplacementTransform(one_and_i_rect[0], one_and_i_rect[1]),
            roman["I"][1].animate.set_color(color)
        )
        self.play(
            Uncreate(one_and_i_rect[1]),
            roman["I"][1].animate.set_color(GOLD)
        )
        self.play(
            TransformFromCopy(math["-"], roman["-"])
        )
        self.wait(0.5)
        self.play(
            roman["-"].animate.move_to(roman["I"][0]),
            roman["I"][1].animate.move_to(roman["I"][0])
        )
        self.wait()
        self.play(
            FadeOut(roman["-"]),
            FadeOut(roman["I"])
        )
        self.wait()

        xx = Tex("XX")
        xx.move_to(roman["XIX"])
        xx.set_color(GOLD)

        self.play(
            ReplacementTransform(roman["X"][0], xx[0]),
            ReplacementTransform(roman["X"][1], xx[1]),
        )
        self.play(
            ReplacementTransform(xx, math["20"])
        )
        self.wait()