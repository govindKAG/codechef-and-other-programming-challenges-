def revinr(s, start, end):
    return (s[:start] + (s[start:end + 1][::-1] + s[end + 1:]), end)


def optimalsub(s):
    firstb = s.find("b")
    bestsofar = s
    bestend = firstb
    for i in range(firstb + 1, len(s)):
        rev, end = revinr(s, firstb, i)
        if rev < bestsofar:
            bestsofar, bestend = rev, end
        elif rev == bestsofar:
            if end < bestend:
                bestend = end

    return (firstb, bestend,)# bestsofar)
