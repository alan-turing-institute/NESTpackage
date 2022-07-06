import networkx as nx
import numpy as np
from scipy import sparse
from numpy import linalg
from nest.graphstatistics.base import baseStatClass
from nest.graphstatistics.base import baseWithHistPlot
import numpy as np
name = 'Spectral Approaches'

class Adj_Top_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G)
        B = A
        self.data = sparse.linalg.eigsh(B,10,return_eigenvectors=False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))


class SymAdj_Top_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G)
        B = (A + A.T)/2
        self.data = sparse.linalg.eigsh(B,10,return_eigenvectors=False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class Adj_Top_Svd(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G,dtype=np.float)
        self.data = sparse.linalg.svds(A,10,return_singular_vectors = False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))


class Lap_Smallest_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D - A
        self.data = sparse.linalg.eigsh(L, 10, return_eigenvectors=False,sigma=0)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class RwLap_Smallest_Spectra(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = 1/A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D@A
        self.data = sparse.linalg.eigs(L, 10, return_eigenvectors=False, which='LR')
        self.histData = self.data.real
        self.data = dict(enumerate(sorted(self.data)))


class SymAdj_Top_Spectra_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G,weight=None)
        B = (A + A.T)/2
        self.data = sparse.linalg.eigsh(B,10,return_eigenvectors=False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class Adj_Top_Svd_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A = nx.to_scipy_sparse_matrix(G,dtype=np.float,weight=None)
        self.data = sparse.linalg.svds(A,10,return_singular_vectors = False)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))


class Lap_Smallest_Spectra_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G,weight=None)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D - A
        self.data = sparse.linalg.eigsh(L, 10, return_eigenvectors=False,sigma=0)
        self.histData = self.data
        self.data = dict(enumerate(sorted(self.data)))

class RwLap_Smallest_Spectra_NoWeight(baseWithHistPlot):
    def __init__(self,G1, optionsDict):
        G = G1.subgraph(max(nx.weakly_connected_components(G1), key=len))
        A0 = nx.to_scipy_sparse_matrix(G,weight=None)
        A = (A0 + A0.T)/2
        # adapted from networkx code
        n, m = A.shape
        diags = 1/A.sum(axis=1)
        D = sparse.spdiags(diags.flatten(), [0], m, n, format="csr")
        L = D@A
        self.data = sparse.linalg.eigs(L, 10, return_eigenvectors=False, which='LR')
        self.histData = self.data.real
        self.data = dict(enumerate(sorted(self.data)))
