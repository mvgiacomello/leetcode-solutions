from typing import List

from meeting_rooms_ii.interval import Interval


def min_meeting_rooms(intervals: List[Interval]) -> int:
    """
    https://leetcode.com/problems/meeting-rooms-ii/
    :param intervals: array of meeting time intervals consisting of start and end times
    :return: minimum number of conference rooms required
    """
    if len(intervals) <= 1:
        return len(intervals)

    intervals.sort(key=lambda x: x.end, reverse=True)
    highest = intervals[0].end

    # Populate each entry of time with a value
    time_table = [0] * highest
    for entry in intervals:
        for value in range(entry.start, entry.end):
            time_table[value] += 1

    time_table.sort(reverse=True)
    return time_table[0]
