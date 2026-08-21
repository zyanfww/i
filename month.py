from manimlib import *

class YourProbelm(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        problem = Tex(R"\mathrm{Y}our \mathrm{B}ith \mathrm{M}onth")
        math = Tex(R"\mathrm{Y}our \mathrm{M}ath \mathrm{P}roblem")

        problem.shift(UP * 0.5)
        math.next_to(problem, DOWN, buff=MED_LARGE_BUFF)
        problem.set_color(color)
        math.set_color(color)

        self.add(problem, math)