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
    b = 50
    hist, _ = np.histogram(rc, bins=b, range=(-1, 1), density=True)

    # Compute free energy and shift minimum to zero
    energy = -kT*np.log(hist/np.amax(hist))

    # Assign x-axes
    time = np.arange(len(rc))/2000
    rxn = np.linspace(-1, 1, b)

    # Plot
    _, ax = plt.subplots(3, 1)
    
    # Time evolution of the reaction coordinate
    ax[0].plot(time, rc)
    ax[0].set_xlabel('Time (ps)')
    ax[0].set_ylabel('Reaction coordinate (Å)')

    # Probability density of the reaction coordinate
    ax[1].plot(rxn, hist)
    ax[1].set_xlabel('Reaction coordinate (Å)')
    ax[1].set_ylabel('Probability density')
    
    # Helmholtz free energy profile
    ax[2].plot(rxn, energy)
    ax[2].set_xlabel('Reaction coordinate (Å)')
    ax[2].set_ylabel('Free energy (meV)')
    
    plt.show()

if __name__ == '__main__':
    main()
