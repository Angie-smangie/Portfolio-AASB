"""
É necessário adicionar um Assert na matriz de substituição, que se identificar_sequencia=="DNA" usa o que está, e se for =="AMINO" usar BLOSUM62
É necessário fazer reconstrução
"""

def matriz_substituição(match,mismatch):
    subst={"A":{"A":match,"G":mismatch,"C":mismatch,"T":mismatch},
           "C":{"A":mismatch,"G":mismatch,"C":match,"T":mismatch},
           "G":{"A":mismatch,"G":match,"C":mismatch,"T":mismatch},
           "T":{"A":mismatch,"G":mismatch,"C":mismatch,"T":match}}
    return subst

def matriz_de_zeros(seq1,seq2):
    return [[0 for n2 in range(len(seq2)+1)] for n1 in range(len(seq1)+1)]

def primeira_linha_e_coluna(seq1,seq2,space):
    matriz=matriz_de_zeros(seq1,seq2)
    for p2 in range(len(seq2)):
        matriz[0][p2+1]=matriz[0][p2]+space
    for p1 in range(len(seq1)):
        matriz[p1+1][0]=matriz[p1][0]+space
    return matriz

def needleman_wunsch(seq1,seq2,match=2,mismatch=-3,space=-8):
    inicial=primeira_linha_e_coluna(seq1,seq2,space)
    subst=matriz_substituição(match,mismatch)
    for p1,n1 in enumerate(seq1):
        for p2,n2 in enumerate(seq2):
            inicial[p1+1][p2+1]=max(inicial[p1][p2+1]+space,
                                inicial[p1+1][p2]+space,
                                inicial[p1][p2]+subst[n1][n2])
    return inicial

def smith_waterman(seq1,seq2,match=2,mismatch=-3,space=-8):
    inicial=primeira_linha_e_coluna(seq1,seq2,space=0)
    subst=matriz_substituição(match,mismatch)
    for p1,n1 in enumerate(seq1):
        for p2,n2 in enumerate(seq2):
            inicial[p1+1][p2+1]=max(0,
                                inicial[p1][p2+1]+space,
                                inicial[p1+1][p2]+space,
                                inicial[p1][p2]+subst[n1][n2])
    return inicial
