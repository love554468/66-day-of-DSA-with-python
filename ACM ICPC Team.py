https://www.hackerrank.com/challenges/acm-icpc-team/problem
def acmTeam(topic):
    maxsub = 0
    count = 0

    for i in range(n):
        for j in range(i, n):
            sub = 0
            for x, y in zip(topic[i], topic[j]):
                if x=='1' or y=='1':
                    sub +=1

            if sub>maxsub:
                maxsub = sub
                count = 1
            elif sub == maxsub:
                count +=1

    return [maxsub, count]
    