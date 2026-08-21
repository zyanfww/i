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
        title = TexText(R"$\mathbb{J}$anuary", font_size=60)
        title.set_color(color)
        under = Underline(title, buff=-0.1)
        under.insert_n_curves(10)
        under.set_stroke(width=[0.5, 1.5, 1.5, 0.5], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)