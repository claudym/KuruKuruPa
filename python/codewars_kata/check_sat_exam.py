def check_exam(answers, test):
    score = 0
    for i in range(len(answers)):
        if test[i] == answers[i]:
            score += 4
        elif test[i] == '':
            pass
        else:
            score -= 1
    return score if score >= 0 else 0 