#!/usr/bin/env python3

def get_intervals():
    intervals = []
    new_interval = []
    n = int(input())
    for i in range(n+1):
        pair = input()
        pair = [int(x) for x in pair.split(" ")]
        if i < n: intervals += [pair]
        else: new_interval += pair
    return [intervals, new_interval]

def insert(intervals, new_interval):
    if len(intervals) == 0: return [new_interval]

    result = []
    result.append(intervals[0])
    top = result[-1]

    if new_interval[1] < top[0]:
        top = result.pop()
        result.append(new_interval)
        result.append(top)
    elif new_interval[0] <= top[1]:
        result.pop()
        top = [min(top[0], new_interval[0]),
               max(top[1], new_interval[1])]
        result.append(top)
    else:
        result.append(new_interval)

    top = result[-1]
    for i in range(1, len(intervals)):
        if intervals[i][1] < top[0]:
            top = result.pop()
            result.append(intervals[i])
            result.append(top)
        elif intervals[i][0] <= top[1]:
            result.pop()
            top = [min(top[0], intervals[i][0]),
                   max(top[1], intervals[i][1])]
            result.append(top)
        else:
            result.append(intervals[i])
        top = result[-1]

    return result

def main():
    intervals = insert(*get_intervals())
    print(intervals)

if __name__ == "__main__":
    main()
