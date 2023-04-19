&DFT
  RESTART_FILE_NAME ${WFN_NAME}
  BASIS_SET_FILE_NAME BASIS_MOLOPT
  &QS
    EPS_DEFAULT 1.0E-12                 ! Sets convergence criteria so that energy should be accurate up to this value
  &END QS
  &POISSON                              ! How to deal with electrostatics
    PERIODIC NONE                       ! System is not periodic
    POISSON_SOLVER WAVELET              ! Efficient solver for non-periodic system
  &END POISSON
  &SCF
    SCF_GUESS TODO                      ! Initial density guess is a simple superposition of atomic charge densities
    EPS_SCF 1.0E-6                      ! Energy convergence criteria (atomic units)
    &OT                                 ! Use orbital transformation method instead of brute-force diagonalization
      ALGORITHM IRAC                    ! OT algorithm
      MINIMIZER DIIS                    ! Minimization algorithm
      PRECONDITIONER FULL_ALL           ! Preconditioner for the minimizer
    &END OT
    MAX_SCF 20                          ! Maximum number of SCF steps before rebuilding preconditioner
    &OUTER_SCF ON
      EPS_SCF 1.0E-6                    ! Outer loop energy convergence criteria (atomic units)
      MAX_SCF 12                        ! Maximum number of preconditioner rebuilds before terminating
    &END OUTER_SCF
    &PRINT
      &RESTART
        BACKUP_COPIES 0                 ! Avoid excessive printing of restart files
      &END RESTART
    &END PRINT
  &END SCF
  &XC
    &XC_FUNCTIONAL PBE                  ! Exchange-correlation funtional to use
    &END XC_FUNCTIONAL
  &END XC
&END DFT
