import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, expon, norm, poisson


class Distribution:
    def sample(self):
        pass

    def calculate_pdf(self):
        pass


class PoissonDistribution(Distribution):
    def __init__(self, sample_size, lam):
        self.sample_size = sample_size
        self.lam = lam

    def sample(self):
        return poisson.rvs(mu=self.lam, size=self.sample_size)

    def calculate_pdf(self):
        x = np.arange(0, self.lam * 3)
        y = poisson.pmf(x, mu=self.lam)
        return x, y


class BinomialDistribution(Distribution):
    def __init__(self, sample_size, n, p):
        self.sample_size = sample_size
        self.n = n
        self.p = p

    def sample(self):
        return binom.rvs(n=self.n, p=self.p, size=self.sample_size)

    def calculate_pdf(self):
        x = np.arange(0, self.n + 1)
        y = binom.pmf(x, n=self.n, p=self.p)
        return x, y


class NormalDistribution(Distribution):
    def __init__(self, sample_size, loc, scale):
        self.sample_size = sample_size
        self.loc = loc
        self.scale = scale

    def sample(self):
        return norm.rvs(loc=self.loc, scale=self.scale, size=self.sample_size)

    def calculate_pdf(self):
        x = np.linspace(self.loc - 3 * self.scale, self.loc + 3 * self.scale, 100)
        y = norm.pdf(x, loc=self.loc, scale=self.scale)
        return x, y


class ExponentialDistribution(Distribution):
    def __init__(self, sample_size, scale):
        self.sample_size = sample_size
        self.scale = scale

    def sample(self):
        return expon.rvs(scale=self.scale, size=self.sample_size)

    def calculate_pdf(self):
        x = np.linspace(0, self.scale * 3, 100)
        y = expon.pdf(x, scale=self.scale)
        return x, y


class DistributionHandler:
    def __init__(self, distribution):
        self.distribution = distribution

    def plot_distribution(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        sample = self.distribution.sample()
        ax1.hist(sample, color="blue", alpha=0.5, bins=30)
        ax1.set_xlabel("Value")
        ax1.set_ylabel("Frequency")

        x, y = self.distribution.calculate_pdf()
        ax2.plot(x, y, color="red")
        ax2.set_xlabel("Value")
        ax2.set_ylabel("Probability Density")
        ax2.set_xlim([min(sample), max(sample)])
        plt.show()


class CombinedDistribution:
    def __init__(self, distribution1, distribution2):
        self.distribution1 = distribution1
        self.distribution2 = distribution2

    def plot_distribution(self):
        fig, axs = plt.subplots(1, 2, figsize=(10, 4))

        sample_1 = self.distribution1.sample()
        sample_2 = self.distribution2.sample()
        # Plot overlapping histograms
        axs[0].hist(sample_1, color="red", alpha=0.8, label="Distribution 1")
        axs[0].hist(sample_2, color="blue", alpha=0.8, label="Distribution 2")
        axs[0].set_xlabel("Value")
        axs[0].set_ylabel("Frequency")
        axs[0].legend()

        # Plot overlapping PDFs
        x1, y1 = self.distribution1.calculate_pdf()
        x2, y2 = self.distribution2.calculate_pdf()

        # plot, set x range to same as histogram
        axs[1].plot(x1, y1, color="red", label="Distribution 1")
        axs[1].plot(x2, y2, color="blue", label="Distribution 2")
        axs[1].set_xlabel("Value")
        axs[1].set_ylabel("Probability Density")
        axs[1].set_xlim(
            [min(min(sample_1), min(sample_2)), max(max(sample_1), max(sample_2))]
        )
        axs[1].legend()

        plt.tight_layout()
        plt.show()

    def plot_boxplots(self):
        samples1 = self.distribution1.sample()
        samples2 = self.distribution2.sample()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.boxplot([samples1, samples2])
        ax.set_xticklabels(["Distribution 1", "Distribution 2"])
        ax.set_ylabel("Value")

        plt.show()
