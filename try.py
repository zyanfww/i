from manimlib import *


class TestMatchingStrings(Scene):
    def construct(self):
        source = Tex("x + y = 2")        target = Tex("x = 2 - y")

        source.to_edge(LEFT)
        target.to_edge(RIGHT)

        self.add(source)
        self.wait()

        self.play(
            TransformMatchingStrings(
                source,
                target,
                key_map={"+": "-"},
            )
        )

        self.wait()