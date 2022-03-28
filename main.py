import glob
from shikaku.shikaku import Shikaku

if __name__ == '__main__':
    for filename in sorted(glob.glob("puzzles/*.txt")):
        filename = "puzzles/32.txt"
        s = Shikaku(filename)
        puzzle_id = str(filename[8:10])
        s.draw("testcases_result/" + puzzle_id + "_input.png")
        s.solve(
            log="testcases_result/" + puzzle_id + "_log.txt",
            output_image="testcases_result/" + puzzle_id + "_output.png"
        )
        break