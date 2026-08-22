from manimlib import *


class TestMatchingStrings(Scene):
    def construct(self):
        source = Tex("x + x")
        target = Tex("x^2 + x")

        source.to_edge(LEFT)
        target.to_edge(RIGHT)

        self.add(source)
        self.wait()

        # Get the two x occurrences from source
        source_x1 = source[0]
        source_x2 = source[2]

        # Get the two x occurrences from target
        target_x1 = target[0]
        target_x2 = target[3]

        self.play(
            TransformMatchingStrings(
                source,
                target,
                key_map={"x": 2},
                matched_pairs=[
                    (source_x1, target_x1),
                    (source_x2, target_x2),
                ],
            )
        )

        self.wait()