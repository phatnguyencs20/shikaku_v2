import sys
import glob
from shikaku.shikaku import Shikaku

if __name__ == '__main__':
    for filename in sorted(glob.glob("puzzles/*.txt")):
        #filename = "puzzles/puzzle0.txt"
        s = Shikaku(filename)
        s.draw("test/input.png")
        s.solve(heuristic=False, info=True, output_image="test/blind_search.png")
        print("\n\n")
        s.solve(heuristic=True, info=True, output_image="test/heuristic_search.png")
        #break