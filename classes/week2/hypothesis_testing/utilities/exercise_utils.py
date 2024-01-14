# sgenerate a set of exam scores with population mean 80 and standard deviation 5

import random

import matplotlib.pyplot as plt
import numpy as np


def generate_scores(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(80, 5))
    return scores


def generate_conversion_scores_with_feature(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(0.1, 0.01))
    return scores


def generate_conversion_scores_without_feature(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(0.08, 0.01))
    return scores


def generate_blood_pressure_before(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(120, 10))
    return scores


def generate_blood_pressure_after(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(100, 10))
    return scores


def trial_with_drug(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(0.55, 0.1))
    return scores


def trial_with_placebo(n):
    scores = []
    for i in range(n):
        scores.append(random.gauss(0.5, 0.1))
    return scores


# generate contingency table of product preferences across age groups


def generate_product_preferences(n):
    table = np.zeros((3, 3))
    for i in range(n):
        age = random.randint(0, 2)
        product = random.randint(0, 2)
        table[age, product] += 1
    return table
