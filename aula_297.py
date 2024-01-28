from secrets import SystemRandom as Sr
import random
import string as s
import time

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))

#random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10,11,12]))

r_range = random.randrange(1,20,2)
print(r_range)
s
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

