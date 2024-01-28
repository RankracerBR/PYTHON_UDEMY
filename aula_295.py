import time
import random

#random.seed(0)

r_range = random.randrange(1,20,2)
print(r_range)

r_uniform = random.uniform(10,20)
print(r_uniform)

nomes = ['Luiz','Maria','Helena','Joana']
random.shuffle(nomes)
print(nomes)

novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

print(random.choice(novos_nomes))

random.seed(time.time())
print(time.time())