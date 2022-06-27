def get_divisors(n: int, h: int, window: int):
    pre_pad = [0.0] * h
    post_pad = [0.0] * h
    weights = pre_pad + [1.0] * n + post_pad

    n = len(weights)
    s = sum(weights[:window])
    divisors = [s]

    for ind in range(n - window):
        s = s - weights[ind] + weights[ind + window]
        divisors.append(s)

    return divisors


def get_sums(inlist: [float], h: int, window: int):
    pre_pad = [0] * h
    post_pad = [0] * h
    inlist = pre_pad + inlist + post_pad

    n = len(inlist)
    s = sum(inlist[:window])
    sums = [s]

    for ind in range(n - window):
        s = s - inlist[ind] + inlist[ind + window]
        sums.append(s)

    return sums


def smooth(inlist: [float], h: int):
    """
    This function performs a basic smoothing
    of inlist and returns the result (outlist).
    Both lists have the same length, N. Each
    item in inlist should have type 'float' and
    'h' should be an integer. For each i,
    outlist[i] will be the average of inlist[k]
    over all k that satisfy i-h <= k <= i+h
    and 0 <= k <= N-1.

    INPUT:
    inlist: Array of floats
    h: Integer

    OUTOUT:
    outlist: Array of floats (smoothened array)
    """

    window = (2 * h) + 1
    divisors = get_divisors(len(inlist), h, window)
    sums = get_sums(inlist, h, window)
    outlist = [s / d for s, d in zip(sums, divisors)]

    return outlist


##inlist = [float(1) for i in range(1,15)]
print("Input space-separated inlist elements:")
inlist = list(map(float, input().split()))
print("inlist:", inlist)
print("Input h:")
h = int(input())
print("outlist:", smooth(inlist, h))
