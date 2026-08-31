# Python DSA Lab

A structured Python repository for learning, implementing, testing, and documenting Data Structures and Algorithms.

This repository contains practical implementations of common data structures and algorithms, along with automated tests and complexity analysis.

The goal is to strengthen Python programming, problem-solving, algorithmic thinking, and technical interview fundamentals.

---

## Purpose

The purpose of this repository is to:

- Strengthen Python programming fundamentals
- Practice Object-Oriented Programming (OOP)
- Understand how common data structures work
- Implement important algorithms from scratch
- Improve logical thinking and problem-solving skills
- Understand time and space complexity
- Practice writing clean and testable code
- Build a practical reference for technical interviews

This repository is primarily a **Python DSA learning, practice, and interview-preparation repository**.

---

## Technology Stack

- Python 3
- Object-Oriented Programming (OOP)
- Python Type Hints
- pytest
- Git
- GitHub

---

## Completed Topics

### Data Structures

- Arrays
- Strings
- Linked Lists
- Stacks
- Queues
- Hash Tables

### Searching Algorithms

- Linear Search
- Iterative Binary Search
- Recursive Binary Search

### Sorting Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

---

## Testing

The repository uses **pytest** for automated testing.

Tests cover:

- Correct results
- Edge cases
- Empty inputs
- Missing values
- Invalid operations
- Data structure behavior
- Algorithm correctness

### Current Test Status

**87 / 87 tests passing**

```text
87 passed
```

Run the complete test suite with:

```bash
pytest
```

---

## Project Structure

```text
python-dsa/
│
├── arrays/
│   └── array_operations.py
│
├── strings/
│   └── string_operations.py
│
├── linked_lists/
│   └── linked_list.py
│
├── stacks/
│   └── stack.py
│
├── queues/
│   └── queue.py
│
├── hash_tables/
│   └── hash_table.py
│
├── searching/
│   └── search_algorithms.py
│
├── sorting/
│   └── sort_algorithms.py
│
├── recursion/              # Planned
├── trees/                  # Planned
├── heaps/                  # Planned
├── graphs/                 # Planned
├── greedy/                 # Planned
├── dynamic_programming/   # Planned
│
├── problems/               # Planned
├── playground/             # Planned
├── docs/                   # Planned
│
├── tests/
│
├── README.md
├── pyproject.toml
└── .gitignore
```

---

## How the Repository Is Organized

Each major topic has its own Python package.

For example:

```text
arrays/
└── array_operations.py

tests/
└── test_array_operations.py
```

The implementation file contains the actual data structure or algorithm.

The corresponding test file verifies that the implementation works correctly.

This keeps the repository organized and makes each topic easy to understand and revisit.

---

## Development Approach

Every topic follows the same development process:

```text
Plan
  ↓
Create Structure
  ↓
Implement
  ↓
Write Tests
  ↓
Run pytest
  ↓
Fix Issues
  ↓
Commit
  ↓
Push to GitHub
```

The goal is not only to write algorithms, but also to practice a professional development workflow.

---

# Current Roadmap

## Phase 1 — Core Data Structures

Completed:

- Arrays
- Strings
- Linked Lists
- Stacks
- Queues
- Hash Tables

**Status: COMPLETED**

---

## Phase 2 — Searching

Completed:

- Linear Search
- Iterative Binary Search
- Recursive Binary Search

**Status: COMPLETED**

---

## Phase 3 — Sorting

Completed:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

**Status: COMPLETED**

---

## Phase 4 — Recursion

Planned topics:

- Recursion fundamentals
- Base cases
- Recursive problem solving
- Recursive searching
- Recursive traversal
- Recursion-based problems

**Status: PLANNED**

---

## Phase 5 — Trees

Planned topics:

- Binary Trees
- Binary Search Trees
- Preorder Traversal
- Inorder Traversal
- Postorder Traversal
- Level-order Traversal
- Searching
- Insertion
- Tree-based problems

**Status: PLANNED**

---

## Phase 6 — Heaps

Planned topics:

- Min Heap
- Max Heap
- Heap insertion
- Heap extraction
- Heapify
- Priority Queue concepts
- Heap-based problems

**Status: PLANNED**

---

## Phase 7 — Graphs

Planned topics:

- Graph representation
- Adjacency List
- Adjacency Matrix
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Visited-node tracking
- Connected components
- Basic path exploration

**Status: PLANNED**

---

## Phase 8 — Greedy Algorithms

Planned topics:

- Greedy strategy
- Activity Selection
- Interval-based problems
- Representative greedy problems
- Complexity analysis

**Status: PLANNED**

---

## Phase 9 — Dynamic Programming

Planned topics:

- Dynamic Programming fundamentals
- Memoization
- Tabulation
- Overlapping subproblems
- Optimal substructure
- Representative DP problems

**Status: PLANNED**

---

## Phase 10 — Interview Problems

The `problems/` directory will contain selected interview-style problems.

Each important problem should contain:

1. Problem statement
2. Approach
3. Implementation
4. Time complexity
5. Space complexity
6. Test cases

Problems will be organized by topic and difficulty.

**Status: PLANNED**

---

## DSA Playground

The `playground/` directory is planned as an optional interactive CLI for experimenting with implemented data structures and algorithms.

Possible interface:

```text
================================
        PYTHON DSA LAB
================================

1. Arrays
2. Strings
3. Linked Lists
4. Searching
5. Sorting
6. Stack
7. Queue
8. Hash Tables
9. Trees
10. Graphs
11. Exit

================================
```

The playground will expand as useful topics are implemented.

**Status: PLANNED**

---

## Documentation

The `docs/` directory is planned for useful reference material such as:

- Time complexity
- Space complexity
- Data structure comparisons
- Algorithm explanations
- Interview notes
- Practical examples
- Performance notes

**Status: PLANNED**

---

# Complexity Analysis

Important implementations will include time and space complexity.

For example:

### Binary Search

```text
Time Complexity: O(log n)
Space Complexity: O(1)
```

Complexity analysis connects the implementation with the reasoning behind algorithm selection.

---

# What This Repository Demonstrates

The completed repository is intended to demonstrate:

- Python programming
- Data structure fundamentals
- Algorithm implementation
- Problem-solving ability
- OOP concepts
- Python type hints
- Error and edge-case handling
- Automated testing with pytest
- Time and space complexity awareness
- Clean project organization
- Git and GitHub workflow

---

# Current Progress

## Completed

```text
Arrays              ✅
Strings             ✅
Linked Lists        ✅
Stacks              ✅
Queues              ✅
Hash Tables         ✅
Searching           ✅
Sorting             ✅
```

## Planned

```text
Recursion           🔜
Trees               🔜
Heaps               🔜
Graphs              🔜
Greedy Algorithms   🔜
Dynamic Programming 🔜
Interview Problems  🔜
Playground          🔜
Documentation       🔜
```

## Test Status

```text
87 / 87 tests passing
```

---

# Development Philosophy

This repository focuses on **understanding rather than simply collecting code**.

Every implementation should be:

- Understandable
- Testable
- Explainable
- Properly documented
- Reasonably efficient

New topics should be added only when they provide meaningful learning or interview value.

---

# Future Improvements

As the repository grows, possible improvements include:

- More DSA implementations
- More interview problems
- More automated tests
- Complexity documentation
- Practical examples
- Performance comparisons
- Algorithm demonstrations
- Interactive CLI experiments
- Better documentation

These improvements will be added progressively rather than simply increasing the number of files.

---

# Final Goal

The final `python-dsa` repository should be a clean and organized demonstration of Python Data Structures and Algorithms.

It should allow someone visiting the repository to understand:

1. What data structures and algorithms have been implemented
2. How they work
3. How they are tested
4. Their time and space complexity
5. How the project is organized
6. What topics are planned for future development

The repository is **not intended to be a single application**.

It is a practical **Python DSA learning, practice, and interview-preparation laboratory**.

---

# Author

**Mohit Kumar**

GitHub: https://github.com/immohitk