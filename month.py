from manimlib import *

class YourProbelm(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        problem = TexText(R"$\mathbb{Y}$our $\mathbb{B}$irth $\mathbb{M}$onth")
        math = TexText(R"$\mathbb{Y}$our $\mathbb{M}$ath $\mathbb{P}$roblem")

        problem.shift(UP * 0.5)
        math.next_to(problem, DOWN, buff=MED_LARGE_BUFF)
        problem.set_color(color)
        math.set_color(color)

        self.add(problem, math)