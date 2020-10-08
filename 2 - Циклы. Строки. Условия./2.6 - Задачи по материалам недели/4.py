str_input = str(input())

stop_word = "end"

if str_input != stop_word:
    matrix = [str_input.split()]

    # Ввод значений матрицы построчно, до строки "end":
    while str_input != stop_word:
        str_input = str(input())
        if str_input != stop_word and str_input != "":
            matrix.append(str_input.split())
        else:
            break

    # Глубокое копирование матрицы:
    matrix_copy = matrix[:]
    for n, m in enumerate(matrix):
        matrix_copy[n] = matrix[n][:]

    # Многомерный цикл:
    for i, ii in enumerate(matrix):
        for j, jj in enumerate(ii):
            
            len_str = len(matrix)
            len_col = len(ii)
            m_str_end = len_str - 1
            m_col_end = len_col - 1

            # Матрица 1х1:
            if len_str == 1 and len_col == 1:
                matrix_copy[i][j] = str(int(matrix[i][j]) * 4)

            # Квадратная или произвольная матрица:
            elif (len_str == len_col) or (len_str != len_col and len_str, len_col != 1):

                # 1:
                if i == 0 and j == 0:
                    up = int(matrix[m_str_end][j])
                    down = int(matrix[i + 1][j])
                    left = int(matrix[i][m_col_end])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 2 - середина:
                elif i == 0 and 0 < j < m_col_end:
                    up = int(matrix[m_str_end][j])
                    down = int(matrix[i + 1][j])
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 3:
                elif i == 0 and j == m_col_end:
                    up = int(matrix[m_str_end][j])
                    down = int(matrix[i + 1][j])
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][0])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 4 - середина:
                elif 0 < i < m_str_end and j == 0:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[i + 1][j])
                    left = int(matrix[i][m_col_end])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 5 - центральные:
                elif 0 < i < m_str_end and 0 < j < m_col_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[i + 1][j])
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 6 - середина:
                elif 0 < i < m_str_end and j == m_col_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[i + 1][j])
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][0])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 7:
                elif i == m_str_end and j == 0:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[0][j])
                    left = int(matrix[i][m_col_end])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 8:
                elif i == m_str_end and 0 < j < m_col_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[0][j])
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up + down + left + right)

                # 9:
                elif i == m_str_end and j == m_col_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[0][j])
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][0])
                    matrix_copy[i][j] = str(up + down + left + right)

            # Матрица со столбцом = 1:
            elif len_str > 1 and len_col == 1:
                if i == 0:
                    up = int(matrix[m_str_end][j])
                    down = int(matrix[i + 1][j])
                    left_right = int(matrix[i][j]) * 2
                    matrix_copy[i][j] = str(up + down + left_right)

                elif i == m_str_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[0][j])
                    left_right = int(matrix[i][j]) * 2
                    matrix_copy[i][j] = str(up + down + left_right)

                elif 0 < i < m_str_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[i + 1][j])
                    left_right = int(matrix[i][j]) * 2
                    matrix_copy[i][j] = str(up + down + left_right)

            # Матрица со строчкой = 1:
            elif len_str == 1 and len_col > 1:
                if j == 0:
                    up_down = int(matrix[i][j]) * 2
                    left = int(matrix[i][m_col_end])
                    right = int(matrix[i][j+1])
                    matrix_copy[i][j] = str(up_down + left + right)

                elif j == m_col_end:
                    up_down = int(matrix[i][j]) * 2
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][0])
                    matrix_copy[i][j] = str(up_down + left + right)

                elif 0 < j < m_col_end:
                    up_down = int(matrix[i][j]) * 2
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][j + 1])
                    matrix_copy[i][j] = str(up_down + left + right)
            else:
                break

    # Вывод результата:
    if len(matrix_copy[:][:]) != 0:
        for z, zz in enumerate(matrix_copy):
            output_string = ""
            for x, xx in enumerate(zz):
                output_string += xx + " "
            print(output_string[:-1])
