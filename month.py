from manimlib import *

class YourProbelm(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        problem = TexText(R"$\mathbb{Y}$our $\mathbb{B}$irth $\mathbb{M}$onth")
        math = TexText(R"$\mathbb{Y}$our $\mathbb{M}$ath $\mathbb{P}$roblem")

        problem.shift(UP * 0.5)
        math.next_to(problem, DOWN, buff=LARGE_BUFF)

        pm = VGroup(problem, math)
        pm.set_color(color)
        pm.scale(1.1)
        self.add(pm)

class January(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        title = TexText(R"$\mathbb{J}$anuary", font_size=67)
        title.set_color(color)
        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"-6 + 3x = 6 - 3x")
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Solve for $x$")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF*1.25)
        self.add(solve)