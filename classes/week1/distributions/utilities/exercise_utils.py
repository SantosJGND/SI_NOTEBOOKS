from typing import Union

import numpy as np
import pandas as pd
import scipy.stats as stats


def website_vists_per_day(avg: int = 1000, ndays: int = 365):
    # set seed to 42
    np.random.seed(42)

    return stats.poisson.rvs(avg, size=ndays)


def convert_visitors(visitors: int, conversion_rate: float = 0.01):
    # set seed to 42
    np.random.seed(42)
    return stats.binom.rvs(visitors, conversion_rate)


def website_conversion_data(
    avg_visits: int = 1000, ndays: int = 365, conversion_rate: float = 0.01
):
    # set up a dataframe with the number of visits and the number of conversions
    # for each day
    # set seed to 42
    # return the dataframe

    visits = website_vists_per_day(avg_visits, ndays)
    df = pd.DataFrame({"visits": visits})
    df["conversions"] = df["visits"].apply(
        convert_visitors, conversion_rate=conversion_rate
    )
    return df


def monte_carlo_simulation(
    initial_price: float, days: int, daily_returns: Union[np.ndarray, list]
):
    stock_prices = [initial_price]

    for i in range(1, days):
        price = stock_prices[-1] * (1 + daily_returns[i])
        stock_prices.append(price)

    return stock_prices


def historical_returns_data():
    # set seed
    # np.random.seed(6)
    #
    return np.random.normal(0.001, 0.02, 1000)
