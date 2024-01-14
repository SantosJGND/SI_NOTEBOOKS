import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def plot_poisson_test(observed_clicks, total_users, null_ctr, alpha):
    # Calculate the p-value
    # Calculate the test statistic (clicks)
    test_statistic = observed_clicks
    p_value = 1 - stats.poisson.cdf(test_statistic, total_users * null_ctr)

    # Perform hypothesis testing
    if p_value < alpha:
        hypothesis_result = "Reject the null hypothesis"
    else:
        hypothesis_result = "Accept the null hypothesis"

    # upper boundary of the rejection region
    upper_bound = stats.poisson.ppf(1 - alpha, total_users * null_ctr)

    # Generate x values for the plot
    x = np.arange(0, total_users + 1)

    # Generate y values for the Poisson distribution
    y = stats.poisson.pmf(x, total_users * null_ctr)

    # Plot the Poisson distribution
    plt.plot(x, y, "b-", linewidth=2)

    # Highlight the observed click-through rate
    plt.plot(
        observed_clicks,
        stats.poisson.pmf(observed_clicks, total_users * null_ctr),
        "ro",
    )

    # fill the area after the critical value
    plt.fill_between(x, y, where=(x >= upper_bound), color="red", alpha=0.3)

    # add legend for rejection region
    plt.legend(["Null Distribution", "Observed Clicks", "Rejection Region"])

    # Set plot labels and title
    plt.xlabel("Number of Clicks")
    plt.ylabel("Probability")
    plt.title("Poisson Distribution: Click-Through Rates")

    # Add legend and hypothesis result
    # plt.legend(['Null Distribution', 'Observed Clicks'])
    plt.text(40, 0.09, hypothesis_result)
    plt.text(45, 0.07, f"p-value: {p_value:.6f}")

    # Show the plot
    plt.show()


def plot_two_sample_t_test(
    class1_mean, class1_std, class2_mean, class2_std, class_size, alpha
):
    # generate the data
    np.random.seed(123456789)

    class1_scores = np.random.normal(class1_mean, class1_std, class_size)
    class2_scores = np.random.normal(class2_mean, class2_std, class_size)

    # calculate the difference in means
    mean_class1 = np.mean(class1_scores)
    mean_class2 = np.mean(class2_scores)
    mean_diff = mean_class1 - mean_class2

    # calculate the standard error of the difference in means
    std_class1 = np.std(class1_scores)
    std_class2 = np.std(class2_scores)

    # calculate the degrees of freedom
    n1 = len(class1_scores)
    n2 = len(class2_scores)
    df = n1 + n2 - 2

    # calculate pooled variance
    n1 = len(class1_scores)
    n2 = len(class2_scores)
    pooled_var = ((n1 - 1) * std_class1**2 + (n2 - 1) * std_class2**2) / (
        n1 + n2 - 2
    )

    # calculate interval bounds
    t_crit = stats.t.ppf(1 - alpha / 2, df=df)
    margin_of_error = t_crit * np.sqrt(pooled_var * (1 / n1 + 1 / n2))
    ci_lower = mean_diff - margin_of_error
    ci_upper = mean_diff + margin_of_error

    # calculate the t-statistic
    t_stat = mean_diff / np.sqrt(pooled_var * (1 / n1 + 1 / n2))
    # calculate the p-value
    p_value = (1 - stats.t.cdf(abs(t_stat), df=df)) * 2

    ## Plot the distributions
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # plot histogram of class scores on the left subplot
    ax1.hist(class1_scores, bins=10, alpha=0.5, label="Class 1")
    ax1.hist(class2_scores, bins=10, alpha=0.5, label="Class 2")
    ax1.set_xlabel("Scores")
    ax1.set_ylabel("Frequency")
    ax1.set_title("Histogram of Class Scores")
    ax1.legend()

    # plot t-distribution on the right subplot
    x = np.linspace(-4, 4, 1000)
    y = stats.t.pdf(x, df=df)
    ax2.plot(x, y, "b-", linewidth=2)
    ax2.axvline(t_stat, color="r", linestyle="--", label="t-statistic")
    ax2.annotate(
        f"t-statistic = {t_stat:.2f}",
        xy=(t_stat, 0.15),
        xytext=(2, 0.25),
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )

    # text with the p-value
    ax2.annotate(f"p-value = {p_value:.6f}", xy=(t_stat, 0.10), xytext=(1.18, 0.30))

    ax2.set_xlabel("t")
    ax2.set_ylabel("Probability Density")
    ax2.set_title("t-Distribution")
    ax2.legend()

    # adjust spacing between subplots
    plt.subplots_adjust(wspace=0.3)

    # display the figure
    plt.show()
