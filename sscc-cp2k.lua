-- Jupyter

depends_on("gcc/14.2.0")
depends_on("openmpi/5.0.6")
depends_on("cp2k/2025.1")
prepend_path('PATH',"/projappl/project_2017403/sscc-2026-cp2k/bin")

setenv("_COURSE_BASE_NAME","sscc-2026")
setenv("_COURSE_NOTEBOOK","sscc-cp2k/Part-1-NEB/Part-1-NEB.ipynb")
setenv("_COURSE_GIT_REPO","https://github.com/csc-training/sscc-cp2k")
setenv("_COURSE_GIT_REF","")
setenv("_COURSE_NOTEBOOK_TYPE","lab")
