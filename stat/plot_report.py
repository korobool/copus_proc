from pprint import pprint


def plot_rep(items):
    pprint(items)

    from matplotlib import pyplot as plt

    items = items[:300]

    data0 = map(lambda i: i[0], items)
    data1 = map(lambda i: i[1], items)
    data2 = map(lambda i: i[2], items)
    data3 = map(lambda i: i[3], items)

    items_labels = list(range(len(items)))

    plt.plot(items_labels, list(data0))
    plt.plot(items_labels, list(data1))
    plt.plot(items_labels, list(data2))
    plt.plot(items_labels, list(data3))

    plt.show()
