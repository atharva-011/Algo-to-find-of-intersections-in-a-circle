#!/usr/bin/env python
# coding: utf-8

# #### Name: Atharva Kulkarni
# #### Email-ID: atharva.kulkarni@columbia.edu

# In[1]:


import bisect

#Defining a class
class CircleChordIntersections:
    def __init__(self, input_lists):
        self.rad_measures, self.identifiers = input_lists
        self.chords = {}
        self.sorted_chords = []
        self.active_chords = []
        self.intersections = 0

        self._initialize_chords()

        # Sort the chords by start points
        self.sorted_chords = sorted(self.chords.values(), key=lambda x: x['start'])

    def _initialize_chords(self):
        # Pair each start with its corresponding end
        for i, ident in enumerate(self.identifiers):
            if 's' in ident:
                self.chords[ident] = {'start': self.rad_measures[i]}
            else:
                self.chords['s' + ident[1:]]['end'] = self.rad_measures[i]

    def _update_active_chords(self, start):
        # Remove all active chords that have ended before the current chord's start
        self.active_chords = [c for c in self.active_chords if c > start]

    def _count_intersections_with_active_chords(self):
        # Count intersections with active chords (all of them will intersect)
        self.intersections += len(self.active_chords)

    def _insert_into_active_chords(self, end):
        # Insert current chord's end maintaining the sorted order
        bisect.insort(self.active_chords, end)

    def count_intersections(self):
        # Iterate through the sorted chords
        for chord in self.sorted_chords:
            start, end = chord['start'], chord['end']

            self._update_active_chords(start)
            self._count_intersections_with_active_chords()
            self._insert_into_active_chords(end)

        return self.intersections


# In[2]:


# Example Input as per instruction doc

input_lists_1 = [(0.78, 1.47, 1.77, 3.92), ("s_1", "s_2", "e_1", "e_2")]
circle_intersections = CircleChordIntersections(input_lists_1)
result = circle_intersections.count_intersections()
print(f"Number of Intersections (Example 1): {result}")

input_lists_2 = [(0.9, 1.3, 1.70, 2.92), ("s_1", "e_1", "s_2", "e_2")]
circle_intersections = CircleChordIntersections(input_lists_1)
result = circle_intersections.count_intersections()
print(f"Number of Intersections (Example 2): {result}")


# In[3]:


# Defining test cases
test_cases = {
    "No Intersections": { "input": [(0.5, 1.0, 2.0, 3.0), ("s_1", "e_1", "s_2", "e_2")],
        "expected": 0
    },
    "One Intersection": { "input": [(0.78, 1.47, 1.77, 3.92), ("s_1", "s_2", "e_1", "e_2")],
        "expected": 1
    },
    "Multiple Intersections": { "input": [(0.5, 2.5, 1.75, 3.0, 2.2, 3.3), ("s_1", "e_1", "s_2", "e_2", "s_3", "e_3")],
        "expected": 3
    },
       "Chords Forming a Complete Cycle": {"input": [(0.5, 1.5, 1.0, 2.0, 1.4, 2.5, 1.9, 3.0, 2.4, 3.5), 
               ("s_1", "e_1", "s_2", "e_2", "s_3", "e_3", "s_4", "e_4", "s_5", "e_5")],
        "expected": 7
    },
    "Random Chords": { "input": [(0.1, 1.2, 2.3, 3.4, 0.5, 1.6, 2.7, 3.8), 
               ("s_1", "e_1", "s_2", "e_2", "s_3", "e_3", "s_4", "e_4")],
        "expected": 2
    }
}

print(f"Number of Intersections\n")

for name, test in test_cases.items():
    circle_intersections = CircleChordIntersections(test["input"])
    actual = circle_intersections.count_intersections()
    print(f"{name} :- Expected: {test['expected']}, Actual: {actual}")

