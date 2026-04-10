def max_depth(lst):
    if not isinstance(lst, list) or not lst:
        return 0
    return 1 + max((max_depth(item) for item in lst), default=0)
"Task2"
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result