import glob
from shikaku.shikaku import Shikaku

if __name__ == '__main__':
    for filename in sorted(glob.glob("puzzles/*.txt")):
        filename = "puzzles/01.txt"
        s = Shikaku(filename)
        puzzle_id = str(filename[8:10])
        s.draw("testcases_result/" + puzzle_id + "_input.png")
        s.solve(
            heuristic=True,
            info=False,
            log="testcases_result/" + puzzle_id + "_heuristic_search.txt",
            output_image="testcases_result/" + puzzle_id + "_heuristic_search.png"
        )
        #s.solve(
            #heuristic=False,
            #info=False,
            #log="testcases_result/" + puzzle_id + "_blind_search.txt",
            #output_image="testcases_result/" + puzzle_id + "_blind_search.png"
        #)
        break