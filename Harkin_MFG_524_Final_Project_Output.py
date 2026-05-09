Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
= RESTART: C:\Users\Lana\Desktop\MFG 524 Assignments\Harkin MFG 524 Final Project\Harkin_MFG_524_Final _Project_ Emergency_Response_System.py
=======================================================
MFG 524 Given Test Case:
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

=======================================================
TEST CASE (a): Base Functionality
=======================================================
Ambulance Coordinate Table:
  Ambulance    Location (x, y)
  ------------ ---------------
  A            (3, 7)
  B            (8, 2)
  C            (5, 5)
Accident Location: X = (5, 3)
Nearest Ambulance: {'C': (5, 5)}

=======================================================
TEST CASE (b): Tie Resolution (Lexicographic)
=======================================================
Ambulance Coordinate Table:
  Ambulance    Location (x, y)
  ------------ ---------------
  A            (3, 3)
  B            (8, 5)
  C            (6, 3)
  D            (6, 3)
  E            (5, 5)
Accident Location: X = (5, 3)
Nearest Ambulance: {'C': (6, 3)}

=======================================================
TEST CASE (c): Single Ambulance
=======================================================
Ambulance Coordinate Table:
  Ambulance    Location (x, y)
  ------------ ---------------
  A            (5, 5)
Accident Location: X = (1, 1)
Nearest Ambulance: {'A': (5, 5)}

=======================================================
TEST CASE (d): Negative and Large Coordinates
=======================================================
Ambulance Coordinate Table:
  Ambulance    Location (x, y)
  ------------ ---------------
  A            (-100, -50)
  B            (1000000.0, 1000000.0)
  C            (500, 400)
  D            (-200, -300)
  E            (250, 250)
Accident Location: X = (0, 0)
Nearest Ambulance: {'A': (-100, -50)}

