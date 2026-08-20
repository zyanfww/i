from manimlib import *

class Roman(InteractiveScene):
    def construct(self):
        t = TexText("A")
        t2 = TexText("B")
        self.play(Transform(t, t2))
        self.wait()