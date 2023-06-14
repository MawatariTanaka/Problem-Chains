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

def condition_func_problem_02(test_func, case):
    return test_func(*case[0]) == case[1]

def generate_test_cases(n):
    test_case=[((1,1,1,1,1,1),0),((10**9,10**9,10**9,10**9,10**9,10**9),0),((10**9,10**9,10**9,10**9,1,10**9),1),((10**9,10**9,10**9,10**9,10**9,1),1),((10**9,10**9,10**9,10**9,1,1),2),((5,5,5,5,5,5),0),((5,5,5,5,3,3),2),((5,5,5,5,3,5),1),((5,5,5,5,5,3),1),((5,5,5,5,1,1),2),((3*7*11*13*17*19*23*29*31*37+1,3*7*11*13*17*19*23*29*31*37+2,3*7*11*13*17*19*23*29*31+3, 3*7*11*13*17*19+4,3+5,7+6),2)]
    test_case+=[((M:=random.randint(1,10**9),N:=random.randint(1,10**9),x1:=random.randint(1,M),y1:=random.randint(1,N),x2:=random.randint(1,M),y2:=random.randint(1,N)),0 if x1==x2 and y1==y2 else 1 if x1==x2 or y1==y2 else 2) for _ in range(n-11)]
    return test_case

test(10, 1000, get_minimum_move, condition_func_problem_02)