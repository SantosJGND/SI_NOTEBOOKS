import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def plot_distributions(distribution, parameters, num_samples):
    # Initialize dictionary to store means by sample size
    means_by_sample_size = {}
    sample_sizes = [10, 50, 100, 500]
    # Perform simulations and calculate means
    for sample_size in sample_sizes:
        means = []
        for _ in range(num_samples):
            if distribution in parameters:
                params = parameters[distribution]
                sample = getattr(np.random, distribution)(size=sample_size, **params)
            else:
                print("Distribution not available")
                break

            mean = np.mean(sample)
            means.append(mean)
        means_by_sample_size[sample_size] = means

    # Create a figure with four subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Plot histograms of means for each sample size
    for i, sample_size in enumerate(sample_sizes):
        row = i // 2
        col = i % 2
        axs[row, col].hist(means_by_sample_size[sample_size], bins=30, density=True)
        axs[row, col].set_title(f"Sample Size: {sample_size}")
        axs[row, col].set_xlabel("Mean")
        axs[row, col].set_ylabel("Density")

    # Adjust spacing between subplots
    fig.tight_layout()

    # Show the plot
    plt.show()


def plot_sample_means(population_mean, sample_sizes, num_trials):
    sample_means = []

    for sample_size in sample_sizes:
        means = []
        for _ in range(num_trials):
            samples = np.random.normal(population_mean, 1, sample_size)
            means.append(np.mean(samples))
        sample_means.append(means)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot(sample_means)
    ax.axhline(
        y=population_mean, color="orange", linestyle="--", label="True Population Mean"
    )
    ax.set_xticklabels(sample_sizes)
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Sample Mean")
    ax.set_title("Sample Means for Different Sample Sizes")
    ax.legend()

    plt.show()


def plot_sample_means_histogram(population_mean, sample_sizes, num_trials):
    sample_means = []

    for sample_size in sample_sizes:
        means = []
        for _ in range(num_trials):
            samples = np.random.normal(population_mean, 1, sample_size)
            means.append(np.mean(samples))
        sample_means.append(means)

    fig, ax = plt.subplots(figsize=(8, 6))

    for i, means in enumerate(sample_means):
        ax.hist(means, alpha=0.6, label=f"Sample Size: {sample_sizes[i]}", bins=30)

    ax.axvline(
        x=population_mean, color="orange", linestyle="--", label="True Population Mean"
    )
    ax.set_xlabel("Sample Mean")
    ax.set_ylabel("Frequency")
    ax.set_title("Overlapped Histograms of Sample Means")
    ax.legend()

    plt.show()


def plot_exponential_convergence(lambda_, sample_sizes, num_trials):
    means = []
    variances = []

    for sample_size in sample_sizes:
        sample_means = []
        sample_variances = []
        for _ in range(num_trials):
            samples = np.random.exponential(1 / lambda_, sample_size)
            sample_means.append(np.mean(samples))
            sample_variances.append(np.std(samples, ddof=1))
        means.append(sample_means)
        variances.append(sample_variances)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.boxplot(means)
    ax1.set_xticklabels(sample_sizes)
    ax1.set_xlabel("Sample Size")
    ax1.set_ylabel("Sample Mean")
    ax1.set_title("Convergence of Sample Mean")
    # add dashed horizontal line for population mean
    ax1.axhline(
        y=1 / lambda_, color="orange", linestyle="--", label="True Population Mean"
    )

    ax2.boxplot(variances)
    ax2.set_xticklabels(sample_sizes)
    ax2.set_xlabel("Sample Size")
    ax2.set_ylabel("Sample Variance")
    ax2.set_title("Convergence of Population Std")
    # add dashed horizontal line for population std
    ax2.axhline(
        y=1 / lambda_, color="orange", linestyle="--", label="True Population Std"
    )

    plt.legend()

    plt.tight_layout()
    plt.show()
