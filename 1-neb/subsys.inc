&SUBSYS
  &CELL
    PERIODIC NONE                       ! System is not periodic
    ABC TODO TODO TODO                  ! Dimensions of the simulation cell in angstroms
  &END CELL
  &TOPOLOGY                             ! Specify input coordinate format and filename
    COORD_FILE_FORMAT XYZ
    COORD_FILE_NAME ${XYZ_NAME}
  &END TOPOLOGY
  &KIND H                               ! Basis sets and pseudopotential for hydrogen
    BASIS_SET DZVP-MOLOPT-SR-GTH
    POTENTIAL GTH-PBE-q1
  &END KIND
  &KIND C                               ! Basis sets and pseudopotential for carbon
    BASIS_SET DZVP-MOLOPT-SR-GTH
    POTENTIAL GTH-PBE-q4
  &END KIND
  &KIND O                               ! Basis sets and pseudopotential for oxygen
    BASIS_SET DZVP-MOLOPT-SR-GTH
    POTENTIAL GTH-PBE-q6
  &END KIND
&END SUBSYS
