
def breakdown(points):
    print(points)
    if points <= 0:
        return 0
    elif points == 1:
        return 1
    elif points == 2:
        return 2
    elif points == 3:
        return 4

    # DP Array Creation
    """N[i] = # of ways to sum up to i points (with basketball scoring)

    In basketball, you can score three ways:
    1) With free throws (1pt)
    2) With Shots inside the arc (2pts)
    3) With shot outside the arc (3pts)
    """
    N = [0 for i in range(points + 1)]

    # DP Base Cases (Same as above)
    N[0] = 0  # didn't score any points -> no way to sum up to 0 with 1, 2, or 3
    N[1] = 1  # scored only one point, only one way: with one free throw
    N[2] = 2  # two free throws or one 2-pointer
    N[3] = 4  # one three pointer or three free throws or a free throw and a two pointer (two ways)

    # DP Step
    """Recurrence relation below

    Number of ways to get points, pt =
    -> Number of ways to get points, pt-1, + 1 free throw
    -> Number of ways to get points, pt-2, + 1 two pointer
    -> Number of ways to get points, pt-3, + 1 three pointer
    """
    for pt in range(4, points + 1):
        N[pt] = N[pt - 1] + N[pt - 2] + N[pt - 3]

    return N[points]


if __name__ == '__main__':
    pts = 33
    print("Steph Curry Scored %d points. There are %d possible ways he could have done that" % (pts, breakdown(pts)))
