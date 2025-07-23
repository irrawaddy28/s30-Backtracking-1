'''
282 Expression Add Operators
https://leetcode.com/problems/expression-add-operators/description/

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Note that a number can contain multiple digits.

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.


Constraints:
1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1

1. Recursion:
case 0: don't pick any operator, just append the next digit, do a recursion on the next digit (array[i+1])
case 1: pick operator +, append the next digit, do a recursion on the next digit (array[i+1])
case 2: pick operator -, append the next digit, do a recursion on the next digit (array[i+1])
case 3: pick operator *, append the next digit, do a recursion on the next digit (array[i+1])

If N = number of digits in string, then
Time is 4^N since for each digit in string, we have 4 choices to make (cases 0,1,2,3,4). Space is O(depth) = O(log 4^N) = O(N)

Time: O(4^N), Space: O(N)
'''

def addOperators(num, target):
    ''' Time: O(4^N), Space: O(N), N = number of digits in string '''
    def recurse(num, target, i, path):
        # if eval() is internally implemented using stack, then eval() takes Time: O(N), Space: O(N)
        curr_sum = eval(path)

        if curr_sum == target and i == N:
            expresssions.append(path)
            return

        if i >= N:
            return

        # case 0: don't pick any operator, just append the next digit
        if i == 1 and path[-1] == '0':
            # eg. if num = "015" and path="0", then don't build a path "01"
            pass
        elif i >= 2 and path[-1] == '0' and path[-2] in ["+", "-", "*"]:
            # eg. if num = "105" and path = 1+0, then don't build a path using "1+05"
            pass
        else:
            recurse(num, target, i+1, path + num[i])

        # case 1: pick '+'
        recurse(num, target, i+1, path + "+" + num[i])

        # case 2: pick '*'
        recurse(num, target, i+1, path + "*" + num[i])

        # case 3: pick '-'
        recurse(num, target, i+1, path + "-" + num[i])

        return

    if not num:
        return []

    N = len(num)
    path=""
    expresssions=[]
    recurse(num, target, 1, path + num[0])
    return expresssions

def run_addOperators():
    tests = [ ("123", 6, ['1+2+3', '1*2*3']),
              ("232", 8, ['2*3+2', '2+3*2']),
              ("124", 9, ['1+2*4']),
              ("125", 7, ['1*2+5', '12-5']),
              ("015", 6,  ['0+1+5']), # cannot have expr "01+5"
              ("015", 5,  ['0+1*5', '0*1+5']), # cannot have expr "01*5"
              ("015", 15,  ["0+15"]), # cannot have expr "015"
              ("105", 15,  ['10+5']),
              ("00", 0, ["0+0", "0-0", "0*0"]),
              ("1111", -1, ["1*1-1-1","1-1*1-1","1-1-1*1"]),
              ("3456237490", 9191, []),
              ("1",1,['1']),
    ]
    for test in tests:
        num, target, ans = test[0], test[1], test[2]
        expressions = addOperators(num, target)
        print(f"\nNumber String = {num}")
        print(f"Target Sum = {target}")
        print(f"Expressions = {expressions}")
        print(f"Pass: {sorted(ans) == sorted(expressions)}")

run_addOperators()
