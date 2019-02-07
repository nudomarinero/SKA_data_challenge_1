"""
Repair beam information in the images
"""
import os
from config import DATA_PATH
from astropy.io import fits


times = ("8h", "100h", "1000h")
bands = ("B1", "B2", "B5")
beams = (1.5, 0.60, 0.0913)


def repair_beam_info(fits_file, beam):
    """Add the beam information to the FITS file
    """
    with fits.open(fits_file, 'update') as f:
        f[0].header['BPA'] = 0
        f[0].header['BMAJ'] = beam
        f[0].header['BMIN'] = beam


if __name__ == "__main__":
    for i, band in enumerate(bands):
        for time in times:
            fits_name = "SKAMid_{}_{}.fit".format(band, time)
            fits_file = os.path.join(DATA_PATH, fits_name)
            print("Repair: {}".format(fits_name))
            repair_beam_info(fits_file, beams[i])

        