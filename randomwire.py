#!/usr/bin/env python

'''
This is a simple program that uses 468/f at all band edges of interest.  Red
boxes are drawn from edge to edge indicating spans of resonance for
particular frequencies.  At resonant frequency highest voltage is at the end
of an end fed and difficult to match.  If you have a modest antenna tuner,
avoid these areas.  If you have a capable tuner, -use- these areas since
signal is strongest.

Bands must be in: 160,80,60,40,30,20,17,15,12,10,6 m

Usage example up to half wavelength:
  endfed.py 40 20 15 10

Usage example up to full wavelength:
  endfed.py -f 40 20 15 10

or to generate the same in meters:
  endfed.py -m 40 20 15 10

and a graph pops up.  Red areas indicate highest voltage at end of wire.
Mouse cursor can be moved on image to read values.  Image can also be saved
as a png.

Mike Markowski, ab3ap
mike.ab3ap@gmail.com
May 2025
'''

import matplotlib.pyplot as plt
import numpy as np
import os, sys

hamBandsExtra_MHz = { # Band edges, USA Extra.
    160:np.array([1.8,     2]),
     80:np.array([3.5,     4]),
     60:np.array([5.335,   5.405]),
     40:np.array([7,       7.3]),
     30:np.array([10.1,   10.15]),
     20:np.array([14,     14.35]),
     17:np.array([18.068, 18.168]),
     15:np.array([21,     21.45]),
     12:np.array([24.89,  24.99]),
     10:np.array([28,     29.7]),
      6:np.array([50,     54])
}

hamBandsCw_MHz = { # Band edges, CW.  160m and 6m, shared modes.
    160:np.array([1.8,     2]),
     80:np.array([3.5,     3.6]),
     60:np.array([5.335,   5.405]),
     40:np.array([7,       7.125]),
     30:np.array([10.1,   10.15]),
     20:np.array([14,     14.15]),
     17:np.array([18.068, 18.11]),
     15:np.array([21,     21.2]),
     12:np.array([24.89,  24.93]),
     10:np.array([28,     28.3]),
      6:np.array([50,     54])
}

def cli(argv):
    '''Pull band values from command line.  Values are sorted in reverse
    order and for each band its low and high frequency edges are returned.

    Input:
      string[]: command line arguments.
    Output:
      [float[]]: list of 2-elt numpy arrays of band edge min, max in MHz.
    '''
    prog = os.path.basename(argv[0])
    argv = argv[1:]
    cw = fullwave = metric = False
    bands = []
    i = 0
    while i < len(argv):
        if argv[i] == '-c': # Use CW sub-bands.
            cw = True
        elif argv[i] == '-f': # Fullwave calculations.
            fullwave = True
        elif argv[i] == '-m': # Output lengths in meters.
            metric = True
        else: # Integer ham band.
            try:
                band = int(argv[i])
            except ValueError:
                usage(prog)
            if not band in hamBandsExtra_MHz:
                usage(prog)
            bands.append(int(argv[i]))
        i += 1
    if len(bands) == 0: # User didn't specify any bands.
        usage(prog)
    bands.sort(reverse=True) # Sort bands, high to low.
    return prog, bands, cw, metric, fullwave

def graph(title, edges_ft, metric, min_ft):
    '''Plot a red box for each span of resonant frequencies.
    '''

    if metric:
        cvt = 12/39.37 # Convert feet to meters.
        min_ft *= cvt # Not really feet anymore!
        edges_ft *= cvt

    plt.figure(figsize=(8, 1.25), dpi=120)
    plt.title(title, fontsize=10)
    plt.xlabel('Wire Length (%s)' % ('m' if metric else 'ft'))
    plt.yticks([]) # Don't label y axis.
    plt.ylim(0,1)  # Arbitrary values for rectangle heights.
    plt.grid(True)

    for e in edges_ft:
        plt.fill([e[0],e[0],e[1],e[1]], [0,1,1,0], 'r') # Xs, Ys, red.
    plt.xlim(min_ft, edges_ft[0][1]) # Min,max wire lengths.
    plt.tight_layout()
    plt.show()

def high_V(band_MHz, max_ft):
    '''Resonant frequencies have highest voltages at ends of antennas.
    Input:
      band_kHz (float[]): kHz, np.array of min and max frequencies.
      max_ft (float): ft, length for largest wavelength considered.
    Output:
      [float[]]: list of 2-elt numpy arrays of band edge min, max in MHz.
    '''

    e1_ft, e0_ft = 468/band_MHz # Band edge lengths, it's all based on this!
    i = 1 + np.arange(max_ft//e0_ft) # Count 1/2 wavelengths.
    return np.array([i*e0_ft, i*e1_ft]).T # Two columns lo,hi band lengths.

def usage(prog):
    print('Usage: %s [-c] [-f] [-m] band...' % prog)
    print('       -c, CW subbands.')
    print('       -f, graph fullwave (halfwave default).')
    print('       -m, metric lengths.')
    print('       band, integers in 160,80,60,40,30,20,17,15,12,10,6 m')
    print('       E.g., %s 40 20 15 10' % prog)
    sys.exit(1)

def main(argv):
    prog, bands_m, cw, metric, fullwave = cli(argv)
    hamBands_MHz = hamBandsCw_MHz if cw else hamBandsExtra_MHz
    bands_MHz = np.array([hamBands_MHz[i] for i in bands_m]) # Band edge freqs.

    min_ft = 234/bands_MHz[0][0] # Min length is 1/4 wavelength at lowest freq.
    scale = 4 if fullwave else 2 # Full or half wavelength.
    max_ft = scale*min_ft        # Max wire length to consider.

    all_ft = []
    for band_MHz in bands_MHz:
        all_ft.extend(high_V(band_MHz, max_ft))

    title = 'High Voltage Lengths for %s m' % str(bands_m)[1:-1]
    graph(title, np.array(all_ft), metric, min_ft)

if __name__ == '__main__':
    main(sys.argv)