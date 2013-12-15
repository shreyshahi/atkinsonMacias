'''
Implementation of the Ghofrani and Atkinson 2013 subduction ground motion model
'''
import gmm

def spectra(M, Rrup, periods):
    '''
    The function takes the source, site, and distance parameters and returns the predicted response spectra, intra event sigma (:math:`\\phi`), and inter event sigma (:math:`\\tau`) at the requested periods.

    :param M: List of magnitudes for which the response spectra is needed.
    :type M: list(float)
    :param Rrup: List with closest distance to rupture for sites at which spectra is needed. Rrup is needed for Interface events. Filler values like -999 can be passed as Rrup for Intraslab events.
    :type Rrup: list(float)
    :param periods: List of periods at which the spectra is needed.
    :type periods: list(float)
    '''

    argumentLengths = [len(M) , len(Rrup)]

    if any([ (l != argumentLengths[0]) for l in argumentLengths]):
        raise Exception("Argument lengths not equal")

    if len(periods) == 0:
        raise Exception("Periods argument is empty")

    return gmm.spectra(M, Rrup, periods)
