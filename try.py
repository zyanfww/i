from manimlib import *


class TestMatchingStrings(Scene):
    def construct(self):
        source = Tex("x + y + z")        
        target = Tex("x - y - z")

        #source.to_edge(LEFT)
        #target.to_edge(RIGHT)

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