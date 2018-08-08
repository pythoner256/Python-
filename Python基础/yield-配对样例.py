a_list = [i for i in range(1, 101)]


def procesor():
    yield 10
    yield 20
    yield 30
    yield 40


n_list = [(n, j) for n in a_list for j in procesor()]
print(n_list)

