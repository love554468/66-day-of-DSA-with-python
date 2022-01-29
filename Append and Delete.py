# https://www.hackerrank.com/challenges/append-and-delete/problem
def appendAndDelete(s,t,k):
    count = 0
    # đếm đoạn tới index giống nhau cuối cùng -> count
    for i, j in zip(s, t):
        if i == j:
            count +=1
        else:
            break

    t_len = len(s) + len(t) # tổng len s và t

    if t_len <=2*count +k and t_len%2 == k%2 or t_len <k:
        return "Yes"
    else:
        return "No"