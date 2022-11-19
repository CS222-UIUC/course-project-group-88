
from typing import List
import re

def fits(times: List[List[int]], add: str) -> bool:
    """
    Checks to see if added time fits into schedule
    times (ListList[[str]]) - List of times in current schedule
    add (str) - time to be added
    Returns (bool) - indication whether or not time was successfully added
    """
    add_me = time_val(add)
    if len(times) == 0:
        times.append(add_me)
        return True
    elif add_me[1] < times[0][0] :
        times.insert(0, add_me)
        return True
    elif add_me[0] > times[-1][1]:
        times.append(add_me)
        return True
    else:
        idx = 0
        lower_bound = False
        for pair in times:
            if add_me[1] < pair[0] and lower_bound:
                times.append(idx, add_me)
                return True
            if pair[1] < add_me[0]:
                lower_bound = True
            else :
                lower_bound = False
    return False

def time_val(time: str) -> List[int] :
    """
    Returns int representation of a time
    time (str) - time to be analyzed
    Returns (List[int]) - A list of two elements, first indicating start time and second indicating end time
    """
    time_ints = []
    interval = time.split('-')
    bounds = [element.replace(' ', '') for element in interval]
    start = re.findall(r'\d+', bounds[0])
    additive = 0 if (start[0] == 12 or "Am" in bounds[0]) else 12 * 60
    time_ints.append(start[0] * 60 + additive + start[1])
    end = re.findall(r'\d+', bounds[1])
    additive = 0 if (end[0] == 12 or "AM" in bounds[1]) else 12 * 60
    time_ints.append(end[0] * 60 + additive + end[1])
    return time_ints
