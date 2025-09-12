## 9/12

n=1

- Graph: 695

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
