import random as r

N = 500
t = 4000

agents = [0] * N
agents[0] = 1

for i in range(t):
    a1, a2 = r.sample(range(N), 2)

    if agents[a1] or agents[a2]:
        agents[a1] = 1
        agents[a2] = 1

    print(sum(agents))