import sys
import numpy as np
import matplotlib.pyplot as plt
from ase.io import read


def main():

    # Thermal energy at room temperature in meV
    kT = 25.85

    # Read input trajectory
    try:
        trj = read(sys.argv[1], index=':')
    except:
        print('Usage: python3 energy.py filename.xyz')

    # Initialize array for reaction coordinate
    rc = np.zeros(len(trj))

    # Loop over trajectory, relevant atoms indices are hard-coded
    for i, frame in enumerate(trj):
        rc[i] = frame.get_distance(10, 14)-frame.get_distance(12,14)

    # Calculate probability density
    hist, _ = np.histogram(rc, bins=50, range=(-1, 1), density=True)

    # Compute free energy and shift minimum to zero
    energy = -kT*np.log(hist)
    energy = energy-np.amin(energy)

    # Plot
    fig, ax = plt.subplots(3, 1)
    ax[0].plot(np.arange(len(rc))/2000, rc)
    ax[0].set_xlabel('Time (ps)')
    ax[0].set_ylabel('Reaction coordinate (Å)')
    ax[1].plot(hist)
    ax[1].set_xlabel('Reaction coordinate (Å)')
    ax[1].set_ylabel('Probability density')
    ax[2].plot(energy)
    ax[2].set_xlabel('Reaction coordinate (Å)')
    ax[2].set_ylabel('Free energy (meV)')
    plt.show()

if __name__ == '__main__':
    main()
