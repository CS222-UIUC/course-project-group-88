
from typing import List
import re

def fits(times: List[str], add: str) -> bool:
    """
    Checks to see if added time fits into schedule
    times (List[str]) - List of times in current schedule
    add (str) - time to be added
    Returns (bool) - indication whether or not time was successfully added
    """
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
