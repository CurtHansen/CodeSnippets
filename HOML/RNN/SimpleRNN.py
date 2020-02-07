import numpy as np


def generate_time_series(nseries,
                         nsteps):

    freqs1, freqs2, offsets1, offsets2 = np.randon.rand(4, nseries, 1)
    time = np.linspace(0, 1, nsteps)
    series = 0.5 * np.sin((time - offsets1) * (freqs1 * 10 + 10))
    series += 0.2 * np.sin((time - offsets2) * (freqs2 * 20 + 20))
    series += 0.1 * (np.random.random(nseries, nsteps) - 0.5)
    return series[..., np.newaxis].astype(np.float32)



