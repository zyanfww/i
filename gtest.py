from manimlib import *

class Test(InteractiveScene):
    def construct(self):
        s = Square()
        s.set_width(FRAME_WIDTH - 1)
        s.set_fill([GREY_D, GREY_A], 1.0, gradient_direction=UR)
        self.add(s)