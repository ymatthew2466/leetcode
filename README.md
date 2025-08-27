File names are LeetCode problem numbers ( 1.py == Two Sum )

Problems are organized by NeetCode categories

## 8/26

Count = 3

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

Count = 4

- Arrays: 485, 567
- Sliding Window: 2379, 1984,

### Notes

Sliding Window: don't overcomplicate, simply track the difference when left is shrunk, and right is expanded

## 8/24

Count = 3

- Arrays: 438, 605
- Sliding Window: 121

### Notes

Review sliding window technique: shrink leftmost, expand rightmost

## 8/23

Count = 4

- Arrays: 49
- Math/Geometry: 2807, 57
- Backtracking: 46

### Note

redo 49 using ASCII chars, learn how to sort into buckets, string slice/concat with [:], list comprehension

## 8/21

Count = 8

- Arrays: 1408, 1701, 2073, 3110,
- Two Pointers: 392, 844, 2486
- Backtracking: 17
