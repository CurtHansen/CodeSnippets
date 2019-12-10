import pandas as pd


def compute_cross_corrs(datax, datay, lags):

    if not isinstance(datax, pd.Series):
        raise TypeError('First argument must be Pandas series!')
    if not isinstance(datay, pd.Series):
        raise TypeError('Second argument must be Pandas series!')

    if not (datax.index.name == 'date' and datay.index.name == 'date'):
        raise ValueError("Both series must have 'date' as index!")

    combined_data = pd.concat([datax, datay], axis=1, join='inner')
    if len(combined_data) == 0:
        raise ValueError("Inputs have no overlapping index values!")
    combined_data.columns = ['x', 'y']

    all_corrs = {}
    for lag in lags:
        all_corrs[lag] = crosscorr(combined_data['x'], combined_data['y'], lag)

    return all_corrs


def crosscorr(datax, datay, lag=0):
    """
    Lag-N cross correlation.
    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length

    Returns
    ----------
    crosscorr : float
    See https://stackoverflow.com/questions/33171413/cross-correlation-time-lag-correlation-with-pandas
    """
    return datax.corr(datay.shift(lag))