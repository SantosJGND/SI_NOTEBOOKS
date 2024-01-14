import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import ttest_ind


def plot_t_test(perm_t_stats, t_stat):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    # Plot the distribution of t-statistics on the left subplot
    axs[0].hist(perm_t_stats, bins=20, alpha=0.5, label="Permutation Test")
    axs[0].axvline(x=t_stat, color="red", linestyle="--", label="Observed t-statistic")
    axs[0].set_xlabel("t-statistic")
    axs[0].set_ylabel("Frequency")
    axs[0].set_title("Distribution of t-statistics")
    axs[0].legend()

    # Plot the CDF of the observed t-statistic on the right subplot
    sorted_t_stats = np.sort(perm_t_stats)
    cdf = np.arange(1, len(sorted_t_stats) + 1) / len(sorted_t_stats)
    axs[1].plot(sorted_t_stats, cdf)
    axs[1].axvline(x=t_stat, color="red", linestyle="--", label="Observed t-statistic")
    axs[1].set_xlabel("t-statistic")
    axs[1].set_ylabel("Cumulative Probability")
    axs[1].set_title("CDF of Observed t-statistic")
    axs[1].legend()

    # Adjust spacing between subplots
    fig.tight_layout()

    # Show the plot
    plt.show()
