import math


def mean(data):
    return sum(data) / len(data)


def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    return sorted_data[n // 2]


def quartiles(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1 = median(sorted_data[: n // 2])
    q2 = median(sorted_data)
    q3 = median(sorted_data[(n + 1) // 2 :])
    return q1, q2, q3


def standard_deviation(data):
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / len(data)
    return math.sqrt(variance)


def covariance(data1, data2):
    mean1 = mean(data1)
    mean2 = mean(data2)
    cov = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2)) / len(data1)
    return cov


def correlation(data1, data2):
    cov = covariance(data1, data2)
    std1 = standard_deviation(data1)
    std2 = standard_deviation(data2)
    correlation_coefficient = cov / (std1 * std2)
    return correlation_coefficient
