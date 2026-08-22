from manimlib import *

class YourInitial(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]
        title = TexText(R"$\mathbb{Y}$our $\mathbb{I}$nitial", font_size=67)
        title2 = TexText(R"$\mathbb{Y}$our $\mathbb{M}$ath $\mathbb{P}$roblem", font_size=67)

        title.shift(0.5 * UP)
        title2.next_to(title, DOWN, buff=LARGE_BUFF)

        tt = VGroup(title, title2)
        tt.set_color(color)
        tt.scale(1.0)
        tt.center()
        self.add(tt)

class A(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{A}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^1 x\ln x\,dx")
        problem.set_color(color)
        problem.set_width(FRAME_WIDTH - 3)
        problem.shift(UP)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class B(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{B}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^2}")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 6)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class C(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{C}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\infty xe^{-x}\,dx")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class D(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{D}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\lim_{x\to0}\frac{\sin x-x+\frac{x^3}{6}}{x^5}")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Evaluate the limit")
        solve.set_color(color)
        solve.set_width(FRAME_WIDTH - 4)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class E(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{E}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\infty\frac{x}{e^x-1}\,dx")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 3)

        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class F(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{F}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Find the sum")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class G(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{G}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^1\frac{\ln x}{1+x}\,dx")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class H(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{H}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n(n+1)}")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 5)

        self.add(problem)

        solve = TexText("Find the sum")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class I(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{I}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\pi x\sin x\,dx")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class J(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{J}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Evaluate the series")
        solve.set_color(color)
        solve.set_width(3.6)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class K(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{K}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\Gamma\left(\frac12\right)")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 6)

        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class L(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{L}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^1x^{a-1}(1-x)^{b-1}\,dx")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Express using the Beta function")
        solve.set_color(color)
        solve.set_width(6)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class M(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{M}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\infty x^{s-1}e^{-x}\,dx")
        problem.set_color(color)
        problem.shift(UP)
        problem.set_width(FRAME_WIDTH - 4)

        self.add(problem)

        solve = TexText("Identify the function")
        solve.set_color(color)
        solve.set_width(4)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF * 1.5)
        self.add(solve)


class N(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{N}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^s}")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Identify the function")
        solve.set_color(color)
        solve.set_width(4.8)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class O(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{O}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\infty\frac{x^{s-1}}{e^x-1}\,dx")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Express in terms of Gamma and Zeta")
        solve.set_color(color)
        solve.set_width(5.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class P(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{P}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^2}")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class Q(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{Q}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\zeta(2)")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class R(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{R}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\zeta(0)")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate using analytic continuation")
        solve.set_color(color)
        solve.set_width(5.0)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class S(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{S}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\zeta(2)=\sum_{n=1}^{\infty}\frac{1}{n^2}")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate the series")
        solve.set_color(color)
        solve.set_width(4.5)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class T(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{T}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\infty\frac{\sin x}{x}\,dx")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class U(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{U}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\oint_C\frac{e^z}{z^2}\,dz")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate using Cauchy's integral formula")
        solve.set_color(color)
        solve.set_width(5.1)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class V(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{V}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\oint_C\frac{dz}{z(z-1)}")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate using residues")
        solve.set_color(color)
        solve.set_width(4.4)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class W(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{W}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^4}")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate the series")
        solve.set_color(color)
        solve.set_width(4.5)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class X(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{X}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_{-\infty}^{\infty}e^{-x^2}\,dx")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate")
        solve.set_color(color)
        solve.set_width(3.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class Y(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{Y}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\int_0^\infty\frac{x^{s-1}}{e^x-1}\,dx")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Express in terms of Gamma and Zeta")
        solve.set_color(color)
        solve.set_width(5.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)


class Z(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{Z}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        problem = Tex(R"\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}")
        problem.set_color(color)
        problem.shift(UP * 2)
        self.add(problem)

        solve = TexText("Evaluate $\zeta(2)$")
        solve.set_color(color)
        solve.set_width(4.2)
        solve.next_to(problem, DOWN, buff=LARGE_BUFF)
        self.add(solve)