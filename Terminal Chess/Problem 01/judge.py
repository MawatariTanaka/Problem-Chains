from submission import get_minimum_move
from os import system, name
import threading
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

def condition_func_problem_01(test_func, case):
    return test_func(*case[0]) == case[1]

def generate_test_case_list(n):
    test_case_list = []
    test_case_list.append(((1, 1, 1, 1, 1, 1), 0))
    test_case_list.append(((10**9, 10**9, 10**9, 10**9, 10**9, 10**9), 0))
    test_case_list.append(((10**9, 10**9, 10**9, 10**9, 1, 1), 10**9 - 1))
    test_case_list.append(((10**9, 10**9, 1, 1, 10**9, 10**9), 10**9 - 1))
    test_case_list.append(((10**9, 10**9, 500000000, 500000000, 500000001, 500000001), 1))
    for i in range(n - len(test_case_list)):
        M = random.randint(1, 10**9)
        N = random.randint(1, 10**9)
        x1 = random.randint(1, M)
        y1 = random.randint(1, N)
        x2 = random.randint(1, M)
        y2 = random.randint(1, N)
        answer = max(abs(x2 - x1), abs(y2 - y1))
        test_case_list.append(((M, N, x1, y1, x2, y2), answer))
    return test_case_list

def execute_submitted_function(test_number, cases, submitted_function, test_function):
    status = 'Answer Accepted'
    try:
        for case in cases:
            result = test_function(submitted_function, case)
            if not result:
                status = 'Wrong Answer'
                break
        timer.cancel()
        judge_test.append(status)
        print(f"- Test {test_number}: {status}.")
    except Exception as ex:
        print(f"- Test {test_number}: {ex}")
def cancel_thread(test_number, thread):
    print(f"- Test {test_number}: Time limit exceeded.")
    if thread.is_alive():
        thread._tstate_lock.release()
        thread._stop()

total_number_of_tests = 10
judge_test = []
print(f'Running on {total_number_of_tests} tests:')
for i in range(total_number_of_tests):
    test_cases_problem_01 = generate_test_case_list(1000)
    worker = threading.Thread(target=execute_submitted_function, args=(i+1, test_cases_problem_01, get_minimum_move, condition_func_problem_01))
    worker.daemon = True
    timer = threading.Timer(5, cancel_thread, args=(i+1, worker))
    timer.daemon = True
    worker.start()
    timer.start()
    worker.join()
    timer.join()

total_correct = 0
for i in judge_test:
    total_correct += int(i == 'Answer Accepted')
if total_correct == total_number_of_tests:
    print('All tests passed.')
else:
    print(f'{total_correct} of {total_number_of_tests} tests passed.')