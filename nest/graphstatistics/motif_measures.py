import networkx as nx
import importlib
from nest.graphstatistics.base import baseStatClass
name = 'Motif Measures'


def __statistic_helper__(func, A):
    res = {}
    f1 = func(A, 'struc', 'unweighted', 'sparse').sum(axis=0)
    res['unweighted_mean'] = f1.mean()
    res['unweighted_min'] = f1.min()
    res['unweighted_max'] = f1.max()
    f1 = func(A, 'struc', 'product', 'sparse').sum(axis=0)
    res['product_mean'] = f1.mean()
    res['product_min'] = f1.min()
    res['product_max'] = f1.max()
    f1 = func(A, 'struc', 'mean', 'sparse').sum(axis=0)
    res['mean_mean'] = f1.mean()
    res['mean_min'] = f1.min()
    res['mean_max'] = f1.max()
    return res

if importlib.util.find_spec('motifcluster'):
    from motifcluster import motifadjacency as ma

    class Triadic_census(baseStatClass):
        def __init__(self, G, optionsDict):
            triadicCensus = nx.triadic_census(G)
            self.data = triadicCensus


    class Motif_Stats_M1(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M1
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M2(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M2
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M3(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M3
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M4(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M4
            res = {}
            f1 = func(A, 'unweighted', 'sparse').sum(axis=0)
            res['unweighted_mean'] = f1.mean()
            res['unweighted_min'] = f1.min()
            res['unweighted_max'] = f1.max()
            f1 = func(A, 'product', 'sparse').sum(axis=0)
            res['product_mean'] = f1.mean()
            res['product_min'] = f1.min()
            res['product_max'] = f1.max()
            f1 = func(A, 'mean', 'sparse').sum(axis=0)
            res['mean_mean'] = f1.mean()
            res['mean_min'] = f1.min()
            res['mean_max'] = f1.max()
            self.data = res


    class Motif_Stats_M6(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M6
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M7(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M7
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M8(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M8
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M9(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M9
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M10(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M10
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M11(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M11
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M12(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M12
            self.data = __statistic_helper__(func, A)


    class Motif_Stats_M13(baseStatClass):
        def __init__(self, G, optionsDict):
            A = nx.to_scipy_sparse_matrix(G)
            func = ma.mam_M13
            self.data = __statistic_helper__(func, A)
