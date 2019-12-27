import random

N = 100

def work(C1, C2, C3, Nmin, Q, Q0, T):
    t = j = k =0
    N = Nmin
    demand = [0]*T-1
    for f in range(T):
        demand[f] = random.randrange(5, 10, 1)
    lead_time = [0]*100
    cost = deficit = storage_cost = delivery = 0
    N = N + Q0
    while t <= T:
        if t == k:
            N = N + Q
        N = N - demand[t]
        if N < 0:
            deficit = deficit - C2*N
            N = 0
        storage_cost = storage_cost + C1*N
        if N <= Nmin:
            if t >= k:
                #дозаказ
                delivery = delivery + C3*Q
                j = j+1
                lead_time[j] = random.randrange(5, 10, 1)
                k = t + lead_time[j]
        t = t+1
    cost = deficit + storage_cost + delivery
    return (cost)