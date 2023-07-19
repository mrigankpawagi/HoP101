import random
import math # for making the plot log-scaled (we also add 1 to values as we cannot put 0 inside log)

N = 5000 # number of people
N_i = 5 # number of initial infected people

# 0 -> susceptible
# 1 -> infected
# 2 -> recovered

# T = 0

state = [0] * N
initial_infected = random.sample(range(0, N), N_i)
for i in initial_infected:
    state[i] = 1

# If you are susceptible, and have a infected neighbour, you have a 50% chance of being infected
k = 0.3 # chance of infection

# If you are recovered, you have a ___ % of recovery given that it takes 10 days to recover on average
d = 5 # days to recover
r = 1/d # chance of recovery

# Let's say that the average person makes contact with c people a day
c = 10 # number of contacts

print(N - N_i, N_i, 0, sep=", ")

T = 1 # Time instance

while T < 60:
    if T == 5:
        # 10 days after the first infection, we have a lockdown
        c = 2

    new_state = state.copy()

    i = 0
    while i < len(state):
        if state[i] == 0:
            # pick people from the population that interact with this person
            # and count how of them are infected
            num_contacts = c + random.randint(-c, c)
            infected = 0
            for j in random.sample(range(0, N), num_contacts):
                if state[j] == 1:
                    infected += 1
            prob = 1 - (1 - k) ** infected # probability of being infected
            if random.random() < prob:
                new_state[i] = 1
                
        if state[i] == 1:
            if random.random() < r:
                new_state[i] = 2

        i = i + 1

    state = new_state.copy()

    i = 0
    nums = [0, 0, 0]
    while i < len(state):
        nums[state[i]] += 1
        i += 1

    print(*nums, sep=", ")

    T = T + 1

# Run in the command prompt/terminal:
# python main.py > data.csv
# and open data.csv in Excel to plot the data and observe the curve!
