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

class AB(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{A}$ - $\mathbb{B}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        A = Tex(R"\int_0^1 x\ln x\,dx")
        A.set_color(color)
        A.set_width(FRAME_WIDTH - 4)

        B = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^2}")
        B.set_color(color)
        B.set_width(FRAME_WIDTH - 4)

        A.next_to(titles, DOWN, buff=LARGE_BUFF)
        B.next_to(A, DOWN, buff=LARGE_BUFF)

        self.add(A, B)

        a = TexText("Evaluate")
        a.set_color(color)
        a.set_width(3.2)
        a.next_to(A, DOWN, buff=MED_LARGE_BUFF)

        b = TexText("Evaluate")
        b.set_color(color)
        b.set_width(3.2)
        b.next_to(B, DOWN, buff=MED_LARGE_BUFF)

        self.add(a, b)


class CD(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{C}$ - $\mathbb{D}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        C = Tex(R"\int_0^\infty xe^{-x}\,dx")
        C.set_color(color)
        C.set_width(FRAME_WIDTH - 4)

        D = Tex(R"\lim_{x\to0}\frac{\sin x-x+\frac{x^3}{6}}{x^5}")
        D.set_color(color)
        D.set_width(FRAME_WIDTH - 4)

        C.next_to(titles, DOWN, buff=LARGE_BUFF)
        D.next_to(C, DOWN, buff=LARGE_BUFF)

        self.add(C, D)

        c = TexText("Evaluate")
        c.set_color(color)
        c.set_width(3.2)
        c.next_to(C, DOWN, buff=MED_LARGE_BUFF)

        d = TexText("Evaluate the limit")
        d.set_color(color)
        d.set_width(4.2)
        d.next_to(D, DOWN, buff=MED_LARGE_BUFF)

        self.add(c, d)


class EF(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{E}$ - $\mathbb{F}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        E = Tex(R"\int_0^\infty\frac{x}{e^x-1}\,dx")
        E.set_color(color)
        E.set_width(FRAME_WIDTH - 4)

        F = Tex(R"\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}")
        F.set_color(color)
        F.set_width(FRAME_WIDTH - 4)

        E.next_to(titles, DOWN, buff=LARGE_BUFF)
        F.next_to(E, DOWN, buff=LARGE_BUFF)

        self.add(E, F)

        e = TexText("Evaluate")
        e.set_color(color)
        e.set_width(3.2)
        e.next_to(E, DOWN, buff=MED_LARGE_BUFF)

        f = TexText("Find the sum")
        f.set_color(color)
        f.set_width(3.8)
        f.next_to(F, DOWN, buff=MED_LARGE_BUFF)

        self.add(e, f)


class GH(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{G}$ - $\mathbb{H}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        G = Tex(R"\int_0^1\frac{\ln x}{1+x}\,dx")
        G.set_color(color)
        G.set_width(FRAME_WIDTH - 4)

        H = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n(n+1)}")
        H.set_color(color)
        H.set_width(FRAME_WIDTH - 4)

        G.next_to(titles, DOWN, buff=LARGE_BUFF)
        H.next_to(G, DOWN, buff=LARGE_BUFF)

        self.add(G, H)

        g = TexText("Evaluate")
        g.set_color(color)
        g.set_width(3.2)
        g.next_to(G, DOWN, buff=MED_LARGE_BUFF)

        h = TexText("Find the sum")
        h.set_color(color)
        h.set_width(3.8)
        h.next_to(H, DOWN, buff=MED_LARGE_BUFF)

        self.add(g, h)


class IJ(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{I}$ - $\mathbb{J}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        I = Tex(R"\int_0^\pi x\sin x\,dx")
        I.set_color(color)
        I.set_width(FRAME_WIDTH - 4)

        J = Tex(R"\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^2}")
        J.set_color(color)
        J.set_width(FRAME_WIDTH - 4)

        I.next_to(titles, DOWN, buff=LARGE_BUFF)
        J.next_to(I, DOWN, buff=LARGE_BUFF)

        self.add(I, J)

        i = TexText("Evaluate")
        i.set_color(color)
        i.set_width(3.2)
        i.next_to(I, DOWN, buff=MED_LARGE_BUFF)

        j = TexText("Evaluate the series")
        j.set_color(color)
        j.set_width(4.5)
        j.next_to(J, DOWN, buff=MED_LARGE_BUFF)

        self.add(i, j)


class KL(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{K}$ - $\mathbb{L}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        K = Tex(R"\Gamma\left(\frac12\right)")
        K.set_color(color)
        K.set_width(FRAME_WIDTH - 4)

        L = Tex(R"\int_0^1x^{a-1}(1-x)^{b-1}\,dx")
        L.set_color(color)
        L.set_width(FRAME_WIDTH - 4)

        K.next_to(titles, DOWN, buff=LARGE_BUFF)
        L.next_to(K, DOWN, buff=LARGE_BUFF)

        self.add(K, L)

        k = TexText("Evaluate")
        k.set_color(color)
        k.set_width(3.2)
        k.next_to(K, DOWN, buff=MED_LARGE_BUFF)

        l = TexText("Express using the Beta function")
        l.set_color(color)
        l.set_width(5.0)
        l.next_to(L, DOWN, buff=MED_LARGE_BUFF)

        self.add(k, l)


class MN(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{M}$ - $\mathbb{N}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        M = Tex(R"\int_0^\infty x^{s-1}e^{-x}\,dx")
        M.set_color(color)
        M.set_width(FRAME_WIDTH - 4)

        N = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^s}")
        N.set_color(color)
        N.set_width(FRAME_WIDTH - 4)

        M.next_to(titles, DOWN, buff=LARGE_BUFF)
        N.next_to(M, DOWN, buff=LARGE_BUFF)

        self.add(M, N)

        m = TexText("Identify the function")
        m.set_color(color)
        m.set_width(4.8)
        m.next_to(M, DOWN, buff=MED_LARGE_BUFF)

        n = TexText("Identify the function")
        n.set_color(color)
        n.set_width(4.8)
        n.next_to(N, DOWN, buff=MED_LARGE_BUFF)

        self.add(m, n)


class OP(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{O}$ - $\mathbb{P}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        O = Tex(R"\int_0^\infty\frac{x^{s-1}}{e^x-1}\,dx")
        O.set_color(color)
        O.set_width(FRAME_WIDTH - 4)

        P = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^2}")
        P.set_color(color)
        P.set_width(FRAME_WIDTH - 4)

        O.next_to(titles, DOWN, buff=LARGE_BUFF)
        P.next_to(O, DOWN, buff=LARGE_BUFF)

        self.add(O, P)

        o = TexText("Express in terms of Gamma and Zeta")
        o.set_color(color)
        o.set_width(5.2)
        o.next_to(O, DOWN, buff=MED_LARGE_BUFF)

        p = TexText("Evaluate")
        p.set_color(color)
        p.set_width(3.2)
        p.next_to(P, DOWN, buff=MED_LARGE_BUFF)

        self.add(o, p)


class QR(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{Q}$ - $\mathbb{R}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        Q = Tex(R"\zeta(2)")
        Q.set_color(color)
        Q.set_width(FRAME_WIDTH - 4)

        R = Tex(R"\zeta(0)")
        R.set_color(color)
        R.set_width(FRAME_WIDTH - 4)

        Q.next_to(titles, DOWN, buff=LARGE_BUFF)
        R.next_to(Q, DOWN, buff=LARGE_BUFF)

        self.add(Q, R)

        q = TexText("Evaluate")
        q.set_color(color)
        q.set_width(3.2)
        q.next_to(Q, DOWN, buff=MED_LARGE_BUFF)

        r = TexText("Evaluate using analytic continuation")
        r.set_color(color)
        r.set_width(5.0)
        r.next_to(R, DOWN, buff=MED_LARGE_BUFF)

        self.add(q, r)


class ST(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{S}$ - $\mathbb{T}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        S = Tex(R"\zeta(2)=\sum_{n=1}^{\infty}\frac1{n^2}")
        S.set_color(color)
        S.set_width(FRAME_WIDTH - 4)

        T = Tex(R"\int_0^\infty\frac{\sin x}{x}\,dx")
        T.set_color(color)
        T.set_width(FRAME_WIDTH - 4)

        S.next_to(titles, DOWN, buff=LARGE_BUFF)
        T.next_to(S, DOWN, buff=LARGE_BUFF)

        self.add(S, T)

        s = TexText("Evaluate the series")
        s.set_color(color)
        s.set_width(4.5)
        s.next_to(S, DOWN, buff=MED_LARGE_BUFF)

        t = TexText("Evaluate")
        t.set_color(color)
        t.set_width(3.2)
        t.next_to(T, DOWN, buff=MED_LARGE_BUFF)

        self.add(s, t)


class UV(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{U}$ - $\mathbb{V}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        U = Tex(R"\oint_C\frac{e^z}{z^2}\,dz")
        U.set_color(color)
        U.set_width(FRAME_WIDTH - 4)

        V = Tex(R"\oint_C\frac{dz}{z(z-1)}")
        V.set_color(color)
        V.set_width(FRAME_WIDTH - 4)

        U.next_to(titles, DOWN, buff=LARGE_BUFF)
        V.next_to(U, DOWN, buff=LARGE_BUFF)

        self.add(U, V)

        u = TexText("Evaluate using Cauchy's integral formula")
        u.set_color(color)
        u.set_width(5.1)
        u.next_to(U, DOWN, buff=MED_LARGE_BUFF)

        v = TexText("Evaluate using residues")
        v.set_color(color)
        v.set_width(4.4)
        v.next_to(V, DOWN, buff=MED_LARGE_BUFF)

        self.add(u, v)


class WX(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{W}$ - $\mathbb{X}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        W = Tex(R"\sum_{n=1}^{\infty}\frac{1}{n^4}")
        W.set_color(color)
        W.set_width(FRAME_WIDTH - 4)

        X = Tex(R"\int_{-\infty}^{\infty}e^{-x^2}\,dx")
        X.set_color(color)
        X.set_width(FRAME_WIDTH - 4)

        W.next_to(titles, DOWN, buff=LARGE_BUFF)
        X.next_to(W, DOWN, buff=LARGE_BUFF)

        self.add(W, X)

        w = TexText("Evaluate the series")
        w.set_color(color)
        w.set_width(4.5)
        w.next_to(W, DOWN, buff=MED_LARGE_BUFF)

        x = TexText("Evaluate")
        x.set_color(color)
        x.set_width(3.2)
        x.next_to(X, DOWN, buff=MED_LARGE_BUFF)

        self.add(w, x)


class YZ(InteractiveScene):
    def construct(self):
        color = [PURPLE_A, PURPLE_C]

        title = TexText(R"$\mathbb{Y}$ - $\mathbb{Z}$", font_size=67)
        title.set_color(color)

        under = Underline(title)
        under.insert_n_curves(10)
        under.set_stroke(width=[1, 2, 2, 1], color=color)

        titles = VGroup(under, title)
        titles.to_edge(UP)
        self.add(titles)

        Y = Tex(
            R"\int_0^\infty\frac{x^{s-1}}{e^x-1}\,dx"
        )
        Y.set_color(color)
        Y.set_width(FRAME_WIDTH - 4)

        Z = Tex(
            R"\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}"
        )
        Z.set_color(color)
        Z.set_width(FRAME_WIDTH - 4)

        Y.next_to(titles, DOWN, buff=LARGE_BUFF)
        Z.next_to(Y, DOWN, buff=LARGE_BUFF)

        self.add(Y, Z)

        y = TexText("Express in terms of Gamma and Zeta")
        y.set_color(color)
        y.set_width(5.2)
        y.next_to(Y, DOWN, buff=MED_LARGE_BUFF)

        z = TexText(R"Evaluate $\zeta(2)$")
        z.set_color(color)
        z.set_width(4.2)
        z.next_to(Z, DOWN, buff=MED_LARGE_BUFF)

        self.add(y, z)