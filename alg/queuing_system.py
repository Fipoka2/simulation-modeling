import random

N = 100


def work(waiting_cost, dwntime_cost, N, a, b, c, d):
    i = 0
    time_z = [0]*N
    service_time = [0]*N
    time_waiting = [0]*N
    time_dwntime = [0]*N
    mean_time_waiting = mean_time_dwntime = mean_loss = 0
    time_z[i] = random.randrange(a, b, 1)
    service_time[i] = random.randrange(c, d, 1)
    if time_z[i] >= service_time[i]:
        time_waiting[i] = 0
        time_dwntime[i] = time_z[i] - service_time[i]
    else:
        time_dwntime[i] = 0
        time_waiting[i] = service_time[i] - time_z[i]
    for k in range(i):
        mean_time_dwntime += time_dwntime[i]
    for k in range(i):
        mean_time_waiting += time_waiting[i]
    mean_dwntime = dwntime_cost * mean_time_dwntime
    mean_waiting = waiting_cost * mean_time_waiting
    mean_loss = mean_waiting + mean_dwntime

    while i < N-1:
        i = i + 1
        if i < N:
            time_z[i] = random.randrange(a, b, 1)
            time_z[i] = time_z[i] - time_waiting[i-1]
            service_time[i] = random.randrange(c, d, 1)
            if int(time_z[i]) >= int(service_time[i]):
                time_waiting[i] = 0
                time_dwntime[i] = time_z[i] - service_time[i]
            else:
                time_dwntime[i] = 0
                time_waiting[i] = service_time[i] - time_z[i]
            for k in range(i):
                mean_time_dwntime += time_dwntime[i]
            for k in range(i):
                mean_time_waiting += time_waiting[i]
            mean_dwntime = dwntime_cost * mean_time_dwntime/i
            mean_waiting = waiting_cost * mean_time_waiting/i
            mean_loss = mean_waiting + mean_dwntime
    return mean_loss

'''
print("Введите стоимость ожидания в единицу времени", end='\n')
waiting_cost = input()
print("Введите стоимость простоя в единицу времени", end='\n')
dwntime_cost = input()
print("Введите интервал для значений Тз", end='\n')
a = input()
b = input()
print("Введите интервал для значений времени обслуживания", end='\n')
c = input()
d = input()
'''

#work(int(waiting_cost), int(dwntime_cost), 100, int(a), int(b), int(c), int(d))
# print("Средние потери:", work(3, 2, 100, 10, 25, 2, 20))
