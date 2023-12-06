# assignment-03

# no other imports needed
from collections import defaultdict
import math

### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

#### Iterative solution
def parens_match_iterative(mylist):
    
    counter = iterate(parens_update, 0, mylist)
    return (counter == 0)


def parens_update(current_output, next_input):
    
    if next_input == '(':
      current_output += 1
    elif next_input == ')':
      current_output -= 1
    if current_output < 0:
        return -1
    return current_output
  
  
def test_parens_match_iterative():
  assert parens_match_iterative(['(', ')']) == True
  assert parens_match_iterative(['(']) == False
  assert parens_match_iterative([')']) == False
  


#### Scan solution

def parens_match_scan(mylist):
    mapped_list = list(map(paren_map, mylist)) 
    cumulative_sum, total_sum = scan(lambda x, y: x + y, 0, mapped_list) 
    min_value = reduce(min_f, float('inf'), cumulative_sum) 
    return (total_sum == 0) and (min_value >= 0)
  
def scan(f, id_, a):
    
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    
    mid = len(mylist) // 2
    left_half = mylist[:mid]
    right_half = mylist[mid:]
  
    R1, L1 = parens_match_dc_helper(left_half)
    R2, L2 = parens_match_dc_helper(right_half)
    if L1 > R2:
      return (R1, (L1 - R2) + L2)
    else:
      return ((R2 - L1) + R1, L2)
    

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
