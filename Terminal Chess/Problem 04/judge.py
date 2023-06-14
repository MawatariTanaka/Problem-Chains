from submission import min_moves_bishop
from os import system, name
import threading
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

def test(total_number_of_tests, number_of_subtests, submitted_function, condition_function):
    judge_test = ['']*total_number_of_tests
    def execute_submitted_function(test_number, cases, submitted_function, test_function):
        status = 'Answer Accepted'
        try:
            for case in cases:
                result = test_function(submitted_function, case)
                if not result:
                    status = 'Wrong Answer'
                    break
            timer.cancel()
            if not judge_test[test_number-1]:
                print('Case {}: {}'.format(test_number, status))
                judge_test[test_number-1] = status
        except Exception:
            timer.cancel()
            if not judge_test[test_number-1]:
                print('Case {}: Runtime Error'.format(test_number))
                judge_test[test_number-1] = 'Runtime Error'
            
    def cancel_thread(test_number, thread):
        if not judge_test[test_number-1]:
            print('Case {}: Time Limit Exceeded'.format(test_number))
            judge_test[test_number-1] = 'Time Limit Exceeded'
        if thread.is_alive():
            thread._tstate_lock.release()
            thread._stop()

    print(f'Running on {total_number_of_tests} tests:')
    for i in range(total_number_of_tests):
        cases = generate_test_cases(number_of_subtests)
        worker = threading.Thread(target=execute_submitted_function, args=(i+1, cases, submitted_function, condition_function))
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

def condition_func_problem_04(test_func, case):
    return test_func(*case[0]) == case[1]

def generate_test_cases(n):
    test_cases = [((1, 1, 1, 1, 1, 1), 0), ((2, 2, 1, 1, 2, 2), 1), ((2, 2, 1, 1, 1, 2), -1), ((2, 2, 1, 2, 2, 1), 1), ((10**9, 10**9, 1, 1, 10**9, 10**9), 1), ((10**9, 10**9, 1, 1, 10**9, 10**9 - 1), -1), ((10**9, 10**9, 1, 1, 10**9 - 1, 10**9), -1), ((10**9, 10**9, 1, 10**9, 10**9, 1), 1), ((10**9, 10**9, 10**9, 1, 1, 10**9), 1), ((10**9, 10**9, 10**9, 10**9, 1, 1), 1)]
    test_cases += [(((M:=random.randint(1,10**9),N:=random.randint(1,M),(x1:=random.randint(1,M)),(y1:=random.randint(1,N)),(x2:=random.randint(1,M)),(y2:=random.randint(1,N)))),0 if (x1, y1) == (x2, y2) else -1 if (x1 + y1) % 2 != (x2 + y2) % 2 else 1 if abs(x1 - x2) == abs(y1 - y2) else 2) for _ in range(n-15)]
    return test_cases

test(10, 10, min_moves_bishop, condition_func_problem_04)