import random

# opciones = ["a", "b", "c", "d"]

# # Un elemento de una secuencia
# random.choice(opciones)

# # Un entero en [a, b] (ambos incluidos)
# random.randint(1, 10)

# # Un entero de range(...), como en slicing
# random.randrange(0, 10)        # 0..9

# # Un float uniforme en [a, b]
# random.uniform(0.0, 1.0)

# # k elementos SIN repetición
# print(random.sample(opciones, k=2))

# # k elementos CON repetición
# random.choices(opciones, k=5)

p=0.5

for i in range(10):
    print(random.random() < p)
