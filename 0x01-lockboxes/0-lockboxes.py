#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
    """


def canUnlockAll(boxes):
    """checks"""
    if (not isinstance(boxes, list)):
        return False

    seen = [False for _ in range(len(boxes))]
    seen[0] = True
    useBFS(boxes, seen)
    return all(seen)


def useBFS(boxes, seen):
    """uses iteration to visit nodes breadth-first

    """
    for i, box in enumerate(boxes):
        if (isinstance(box, list) is not True):
            continue

        for key in box:
            if (isinstance(key, int) is not True):
                continue

            # guard against
            if (key >= len(boxes)):
                continue

            if (i == key):
                continue

            seen[key] = True


def useDFS(boxes, seen, currentBoxIdx):
    """uses recursion to visit nodes depth-first

    """
    currentBox = boxes[currentBoxIdx]

    if (isinstance(currentBox, list) is not True):
        return

    for key in currentBox:
        if (isinstance(key, int) is not True):
            continue

        # guard against out-of-bounds array access
        if (key >= len(boxes)):
            continue

        if (seen[key]):
            continue

        seen[key] = True
        useDFS(boxes, seen, key)
