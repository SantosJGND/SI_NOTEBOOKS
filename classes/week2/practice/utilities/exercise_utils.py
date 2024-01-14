import numpy as np


def drug_test_experiment(
    loc_1=7, scale_1=1.5, size_1=50, loc_2=8, scale_2=1.5, size_2=50
):
    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate the samples
    sample_1 = np.random.normal(loc=loc_1, scale=scale_1, size=size_1)
    sample_2 = np.random.normal(loc=loc_2, scale=scale_2, size=size_2)

    return sample_1, sample_2


def sleep_survey_data(loc=7, scale=1.5, size=50):
    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate the samples
    sample = np.random.normal(loc=loc, scale=scale, size=size)

    return sample


import numpy as np


def generate_conversion_scores_with_feature(n):
    # Set random seed for reproducibility
    np.random.seed(42)

    scores = []
    for i in range(n):
        scores.append(random.gauss(0.1, 0.01))
    return scores


def generate_conversion_scores_without_feature(n):
    # Set random seed for reproducibility
    np.random.seed(42)

    scores = []
    for i in range(n):
        scores.append(random.gauss(0.08, 0.01))
    return scores
