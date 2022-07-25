import networkx as nx
import numpy as np
from scipy import sparse
from numpy import linalg
from nest.graphstatistics.base import baseStatClass
from nest.graphstatistics.base import baseWithHistPlot
import networkx as nx
import numpy as np
name = 'Spectral Approaches'

class Adj_LCC_Top_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G)
        B = A
        if B.shape[0]<15:
            data = linalg.eigvalsh(B.todense())
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[-10:]
        else:
            self.data = sparse.linalg.eigsh(B,10,return_eigenvectors=False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))


class SymAdj_LCC_Top_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G)
        B = (A + A.T)/2
        if B.shape[0]<15:
            data = linalg.eigvalsh(B.todense())
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[-10:]
        else:
            self.data = sparse.linalg.eigsh(B,10,return_eigenvectors=False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class Adj_LCC_Top_Svd(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G,dtype=np.float)
        if A.shape[0]<15:
            data = linalg.svd(A.todense(),compute_uv=False)
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[-10:]
        else:
            self.data = sparse.linalg.svds(A,10,return_singular_vectors = False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))


class Lap_LCC_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D - A
        if L.shape[0]<15:
            data = linalg.eigvalsh(L.todense())
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[:10]
        else:
            # self.data = sparse.linalg.eigsh(L, 10, return_eigenvectors=False,sigma=0)
            self.data = sparse.linalg.eigsh(L, 10, return_eigenvectors=False,which="SM")
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class RwLap_LCC_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = 1/A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D@A
        if L.shape[0]<15:
            data = linalg.eigvals(L.todense())
            data = sorted(data,key=lambda x:x.real)
            self.data = data[-10:]
        else:
            self.data = sparse.linalg.eigs(L, 10, return_eigenvectors=False, which='LR')
            self.histData = self.data.real
        self.data = dict(enumerate(sorted(self.data)))


class SymAdj_LCC_Top_Spectra_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G,weight=None)
        B = (A + A.T)/2
        if B.shape[0]<15:
            data = linalg.eigvalsh(B.todense())
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[-10:]
        else:
            self.data = sparse.linalg.eigsh(B,10,return_eigenvectors=False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class Adj_LCC_Top_Svd_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G,dtype=np.float,weight=None)
        if A.shape[0]<15:
            data = linalg.svd(A.todense(),compute_uv=False)
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[-10:]
        else:
            self.data = sparse.linalg.svds(A,10,return_singular_vectors = False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))


class Lap_LCC_Spectra_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G,weight=None)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D - A
        if L.shape[0]<15:
            data = linalg.eigvalsh(L.todense())
            data = sorted(data,key=lambda x:abs(x))
            self.data = data[:10]
        else:
           # self.data = sparse.linalg.eigsh(L, 10, return_eigenvectors=False,sigma=0)
            self.data = sparse.linalg.eigsh(L, 10, return_eigenvectors=False,which="SM")
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class RwLap_LCC_Spectra_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        if isinstance(G1, nx.Graph):
            G = G1.subgraph(max(nx.connected_components(G1), key=len))
        else:
            G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G,weight=None)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = 1/A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D@A
        if L.shape[0]<15:
            data = linalg.eigvalsh(L.todense())
            data = sorted(data,key=lambda x:x.real)
            self.data = np.array(data[-10:])
        else:
            self.data = sparse.linalg.eigs(L, 10, return_eigenvectors=False, which='LR')
        self.histData = self.data.real
        self.data = dict(enumerate(sorted(self.data)))
