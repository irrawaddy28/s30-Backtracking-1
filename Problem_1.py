'''
39 Combination Sum
https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times. 7 is a candidate, and 7 = 7. These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Solution:
1. Recursion:
case 0: don't pick the number at the ith index (array[i]), and do a recursion on the next number at index i + 1 (array[i+1])

case 1: pick the number at the ith index (array[i]), and do a recursion on the same number (array[i]) since repetitions of a number are allowed

Let K = target sum/min(array), then
Time is 2^K because for every element in the array, the tree splits into two subtrees (dont pick subtree and pick subtree)
Space is K because the recursion depth is log 2^K  = K

Time: O(2^K), Space: O(K)
'''

def combinationSum(arr, target_sum):
    ''' Time: O(2^K), Space: O(log 2^K) = O(K), K = target sum/min(array) '''
    def recurse(arr, curr_sum, target_sum, i, path):
        if curr_sum == target_sum:
            subsets.append(path.copy())
            return #True
        elif curr_sum > target_sum:
            return #False

        if i >= N:
            return #False

        # case 0: don't pick arr[i]
        recurse(arr, curr_sum, target_sum, i+1, path)

        # case 1: pick arr[i] (but don't increment index since repetitions of arr[i] are allowed)
        path.append(arr[i])
        recurse(arr, curr_sum + arr[i], target_sum, i, path)
        path.pop()

        return #case_0 or case_1

    if not arr:
        return []

    N = len(arr)
    path=[]
    subsets=[]
    recurse(arr, 0, target_sum, 0, path)
    return subsets

def run_combinationSum():
    tests = [([10,12,15,6,19,20], 16, [[10,6]]),
             ([2,3,6,7], 7, [[2,2,3],[7]]),
             ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
             ([2], 1, []),
    ]
    for test in tests:
        arr, target_sum, ans = test[0], test[1], test[2]
        subsets = combinationSum(arr, target_sum)
        a = [sorted(l) for l in sorted(ans)]
        b = [sorted(l) for l in sorted(subsets)]
        print(f"\nArray = {arr}")
        print(f"Target Sum = {target_sum}")
        print(f"Combinations = {subsets}")
        print(f"Pass: {a == b}")

run_combinationSum()
