'''
Code to produce SDSS and 2MASS photometric response for M dwarf flares, from M0 to M6.

Note this model only simulates the peak flare flux.

This Python code is a translation of the original IDL functions written for Davenport et al. (2012)
http://adsabs.harvard.edu/abs/2012ApJ...748...58D
'''

import numpy as np

def flaregrid(mag, filter='u', sptype=0):
    '''
    main function to model ugrizJHK flare response

    Parameters
    ----------
    mag : float
        Input flare response, in magnitudes
    filter : str, optional
        Filter of the input flare response, can be any of 'ugrizJHK', or 0 to 7
    sptype : int, optional
        Spectral type to model, from M0 to M6, written as 0 to 6. (Default is 0)

    Returns
    -------
    array of flare responses
    '''

    fN = 0
    if filter.lower() == 'u':
        fN = 0
    if filter.lower() == 'g':
        fN = 1
    if filter.lower() == 'r':
        fN = 2
    if filter.lower() == 'i':
        fN = 3
    if filter.lower() == 'z':
        fN = 4
    if filter.lower() == 'j':
        fN = 5
    if filter.lower() == 'h':
        fN = 6
    if filter.lower() == 'k':
        fN = 7


    # note this file needs to be in the working directory at the moment
    # this can be fixed later by sniffing out the code dir
    fgrid = np.load('fgrid.npy')

    u = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 0, sptype][::-1])
    g = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 1, sptype][::-1])
    r = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 2, sptype][::-1])
    i = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 3, sptype][::-1])
    z = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 4, sptype][::-1])
    j = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 5, sptype][::-1])
    h = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 6, sptype][::-1])
    k = np.interp(mag, fgrid[:, fN, sptype][::-1], fgrid[:, 7, sptype][::-1])


    out = [u,g,r,i,z,j,h,k]

    return out