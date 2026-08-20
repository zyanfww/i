from manimlib import *

class Roman(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        math = Tex(" 19 - 1 = 20")
        math.set_color(color)
        math.shift(2 * UP)

        self.play(Write(math[:5]))
        self.wait()

        roman = Tex("XIX - I")
        roman.set_color(color)
        roman.next_to(math, DOWN, LARGE_BUFF * 1.5)

        sur_math1 = SurroundingRectangle(math[:2], stroke_color=color, stroke_width=3).round_corners(0.05)
        sur_roman1 = SurroundingRectangle(roman[:3], stroke_color=color, stroke_width=3).round_corners(0.05)

        self.play(
            FadeIn(roman[:3], UP * 0.5),
            ShowCreation(sur_math1),
        )
        self.play(
            ReplacementTransform(sur_math1, sur_roman1),
            roman[:3].animate.set_color(GOLD).set_anim_args(rate_func=there_and_back)
        )
        self.play(
            Uncreate(sur_roman1)
        )
        self.wait()