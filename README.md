# Algorithm to find number of intersections in a circle
## Atharva Kulkarni (atharva.kulkarni@columbia.edu)


## Overview

This README.md file provides a brief summary of the suggested approach/ solution for the Take Home Question. Here I am implementing an algorithm for efficiently finding and counting the number of intersections give a list of chords in a circle.  My preferred language is Python, FYI.

I have also stated the relavent assumptions and analyzed the runtime of the proposed algorithm as per the instructions.

### Assumptions
1. All starting "s_x" and ending point "e_x" are unique i.e. no overlap of start and end points
 
	 Eg: The case `[(0.5, 0.5, 1, 1.5), ("s_1", "s_2", "e_2", "e_1")]` will not be considered for our question.
2. Considering the format of identifiers as "s_x" and "e_x" as mentioned in the Input section of the question for consistency and simplicity.

## Working of the proposed algorithm

The code aims to count the number of intersections between chords on a circle, given their start and end points. For better usage, I have created a class named `CircleChordIntersections` to encapsulate the alogirthm.

Here's the logic/ steps taken to count the number of intersections between chords in a circle :

1. **Initialization:**
   - The constructor `__init__` is used to intializze the following items given below:
      -  Initalizing an empty dictionary  `chords`  and also  `sorted_chords ` which will be used as explained in the below mentioned steps.
      -  Initalizing an empty list `active_chords` to store the current active chords used to check the intersections.
      - Initalizing a counter `intersections` to store the the count of number of intersections as desired in the question..

2. **Chord pairing:**
   - Chords are paired by creating a dictionary (`chords`) where each start point is associated with its corresponding end point.

3. **Sorting:**
   - The paired chords are sorted based on their start points in ascending order to facilitate efficient processing.

4. **Iterating through chords:**
   - The algorithm iterates through the sorted chords, maintaining a list of active chords (`active_chords`).
   - Inactive chords, whose end points have already been reached, are removed from the active list.

5. **Intersection counting:**
   - At each iteration, the number of intersections is updated by the count of active chords.
   - All active chords intersect with the current chord.

6. **Maintaining order of active chords:**
   - The end point of the current chord is inserted into the `active_chords` list while preserving its sorted order.
   - This ensures that the active chords list remains sorted for efficient processing.

7. **Returning the result:**
   - The `count_intersections` method returns the total count of intersections calculated during the iterations.

Basically, the `CircleChordIntersections` class is used to create an instance for each test case, and the `count_intersections` method is called to get the number of intersections. Lastly, the above mentioned steps help us efficiently find and counts chord intersections by maintaining a sorted list of active chord end points as it iterates through the sorted chords based on their start points.

## Runtime analysis

The time taken to implement the algorithm is mainly from using a sorted list (`sorted_chords`) and the `active_chords` list. The initalization of the `chords` dictionary has a time complexity of *O(n)*. 

Here n = number of total chords. 

Sorting the chords based on start points takes *O(n log n)* time. After that the iteration through the sorted chords has a time complexity of *O(n)*, where each iteration deals with the `active_chords` list, which is maintained in sorted order using binary insertion (`bisect.insort`) - Using `bisect` to maintain the sorted order of the active chords reduced the time taken for insertion and deletion operations

The overall time complexity is dominated by the sorting step, resulting in *O(n log n*) time complexity.Therefore, the algorithm efficiently counts chord intersections with a time complexity that scales well with the number of chords.

### Checking the accuracy of the algorithm

In order to assess the accuracy of the the algorithm. I run the algorithm on the examples given in the instruction doc and the expected output and actual output match succesfully.
Additionally, I created 4 test cases based on the assumptions, and all of the test cases passed successfully. Found out the expected output by manual calculation.

## Usage

The class `CircleChordIntersections` can be called to run the method and get the desired count of number of intersections. I have attached both `.py` and `.ipynb` file for your reference.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/atharva-011/takehome-question.git

2. **Project directory:**

   ```bash
   cd takehome-question

3. **Running the file:**

	```bash
   python Atharva Kulkarni_Take-Home Question.py

