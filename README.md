## 9/30

n=2

- Graph: 2658, 133

### Nodes

#### Graph

- Dictionaries are very helpful for graph questions
  - use to retrieve data at each node
- Adjacency lists also great in dict

## 9/29

n=1

- Binary Search: 1011

### Notes

- Check low/high bounds if anything is wrong
  - I.E. low should be max weight of any package

## 9/28

n=1

- Arrays: 3105

### Notes

- Think about how to reduce complexity (variables, if statements)
  - How can some vars/count represent other states?

## 9/27

n=1

- Stack: 496

## 9/26

n=1

- Binary Search: 2300

### Notes

- Nest binary search inside O(N) iteration for O(N \* logN)

## 9/25

n=1

- Binary Search: 441

### Notes

- Upper bound can be vague

## 9/24

n=4

- Binary Search: 875, 540, 74, 153

### Notes

- THINK: HOW TO SPLIT DATA INTO HALVES
- return to 153 -- fix bounds errors

## 9/23

n=3

- Binary Search: 69, 367, 162

### Notes

#### Binary Search

- Sometimes consider 1 step at a time for which direction to move
  - local maxima question, if curr >= right, peak can be at curr or left
    - if right > curr, peak must be right

## 9/22

n=3

- Binary Search: 904, 35, 374

### Notes

#### Binary Search

- https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8/
- Template returns first index where the condition is true
  - for 904, it returns first index where nums[index]>=target
  - We know (>=) condition, so we must check (==) condition explicitly
- def condition(mid): boolean condition that determines the first valid index
- if condition(mid): what we have is valid, so look at left to narrow it down
- else: current is not valid (and nothing to the left is valid either), so look at right to find it

## 9/21

n=1

- Two Pointer: 1968

## 9/20

n=1

- Two Pointer: 15

### Notes

#### Two Pointer

- to avoid duplicates, set left to i+1
  - also, use while loop to increment left/decrement right until we hit a fresh value (avoid set to use less memory)

## 9/19

n=1

- Binary Search: 658

### Notes

- Must review basic algo and redo 658

## 9/18

n=1

- Arrays: 1 (lol)

## 9/17

n=2

- Completed JPMorgan OA

## 9/16

n=4

- Completed Capital One OA
  - practice DP

## 9/15

n=1

- Sliding Window: 904

### Notes

#### Sliding Window

- while loop inside for-loop to shrink window
- can remove stuff from dict to "shrink" window
  - "del dict[key]" to remove key

## 9/14

n=2

- Two Pointer: 443, 2109

### Notes

#### Arrays

- [:] is slice that selects all elts from list
  - arr[:] = arr2, keeps same list object but overwrites everything to arr2

## 9/13

n=2

- Arrays: 1299

- Graph: 130

### Notes

#### BFS

- Mark the starting cell as visited RIGHT AFTER adding to queue
  - This is general pattern: add to visited after adding to queue

## 9/12

n=2

- Graph: 695, 994

### Notes

#### Multi-source BFS

- Add all starting points to queue BEFORE running BFS algorithm
- Inside main while loop (q>0),
  - For-loop thru everything in queue -> THIS IS 1 "LEVEL"
    - Popleft and for-loop thru neighbors

## 9/11

n=1

- Graph: 200

## 9/10

n=1

- Graph: 733

## 9/9

n=1

- Graph: 463

### Notes

- BFS: ALWAYS mark nodes as visited WHEN ADDING TO QUEUE
- use popleft() for queue rather than pop()
- CONVERT TO DFS: Turn deque into [] and pop() instead of popleft()

## 9/8

n=1

- Linked List: 206

### Notes

- Try LL problems recursively next time. My recursion needs some practice

## 9/7

n=2

- Arrays: 3442 (freq array)
- Two Pointer: 905

### Notes

- Good to know when to use frequency array
- Sometimes, we instantiate a new array of SPECIFIED LENGTH to match problem

## 9/6

n=3

- Arrays: 1929, 916, 28

### Notes

- Identify when to use a freqency array for characters
  - freq[i] is # of char appearances, where 0 < i < 26
- Identify patterns, I.E. 916
  - Instead of checking each word2 individually, we notice word1 must conform to the highest letter frequency in all of words2

## 9/5

n=2

- Arrays: 2559
- Sliding Window: 1052

### Notes

- Prefix sum is array that counts the valid number from index 0 to some index.
  - prefix[i] is sum of valid words, from 0 to i-1
  - to find num of valid in range [l, r], we do prefix[r+1] - prefix[l]

## 8/27

n=2

Completed Amazon OA

1. 6/15 test cases passed. However, I identified the edge case and printed when I got there. I just couldn't figure out how to fix it. I explained my intuition on how I would if I had more time.
2. 9/15 test cases passed. Graph question on shortest traversal time. Ran out of time.

### Notes

That was embarassing, and this will never happen to me again.

## 8/26

n=3

- Arrays: 2001
- Sliding Window: 1343
- Backtracking: 78

### Notes

#### Backtrack:

- Use fresh starter values (like phone combinations) when we want FIXED LENGTH.
  - OR, when each position in result has diff constraints/options (phone digits: diff digits == diff letters)
- Use empty start and index `backtrack([], 0)` when doing ALL possible combos.
  - OR, when we're looking at INCLUDE/EXCLUDE decision for each element
- Claude: If you can describe the problem as "for each element in the input, decide whether to include it," use the empty start approach. If you can describe it as "fill each position/slot with valid options," use fresh starters.

## 8/25

n=4

- Arrays: 485, 567
- Sliding Window: 2379, 1984,

### Notes

Sliding Window: don't overcomplicate, simply track the difference when left is shrunk, and right is expanded

## 8/24

n=3

- Arrays: 438, 605
- Sliding Window: 121

### Notes

Review sliding window technique: shrink leftmost, expand rightmost

## 8/23

n=4

- Arrays: 49
- Math/Geometry: 2807, 57
- Backtracking: 46

### Note

redo 49 using ASCII chars, learn how to sort into buckets, string slice/concat with [:], list comprehension

## 8/21

n=8

- Arrays: 1408, 1701, 2073, 3110,
- Two Pointers: 392, 844, 2486
- Backtracking: 17
