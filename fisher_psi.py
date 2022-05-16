# Вычисление критерия ф* — углового преобразования Фишера (критерия Фишера)
# https://studme.org/208002/matematika_himiya_fizik/vychislenie_kriteriya_uglovogo_preobrazovaniya_fishera_kriteriya_fishera

# Таблицы
# https://nashaucheba.ru/v27675/погребицкая_м.в._математические_методы_в_психологии?page=15
import math

# Levels of statistical registration of various values of the Fisher psi criteria
fisher_significant_table = {
    "0.00": [2.91, 2.81, 2.70, 2.62, 2.55, 2.49, 2.44, 2.39, 2.35],
    "0.01": [2.31, 2.28, 2.25, 2.22, 2.19, 2.16, 2.14, 2.11, 2.09, 2.07],
    "0.02": [2.05, 2.03, 2.01, 1.99, 1.97, 1.96, 1.94, 1.92, 1.91, 1.89],
    "0.03": [1.88, 1.86, 1.85, 1.84, 1.82, 1.81, 1.80, 1.79, 1.77, 1.76],
    "0.04": [1.75, 1.74, 1.73, 1.72, 1.71, 1.70, 1.68, 1.67, 1.66, 1.65],
    "0.05": [1.64, 1.64, 1.63, 1.62, 1.61, 1.60, 1.59, 1.58, 1.57, 1.56],
    "0.06": [1.48, 1.47, 1.46, 1.46, 1.45, 1.44, 1.43, 1.43, 1.42, 1.41],
    "0.07": [1.41, 1.40, 1.39, 1.39, 1.38, 1.37, 1.37, 1.36, 1.36, 1.35],
    "0.08": [1.34, 1.34, 1.33, 1.32, 1.32, 1.31, 1.31, 1.30, 1.30, 1.29]}


def fisher_significant(psi):
    for key, val in fisher_significant_table.items():
        if val[-1] <= psi <= val[0]:
            significant = float(key)
            for ind in range(0, len(val) - 1):
                if val[ind + 1] < psi <= val[ind]:
                    return round(significant, 3)
                significant += 0.001
    return 1


def fisher_psi(data):
    phi1 = 2 * math.asin(math.sqrt(data[0][0]))
    phi2 = 2 * math.asin(math.sqrt(data[0][1]))
    fisher = abs(phi1 - phi2) * math.sqrt(data[1][0] * data[1][1] / (data[1][0] + data[1][1]))
    p = fisher_significant(fisher)
    return fisher, p


if __name__ == '__main__':
    print(fisher_psi([[0.857, 0.667], [28, 30]]))
    print(fisher_psi([[0.107, 0.267], [28, 30]]))
