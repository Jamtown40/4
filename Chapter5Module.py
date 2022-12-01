# Prof. Candido
# Module Sample

# Returns the smallest of 2 numbers:
def min_number(nNumber1, nNumber2):
     nSmallest = nNumber1
     if nNumber2 < nNumber1:
          nSmallest = nNumber2

     return nSmallest
          
# Returns the largest of 2 numbers:
def max_number(nNumber1, nNumber2):
     nBiggest =  nNumber1
     if nNumber2 > nNumber1:
          nBiggest = nNumber2

     return nBiggest

# Average 2 numbers:
def avg_numbers(nNumber1, nNumber2):

     nAvg = nNumber1 + nNumber2
     nAvg = nAvg / 2

     return nAvg

# Sum 2 numbers:
def sum_numbers(nNumber1, nNumber2):

     nSum = nNumber1 + nNumber2
     return nSum
