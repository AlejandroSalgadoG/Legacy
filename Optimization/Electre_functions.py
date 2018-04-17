import sys

def get_0_matrix(height, width):
    return [ [ 0 for j in range(width) ] for i in range(height) ]

def print_matrix(title, A):
    height = len(A)
    width = len(A[0])

    print(title)
    for i in range(height):
        for j in range(width):
            sys.stdout.write( " %.2f " % A[i][j])
        print( "" )

def get_transpose(A):
    alt_num = len(A)
    criteria_num = len(A[0])

    transpose = []

    for j in range(criteria_num):
        column = [ A[i][j] for i in range(alt_num) ]
        transpose.append(column)
    return transpose

def calculate_concordance(i,j, A, w, min_max):
    criteria_num = len(A[0])
    concordance = 0

    for k in range(criteria_num):
        if A[i][k] == A[j][k]:
            concordance += w[k]/2

        if min_max[k] == "max" and A[i][k] > A[j][k]:
            concordance += w[k]

        if min_max[k] == "min" and A[i][k] < A[j][k]:
                concordance += w[k]

    return concordance

def get_concordance(A, w, min_max):
    alt_num = len(A)
    concordance = get_0_matrix(alt_num, alt_num)

    for i in range(alt_num):
        for j in range(alt_num):
            if i == j:
                continue
            concordance[i][j] = calculate_concordance(i,j, A, w, min_max)
    return concordance

def normalize(A):
    alt_num = len(A)
    criteria_num = len(A[0])

    N = get_0_matrix(alt_num, criteria_num)

    A_transpose = get_transpose(A)

    min_vals = []
    max_vals = []

    for j in range(criteria_num):
         min_vals.append( min(A_transpose[j]) )
         max_vals.append( max(A_transpose[j]) )

    for i in range(alt_num):
        for j in range(criteria_num):
            N[i][j] = (A[i][j] - min_vals[j]) / (max_vals[j] - min_vals[j])

    return N

def ponderate(N, w):
    alt_num = len(N)
    criteria_num = len(N[0])

    N_pond = get_0_matrix(alt_num, criteria_num)

    for i in range(alt_num):
        for j in range(criteria_num):
            N_pond[i][j] = N[i][j] * w[j]

    return N_pond

def calculate_discordance(i,j, N, min_max):
    alt_num = len(N)
    criteria_num = len(N[0])

    numerator = 0
    denominator = 0
        
    for k in range(criteria_num):
        val_i = N[i][k]
        val_j = N[j][k]

        check_1 = min_max[k] == "max" and val_i < val_j
        check_2 = min_max[k] == "min" and val_i > val_j

        if check_1 or check_2:
            diff_num = abs(val_j - val_i)
            if diff_num > numerator:
                numerator = diff_num
        
        diff_denom = abs(val_j - val_i)
        if diff_denom > denominator:
            denominator = diff_denom

    return numerator / denominator

def get_discordance(N, min_max):
    alt_num = len(N)
    discordance = get_0_matrix(alt_num, alt_num)

    for i in range(alt_num):
        for j in range(alt_num):
            if i == j:
                continue
            discordance[i][j] = calculate_discordance(i,j, N, min_max)
    return discordance

def get_mean(A):
    return 0
