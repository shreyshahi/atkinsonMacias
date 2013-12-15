''' Implementation of the BC Hydro model'''
import numpy as np
import itertools
import model

def interpolateSpectra(spectra1 , spectra2 , period1, period2, period):
    slope = (spectra2 - spectra1)/(np.log10(period2) - np.log10(period1))
    return spectra1 + slope*(np.log10(period) - np.log10(period1))

def fixPeriods(augmentedSpectra, periods, augmentedPeriods):
    fixedSpectra = np.zeros((augmentedSpectra.shape[0], periods.shape[0]))
    sortedAugmented = sorted(augmentedPeriods)

    for i, per in enumerate(periods):
        if per in augmentedPeriods:
            fixedSpectra[:, i] = augmentedSpectra[:, 0]
            fixedSpectra[:, i] = augmentedSpectra[:, np.nonzero(augmentedPeriods == per)[0][0]]
        else:
            idxLow = np.nonzero(sortedAugmented < per)[0][-1]
            perLow = sortedAugmented[idxLow]
            idxLow = np.nonzero(augmentedPeriods == perLow)[0][0]

            idxHigh = np.nonzero(sortedAugmented > per)[0][0]
            perHigh = sortedAugmented[idxHigh]
            idxHigh = np.nonzero(augmentedPeriods == perHigh)[0][0]

            fixedSpectra[:, i] = interpolateSpectra(augmentedSpectra[:, idxLow] , augmentedSpectra[:, idxHigh] , augmentedPeriods[idxLow] , augmentedPeriods[idxHigh] , per)
    return fixedSpectra

def augmentPeriods(periods):
    availablePeriods = np.array([0.01, 0.05, 0.063, 0.079, 0.1, 0.125, 0.16, 0.2, 0.25, 0.32, 0.4, 0.5, 0.63, 0.79, 1.0, 1.26, 1.59, 2.0, 2.5, 3.125, 4.0, 5.0, 6.25, 7.69, 10.0])
    modifiedPeriods = []
    for period in periods:
        if period in availablePeriods:
            modifiedPeriods.append(period)
        else:
            idxLow = np.nonzero(availablePeriods < period)[0][-1]
            modifiedPeriods.append(availablePeriods[idxLow])
            idxHigh = np.nonzero(availablePeriods > period)[0][0]
            modifiedPeriods.append(availablePeriods[idxHigh])
    return modifiedPeriods

def spectra(M, Rrup, periods):
    periods = np.array(periods)
    idx = np.nonzero(periods <= 0.01)[0]
    periods[idx] = 0.01 # Periods less than eq to 0.01 are essentially pga. Setting this allows us to avoid errors while interpolating in log-log scale.
    augmentedPeriods = augmentPeriods(periods)

    R = Rrup
    nRow = len(M)
    nCol = len(augmentedPeriods)

    M = np.array([M] * nCol).transpose()
    R = np.array([R] * nCol).transpose()

    augmentedPeriods = np.array([augmentedPeriods] * nRow)

    augmentedSpectra = np.array([[model.computeSpectra(mag, r, per) for mag, r, per in itertools.izip(mags, rs, pers)] for mags, rs, pers in itertools.izip(M, R, augmentedPeriods)])

    fixedSpectra = fixPeriods(augmentedSpectra, periods, augmentedPeriods[0])

    # convert to cm/s/s
    fixedSpectra = 10**fixedSpectra

    sigma = model.sigma(periods) * nRow

    return fixedSpectra.tolist(), sigma
