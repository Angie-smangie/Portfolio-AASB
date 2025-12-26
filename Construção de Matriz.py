def matriz_de_zeros(seq1,seq2):
    matriz_a_zeros=[[0 for n2 in range(len(seq2)+1)] for n1 in range(len(seq1)+1)]
    return matriz_a_zeros

def primeira_linha_e_coluna(matriz,seq1,seq2,space):
    for p1 in range(len(seq1)):
        matriz[0][p1+1]=matriz[0][p1]+space
    for p2 in range(len(seq2)):
        matriz[p2+1][0]=matriz[p2][0]+space
    return matriz

def needleman_wunsch(seq1,seq2,match=2,mismatch=-2,space=-5):
    matriz=matriz_de_zeros(seq1,seq2)
    primeira_linha_e_coluna(matriz,seq1,seq2,space)
    return primeira_linha_e_coluna

needleman_wunsch("SKJD","SDKDJSOIDF")
