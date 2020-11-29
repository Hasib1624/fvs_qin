import numpy as np
import _pickle

N = np.arange(10 ** 3, 10 ** 4 + 1, 10 ** 3)
mean_deg = np.arange(5, 25, 5)

graphs = []
for n in N:
    for m in mean_deg:
        dict_ = {
            "No_of_vertices": n,
            "Mean_deg": m,
        }
        l = []
        for i in range(n):
            for j in range(n):
                if np.random.uniform() < m / n:
                    l.append((i, j))
        dict_["Edges"] = np.array(l)
        graphs.append(dict_)

with open("graphs.pkl", "wb") as f:
    _pickle.dump(graphs, f)
