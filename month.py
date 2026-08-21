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

class February(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{F}$ebruary", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"x^2 - 7x + 12 = 0")
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Find all possible values of $x$")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class March(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{M}$arch", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\lim_{x\to0}\frac{\sin(5x)}{x}"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class April(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{A}$pril", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"A = \begin{pmatrix}"
            R"0&0&0\\"
            R"0&1&1\\"
            R"0&1&2"
            R"\end{pmatrix}"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Find the eigenvalues")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class May(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{M}$ay", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\int_0^1 x^2 e^x\,dx"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class June(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{J}$une", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\frac{z-2i}{z+i}=1+i"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Find $z$")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class July(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{J}$uly", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\sum_{k=1}^{n} k^2 = "
            R"\frac{n(n+1)(2n+1)}{6}"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText(
            "Find $n$ if the sum is $385$"
        )
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class August(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{A}$ugust", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\det\begin{pmatrix}"
            R"x&1&0\\"
            R"1&x&1\\"
            R"0&1&x"
            R"\end{pmatrix}=0"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Find $x$")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class September(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{S}$eptember", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\mathbf{a}=(2,-1,3),\quad "
            R"\mathbf{b}=(1,2,-1)"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText(
            r"Find $\mathbf{a}\times\mathbf{b}$"
        )
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class October(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{O}$ctober", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"2^x+2^{-x}=\frac{5}{2}"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Find $x$")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class November(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{N}$ovember", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"f(x)=x^3-3x^2+2"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText(
            "Find all critical points of $f$"
        )
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)


class December(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{D}$ecember", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(
            R"\int\frac{dx}{x^2+4x+13}"
        )
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_width(FRAME_WIDTH - 5)
        solve.set_color(color)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.25)
        self.add(solve)