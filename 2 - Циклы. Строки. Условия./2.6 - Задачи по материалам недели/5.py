n_input = str(input())

n = int(n_input)

int_list = []
empty_matrix = [[0] * n for i in range(n)]
m_str = len(empty_matrix)
m_con = len(empty_matrix[0])


for z in range(n ** 2):
    int_list.append(z + 1)

c = len(int_list)
cc = 0

for ii in range(n):
    for jj in range(n):

        # 5 символов:
        if ii == 0:
            empty_matrix[ii][jj] = int_list[jj]
            #print('1')
            #print()

        # 4 символа:
        elif ii != 0 and jj == m_con - 1:
            empty_matrix[ii][jj] = int_list[n + ii - 1]
            #print("2. ii = %s " % ii)

        # 4 символа:
        elif ii == m_str - 1 and jj < m_con - 1:
            empty_matrix[ii][jj] = int_list[n * 2 - jj]
            #print("3. ii = %s " % jj)

        # 3 символа:
        elif ii != 0 and jj == 0:
            empty_matrix[ii][jj] = int_list[n * 3 - ii - 1]
            #print("4. ii = %s " % ii)

        # 3 символа:
        elif ii == 1 and 0 < jj < m_con - 1:
            empty_matrix[ii][jj] = int_list[n * 3 + jj - 2]
            #print("4. ii = %s " % ii)

        # 2 символа:
        elif 0 < ii < m_str - 1 and jj == m_con - 2:
            empty_matrix[ii][jj] = int_list[n * 3 + ii]
            #print("4. ii = %s " % ii)

        # 2 символа:
        elif ii == m_str - 2 and 0 < jj < m_con - 2:
            empty_matrix[ii][jj] = int_list[n * 4 - jj + 1]
            #print("4. ii = %s " % ii)

        # 1 символ:
        elif ii == 2 and 0 < jj < m_con - 2:
            empty_matrix[ii][jj] = int_list[n * 4 + jj]
            #print("4. ii = %s " % ii)


print(int_list)
print()
for x, xx in enumerate(empty_matrix):
    print(empty_matrix[x])
#print(m_str, m_con)

"""
a = [[j for j in range(n)] for i in range(n)]
c.append(a)
"""