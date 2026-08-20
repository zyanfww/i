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
        roman.next_to(math, DOWN, LARGE_BUFF * 1.5)

        sur_math1 = SurroundingRectangle(math[:2], stroke_color=color, stroke_width=3).round_corners(0.05)
        sur_roman1 = SurroundingRectangle(roman[:3], stroke_color=color, stroke_width=3).round_corners(0.05)

        self.play(
            FadeIn(roman[:3], UP * 0.5),
            ShowCreation(sur_math1),
        )
        self.play(
            ReplacementTransform(sur_math1, sur_roman1),
            roman[:3].animate.set_color(color).set_anim_args(run_time=2)
        )
        self.play(
            Uncreate(sur_roman1),
            roman[:3].animate.set_color(GOLD).set_anim_args(run_time=2)
        )
        self.wait()

        one_and_i_rect = VGroup(
            SurroundingRectangle(math["1"], stroke_color=color, stroke_width=3).round_corners(0.05),
            SurroundingRectangle(roman["I"][1], stroke_color=color, stroke_width=3).round_corners(0.05),
        )

        self.play(
            ShowCreation(one_and_i_rect[0]),
        )
        self.play(
            ReplacementTransform(one_and_i_rect[0], one_and_i_rect[1]),
            roman["I"][1].animate.set_color(color).set_anim_args(run_time=2)
        )
        self.play(
            Uncreate(one_and_i_rect[1]),
            roman["I"][1].animate.set_color(GOLD).set_anim_args(run_time=2)
        )
        self.wait()