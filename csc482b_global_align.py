# -*- coding: utf-8 -*-
"""csc482b_global_align.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14tjyOzK1wS2l8exUnO1r9VcIfg2GREAt
"""

# global gap penality and scoring numbers
match = 2
nonMatch = -1
gapPen = -2

# Helper function to initialize a matrix 1 greater than the sequence lengths
# Initializes the spaces to 0
# Returns a list of lists (matrix) full of 0s
def initializeMatrix(xLen, yLen):
  return [[0] * (yLen + 1) for ys in range(xLen)]

# Helper Function checks to see if the pair in the sequences are matching or not 
# Returns a Bool
def matchingPair(s1, s2, xs, ys):
  if s1[ys - 1] == s2[xs - 1]:
    return True
  return False

# Fills out the matrix with the appropiate numbers for a global alignment
# Follows the needleman-wunsch algorithm (used google for pseudo code)
# Takes in the sequences s1 and s2 found in the in files found in main
#   as well as the matrix created from initalizing it all to 0
# Then it sends it to a traceback algorithm to find the alignments
def completeMatrix(s1, s2, mtxXY):
  for i in range(len(s2) + 1):
    mtxXY[0][i] = gapPen * i
  for j in range(len(s1)):
   mtxXY[j][0] = gapPen * j

  # traverse through the matrix
  for xs in range(1, len(s2) + 1):
    for ys in range(1, len(s1)):
      if matchingPair(s1, s2, xs, ys):
        diag = mtxXY[ys - 1][xs - 1] + match
      else:
        diag = mtxXY[ys - 1][xs - 1] + nonMatch
      left = mtxXY[ys][xs - 1] + gapPen
      up = mtxXY[ys - 1][xs] + gapPen
      mtxXY[ys][xs] = max(diag, left, up)  
  
  # traceback from the bottom right corner max and go back until 0,0
  traceResult = []
  traceback(traceResult, s1, s2, xs, ys, mtxXY)
  # Print the results
  print("output 1: \n" + str(mtxXY[ys][xs]))
  print("\noutput 2: ")
  printPrettyMatrix(mtxXY)
  print("\noutput 3 : \n" + str(traceResult[0][1]) + "\n" + str(traceResult[0][0]))
  if len(traceResult) > 1:
    print("\noutput 4: \nYES")
  else:
    print("\noutput 4: \nNO")
  print("\noutput 5: \n" + str(len(traceResult)))
  for i in range(len(traceResult)):
    print(traceResult[i][1])
    print(traceResult[i][0])
    print("\n")
  return mtxXY

# Traceback function to find the right algorithms
# Checks to see if the current cell is created from either diagonal, left, or the one above
# Recursively attaches the right variables from the sequences to an array of tuples
def traceback(traceResult, s1, s2, xs, ys, mtxXY, stringApp='', stringApp2=''):
  if xs > 0 or ys > 0:
    checkNum = mtxXY[ys][xs]
    if matchingPair(s1, s2, xs, ys):
      diag = checkNum == (mtxXY[ys - 1][xs - 1] + match)
    else:
      diag = checkNum == (mtxXY[ys - 1][xs - 1] + nonMatch)
    left = checkNum == (mtxXY[ys][xs - 1] + gapPen)
    up = checkNum == (mtxXY[ys - 1][xs] + gapPen)
    if diag:
      traceback(traceResult, s1, s2, xs - 1, ys -1, mtxXY, s2[xs - 1] + stringApp, s1[ys - 1] + stringApp2)
    if left:
      traceback(traceResult, s1, s2, xs - 1, ys, mtxXY, s2[xs -1] + stringApp, '-' + stringApp2)
    if up: 
      traceback(traceResult, s1, s2, xs, ys -1, mtxXY, '-' + stringApp, s1[ys - 1] + stringApp2)
  else:
    traceResult.append((stringApp, stringApp2))

# Helper function to print out the matrix nicely
def printPrettyMatrix(mtxXY):
  return print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in mtxXY]))

def main():t
  # Change the input to whatever input file you need it to be. Jupyter deletes files after session
  # Ensure that the input is 2 lines long and has 1 sequence per line I didn't check that however
  # We do check if sequence lengths are between 5 and 50 
  file = open('2.in', 'r')
  s1 = file.readline()
  s2 = file.readline()
  # in case the sequences have spaces anywhere in the line.
  # Need to remove or else the matrix creation is messed up
  s1 = s1.replace(" ", "")
  s2 = s2.replace(" ", "")
  # Assignment doc said between 5 and 50 so if its less than 5 or greater than 50
  # We don't process it
  if (len(s1) < 5 or len(s1) > 50) or (len(s2) < 5 or len(s2) > 50):
    print("sequence 1 or sequence 2 has length less than 5 or more than 50")
  else:
    s1s2Matrix = initializeMatrix(len(s1), len(s2))
    s1s2PathMatrix = initializeMatrix(len(s1) + 1, len(s2) + 1)
    completeMatrix(s1, s2, s1s2Matrix)

main()

"""# New Section"""