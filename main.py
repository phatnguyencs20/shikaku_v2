import glob
from shikaku.shikaku import Shikaku

if __name__ == '__main__':
    
    #solve all puzzles
    with open("benchmark.txt", 'w') as f:
        f.write("Analytic information:\n\n")
    
        num_puzzles = 0

        time_speed_up = 0
        space_saved = 0

        for filename in sorted(glob.glob("puzzles/*.txt")):
            s = Shikaku(filename)
            puzzle_id = str(filename[8:10])
            s.draw("testcases_result/" + puzzle_id + "_input.png")
            h, w, time_h, states_h, time_b, states_b, solution = s.solve(
                log="testcases_result/" + puzzle_id + "_log.txt",
                benchmark=True,
                output_image="testcases_result/" + puzzle_id + "_output.png"
            )

            if solution == True and time_h > 0 and time_b > 0:
                time_speed_up += time_b / time_h
                space_saved += states_b / states_h

                num_puzzles += 1

        f.write("Average time speed up: {} times\n".format(round(time_speed_up / num_puzzles, 4)))
        f.write("Average states saved: {} times\n".format(round(space_saved / num_puzzles, 4)))
    
    #solve a particular puzzle
    '''filename = "puzzles/01.txt"
    s = Shikaku(filename)
    s.draw("sample/input.png")
    s.solve(
        log="sample/log.txt",
        benchmark=None,
        output_image="sample/output.png"
    )'''