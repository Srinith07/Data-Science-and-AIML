import random
trials = 10000
count = 0

for _ in range(trials):
    coin = random.choice(['H', 'T'])
    die = random.randint(1, 6)
    if coin == 'H' and die == 6:
        count += 1

print("Independent Events Simulation")
print("Trials:", trials)
print("Experimental Probability:", count / trials)
print("Theoretical Probability: ", 1/12)
