import serveur

assert(serveur.add(1, 2) == 3)
assert(serveur.add(1, 3) == 4)
assert(serveur.add(5, 1) == 6)

assert(serveur.sub(2, 1) == 1)
assert(serveur.sub(3, 1) == 2)
assert(serveur.sub(5, 1) == 4)
assert(serveur.sub(1, 5) == -4)

assert(serveur.mul(1, 2) == 2)
assert(serveur.mul(3, 1) == 3)
assert(serveur.mul(5, 2) == 10)
assert(serveur.mul(7, -5) == -35)

assert(serveur.div(1, 0) == None)
assert(serveur.div(2, 1) == 2)
assert(serveur.div(2, 2) == 1)
