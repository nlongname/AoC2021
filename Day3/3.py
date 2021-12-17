from functools import reduce

data = []

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

#data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

gamma = [sum([int(d[i]) for d in data])*2//len(data) for i in range(len(data[0]))]
epsilon = [int(not d) for d in gamma]
gamma = reduce(lambda x,y: str(x)+str(y), gamma)
epsilon = reduce(lambda x,y: str(x)+str(y), epsilon)
gamma_dec = int(gamma,2)
epsilon_dec = int(epsilon, 2)
print(f"power consumption is {gamma_dec*epsilon_dec}")

#oxygen
oxy_data = [d for d in data]
for i in range(len(data[0])):
    if len(oxy_data) == 1:
        break
    check_digit = str(sum([int(d[i]) for d in oxy_data])*2//len(oxy_data)) #tie-break happens automatically
    oxy_data = [d for d in oxy_data if d[i] == check_digit]
oxy_rating = int(oxy_data[0],2)
#print(f"Oxygen: {oxy_rating}")

#carbon dioxide
co2_data = [d for d in data]
for i in range(len(data[0])):
    if len(co2_data) == 1:
        break
    check_digit = str(int(not sum([int(d[i]) for d in co2_data])*2//len(co2_data))) #and is reversed here, as intended
    co2_data = [d for d in co2_data if d[i] == check_digit]
co2_rating = int(co2_data[0],2)
#print(f"CO2: {co2_rating}")
print(f"Life support rating: {oxy_rating*co2_rating}")
