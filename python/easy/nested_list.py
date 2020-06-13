if __name__ == '__main__':
    master_sheet = []
    scoresheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        master_sheet += [[name, score]]
        scoresheet += [score]

    sorted_scores = sorted(scoresheet)
    if sorted_scores[1] != sorted_scores[0]:
        runnerUp = sorted_scores[1]
    elif sorted_scores[1] == sorted_scores[0]:
        if sorted_scores[1] != sorted_scores[2]:
            runnerUp = sorted_scores[2]
        elif sorted_scores[1] == sorted_scores[2]:
            runnerUp = sorted_scores[3]

    for name, score in sorted(master_sheet):
        if score == runnerUp:
            print(name)
