# Real-Time Emergency Response System
**MFG 524 – Final Semester Project | Lana Harkin**

## Overview
This project implements a **divide-and-conquer** algorithm to find the nearest ambulance to an accident location on a 2D coordinate plane. In emergencies, every second counts — this system rapidly identifies which ambulance to dispatch by minimizing travel distance.

## Problem Statement
Given a dictionary of ambulance positions `{'A': (x, y), ...}` and an accident location `(x, y)`, the system returns the ambulance with the minimum Euclidean distance to the accident.

## Algorithm
The `EmergencyResponseSystem` class:
1. Converts the ambulance dictionary to a list of `(key, (x,y))` tuples
2. **Sorts** by x-coordinate (Hint #1 from project spec)
3. Applies **recursive divide-and-conquer** (binary-search style) to find the nearest candidate in each half
4. **Combines** by comparing distances; ties broken by lexicographically smallest key

### Time Complexity
- Sorting: O(n log n)
- Divide-and-conquer search: O(n log n) total recursive calls

## Files
| File | Description |
|------|-------------|
| `Harkin_MFG_524_Final__Project__Emergency_Response_System.py` | Main implementation |
| `README.md` | Project documentation |

## How to Run
```bash
python Harkin_MFG_524_Final__Project__Emergency_Response_System.py
```

## Test Cases
| Case | Description |
|------|-------------|
| Original Problem | 5 ambulances, accident at (6,2) → nearest: D (7,1) |
| (a) Base Functionality | 3 ambulances, accident at (5,3) |
| (b) Tie Resolution | C and D at same location (6,3); tie → C (lexicographic) |
| (c) Single Ambulance | Only one ambulance available; must return without error |
| (d) Negative & Large Coords | Coordinates range from -300 to 1,000,000 |

## Sample Output
```
=======================================================
ORIGINAL PROBLEM
=======================================================
Ambulance Coordinate Table:
  Ambulance    Location (x, y)
  ------------ ---------------
  A            (2, 4)
  B            (10, 3)
  C            (5, 8)
  D            (7, 1)
  E            (4, 5)
Accident Location: X = (6, 2)
Nearest Ambulance: {'D': (7, 1)}
```

## Professional & Ethical Considerations
- **Life-critical accuracy**: The algorithm must return the correct nearest ambulance — an error could cost a life.
- **Tie-breaking transparency**: Consistent, documented tie-breaking behavior (lexicographic key order) ensures predictable and auditable dispatch decisions.
- **Scalability**: The divide-and-conquer approach scales better than brute-force as the number of ambulances grows in a real city-wide system.
- **Bias-free dispatch**: The algorithm is purely distance-based with no demographic or location bias.

## Class & Tools
- **Course**: MFG 524 – Spring 2026, Arizona State University
- **Language**: Python 3
- **Libraries**: `math.sqrt` (standard library only)
