import random

def get_position(M,N):
  # returns a valid position (x,y) on the board of size MxN
  x = random.randint(1,M)
  y = random.randint(1,N)
  return (x,y)

def get_moves(M,N,x1,y1,x2,y2):
  # returns the minimum number of moves required by the king
  dx = abs(x2-x1)
  dy = abs(y2-y1)
  return max(dx,dy)

T = 1000 # number of test cases
input_file = open("input.txt","w") # create and open the input file
output_file = open("output.txt","w") # create and open the output file
input_file.write(str(T)+"\n") # write the first line to the input file

for _ in range(T):
  M = random.randint(1,10**9) # board width
  N = random.randint(1,10**9) # board height
  x1,y1 = get_position(M,N) # initial position of the king
  x2,y2 = get_position(M,N) # final position of the king
  moves = get_moves(M,N,x1,y1,x2,y2) # minimum number of moves
  input_file.write(str(M)+" "+str(N)+"\n") # write the first line of each test case to the input file
  input_file.write(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)+"\n") # write the second line of each test case to the input file
  output_file.write(str(moves)+"\n") # write the output for each test case to the output file

input_file.close() # close the input file
output_file.close() # close the output file