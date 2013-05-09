def backwards(goal, denom, value, count, current, prog):
    if value == 200:
        count += 1
        prog += 1
    elif value < 200:
        value = value + denom[current]
    else:
        current += 1
        value = 0
        if current > len(denom):
            return count
    #denom = denom[prog:]
    backwards(goal, denom, value, count, current, prog)

goal = 200
denom_off = [1, 2, 5, 10, 20, 50, 100, 200]
denom = [200, 100, 50, 20, 10, 5, 2, 1]
value = 0
count = 0
current = 0
prog = 0


print backwards(goal, denom, value, count, current, prog)
