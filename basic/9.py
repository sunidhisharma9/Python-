def max2(a, b):
  '''
     Objective: Find the larger of the two number from the function
     Input:
         a: First numeric number
         b: Second mumeric number
     Output: Larger of the two number from the function
  '''
  #Approach: If a is greater then b, a is lager or else b have the larger value

  if a>b:
      return a
  else:
      return b

def maxlst(lst):
  '''
     Objective: Find the largest number from the list
     Input:
       lst: List of any naturel numbers
     Output: Largest number from the function
  '''
  #Approach: If a is greatest from the given list

  if lst==[]:
      return'null'
  elif len(lst)==1:
      return lst[0]
  else:
      return max2(lst[0], maxlst(lst[1:]))
 
 

