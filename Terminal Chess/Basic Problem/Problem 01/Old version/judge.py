from submission import get_move
import filecmp 
import threading
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

# Create a function that execute the submitted code
def execute_submitted_function():
    try:
        # Read the input from the file 'input.txt'
        with open('input.txt', 'r') as f:
            # Read the number of test cases
            T = int(f.readline())
            # Open the file 'submission.txt' for writing
            with open('submission.txt', 'w') as g:
                # Loop through each test case
                for _ in range(T):
                    # Read the board dimensions and the king positions
                    M, N = map(int, f.readline().split())
                    x1, y1, x2, y2 = map(int, f.readline().split())
                    # Calculate the minimum number of move
                    moves = get_move(M, N, x1, x2, y1, y2)
                    # Write the output to the file 'submission.txt'
                    g.write(str(moves) + '\n')
        # Stop the timer
        timer.cancel()
        # Check whether the submission is correct or not
        result = filecmp.cmp("submission.txt", "output.txt")
        print('Accepted' if result else 'Wrong Answer')
    except Exception as ex:
        print(f"Error: {ex}")

# Define a function that cancels a thread
def cancel_thread(thread):
    if thread.is_alive():
        print("Time limit exceeded")
        # Terminate the thread
        thread._tstate_lock.release()
        thread._stop()

# Create a worker thread that runs your function
worker = threading.Thread(target=execute_submitted_function)
# Set the worker as a daemon thread so it exits when the main thread exits
worker.daemon = True

# Create a timer thread that cancels the worker after 5 seconds
timer = threading.Timer(5, cancel_thread, args=(worker,))
# Set the timer as a daemon thread so it exits when the main thread exits
timer.daemon = True

# Start both threads
worker.start()
timer.start()

# Wait for both threads to finish
worker.join()
timer.join()