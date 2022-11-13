def check_answer(right_res, user_ans):
    answer = False
    if (user_ans == right_res):
        print("Correct!")
        answer = True
    else:
        print(f"{user_ans} is wrong answer ;(. Correct answer was {right_res}.")
        answer = False
    return answer
