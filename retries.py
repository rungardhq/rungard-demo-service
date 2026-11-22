"""How long a client waits between retries of a failed call."""


def backoff_delays(attempts: int, base: float, cap: float) -> list[float]:
    """The wait before each of `attempts` retries, in seconds.

    Delays are floats. The delay doubles from `base` on each retry and never exceeds `cap`,
    e.g. backoff_delays(5, 1, 10) -> [1, 2, 4, 8, 10].
    """
    return [float(base * 2**n) for n in range(attempts)]
