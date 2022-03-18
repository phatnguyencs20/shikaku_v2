import sys
from shikaku.shikaku import Shikaku

if __name__ == '__main__':
    s = Shikaku(sys.argv[1])
    s.draw("test/input.png")
    s.solve(heuristic=False, info=True, output_image="test/output.png")