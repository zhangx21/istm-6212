# istm-6212
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "nbgrader": {
     "grade": false,
     "solution": false
    }
   },
   "source": [
    "Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\\rightarrow$Run All).\n",
    "\n",
    "Make sure you fill in any place that says `YOUR CODE HERE` or \"YOUR ANSWER HERE\", as well as your name and collaborators below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "NAME = \"Xing Zhang\"\n",
    "COLLABORATORS = \"Xinyi Lu\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "nbgrader": {
     "grade": false,
     "solution": false
    }
   },
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "e3cd066e7cb0c61ba50126b0b2d49e23",
     "grade": false,
     "grade_id": "1",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "# Exercise 1 - Shell basics\n",
    "\n",
    "Work through as much of the Software Carpentry [lesson on the Unix Shell](http://swcarpentry.github.io/shell-novice/) as you can.  Run through the Setup section just below, then open a terminal through Jupyter to run through the exercises.\n",
    "\n",
    "After you have completed the first few sections of the tutorial, return to this notebook.  Execute all of the cells, and answer all of the questions.\n",
    "\n",
    "\n",
    "## Setup - getting required files \n",
    "\n",
    "To get started, you'll need to have the required files in your directory.  Use `wget` to get them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false,
    "deletable": false,
    "nbgrader": {
     "checksum": "8226311a7516ff4f1e6f8a40f42bc600",
     "grade": false,
     "grade_id": "2",
     "locked": true,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--2016-09-01 13:41:23--  http://swcarpentry.github.io/shell-novice/data/shell-novice-data.zip\n",
      "Resolving swcarpentry.github.io (swcarpentry.github.io)... 151.101.32.133\n",
      "Connecting to swcarpentry.github.io (swcarpentry.github.io)|151.101.32.133|:80... connected.\n",
      "HTTP request sent, awaiting response... 200 OK\n",
      "Length: 168355 (164K) [application/zip]\n",
      "Saving to: ‘shell-novice-data.zip.1’\n",
      "\n",
      "shell-novice-data.z 100%[===================>] 164.41K  --.-KB/s    in 0.1s    \n",
      "\n",
      "2016-09-01 13:41:28 (1.32 MB/s) - ‘shell-novice-data.zip.1’ saved [168355/168355]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "!wget http://swcarpentry.github.io/shell-novice/data/shell-novice-data.zip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false,
    "deletable": false,
    "nbgrader": {
     "checksum": "ae8f6d811b95bdcc1a676969401c6b73",
     "grade": false,
     "grade_id": "3",
     "locked": true,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Archive:  shell-novice-data.zip\r\n",
      "  Length      Date    Time    Name\r\n",
      "---------  ---------- -----   ----\r\n",
      "        0  2015-11-22 16:39   data-shell/\r\n",
      "      199  2015-11-22 16:39   data-shell/.bash_profile\r\n",
      "        0  2015-11-17 07:02   data-shell/creatures/\r\n",
      "     1838  2015-11-17 07:02   data-shell/creatures/basilisk.dat\r\n",
      "     1833  2015-11-17 07:02   data-shell/creatures/unicorn.dat\r\n",
      "        0  2015-11-17 07:02   data-shell/data/\r\n",
      "      283  2015-11-17 07:02   data-shell/data/amino-acids.txt\r\n",
      "      136  2015-11-17 07:02   data-shell/data/animals.txt\r\n",
      "        0  2015-11-17 07:02   data-shell/data/elements/\r\n",
      "      270  2015-11-17 07:02   data-shell/data/elements/Ac.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Ag.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/Al.xml\r\n",
      "      325  2015-11-17 07:02   data-shell/data/elements/Am.xml\r\n",
      "      307  2015-11-17 07:02   data-shell/data/elements/Ar.xml\r\n",
      "      326  2015-11-17 07:02   data-shell/data/elements/As.xml\r\n",
      "      261  2015-11-17 07:02   data-shell/data/elements/At.xml\r\n",
      "      308  2015-11-17 07:02   data-shell/data/elements/Au.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/B.xml\r\n",
      "      302  2015-11-17 07:02   data-shell/data/elements/Ba.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Be.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Bi.xml\r\n",
      "      241  2015-11-17 07:02   data-shell/data/elements/Bk.xml\r\n",
      "      321  2015-11-17 07:02   data-shell/data/elements/Br.xml\r\n",
      "      317  2015-11-17 07:02   data-shell/data/elements/C.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Ca.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Cd.xml\r\n",
      "      313  2015-11-17 07:02   data-shell/data/elements/Ce.xml\r\n",
      "      239  2015-11-17 07:02   data-shell/data/elements/Cf.xml\r\n",
      "      323  2015-11-17 07:02   data-shell/data/elements/Cl.xml\r\n",
      "      234  2015-11-17 07:02   data-shell/data/elements/Cm.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Co.xml\r\n",
      "      317  2015-11-17 07:02   data-shell/data/elements/Cr.xml\r\n",
      "      306  2015-11-17 07:02   data-shell/data/elements/Cs.xml\r\n",
      "      313  2015-11-17 07:02   data-shell/data/elements/Cu.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Dy.xml\r\n",
      "      308  2015-11-17 07:02   data-shell/data/elements/Er.xml\r\n",
      "      238  2015-11-17 07:02   data-shell/data/elements/Es.xml\r\n",
      "      315  2015-11-17 07:02   data-shell/data/elements/Eu.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/F.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Fe.xml\r\n",
      "      236  2015-11-17 07:02   data-shell/data/elements/Fm.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Fr.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Ga.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Gd.xml\r\n",
      "      319  2015-11-17 07:02   data-shell/data/elements/Ge.xml\r\n",
      "      317  2015-11-17 07:02   data-shell/data/elements/H.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/He.xml\r\n",
      "      302  2015-11-17 07:02   data-shell/data/elements/Hf.xml\r\n",
      "      310  2015-11-17 07:02   data-shell/data/elements/Hg.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Ho.xml\r\n",
      "      324  2015-11-17 07:02   data-shell/data/elements/I.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/In.xml\r\n",
      "      305  2015-11-17 07:02   data-shell/data/elements/Ir.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/K.xml\r\n",
      "      310  2015-11-17 07:02   data-shell/data/elements/Kr.xml\r\n",
      "      271  2015-11-17 07:02   data-shell/data/elements/La.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Li.xml\r\n",
      "      237  2015-11-17 07:02   data-shell/data/elements/Lr.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Lu.xml\r\n",
      "      237  2015-11-17 07:02   data-shell/data/elements/Md.xml\r\n",
      "      310  2015-11-17 07:02   data-shell/data/elements/Mg.xml\r\n",
      "      322  2015-11-17 07:02   data-shell/data/elements/Mn.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Mo.xml\r\n",
      "      333  2015-11-17 07:02   data-shell/data/elements/N.xml\r\n",
      "      315  2015-11-17 07:02   data-shell/data/elements/Na.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/Nb.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Nd.xml\r\n",
      "      308  2015-11-17 07:02   data-shell/data/elements/Ne.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Ni.xml\r\n",
      "      241  2015-11-17 07:02   data-shell/data/elements/No.xml\r\n",
      "      323  2015-11-17 07:02   data-shell/data/elements/Np.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/O.xml\r\n",
      "      304  2015-11-17 07:02   data-shell/data/elements/Os.xml\r\n",
      "      325  2015-11-17 07:02   data-shell/data/elements/P.xml\r\n",
      "      321  2015-11-17 07:02   data-shell/data/elements/Pa.xml\r\n",
      "      303  2015-11-17 07:02   data-shell/data/elements/Pb.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/Pd.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/Pm.xml\r\n",
      "      307  2015-11-17 07:02   data-shell/data/elements/Po.xml\r\n",
      "      317  2015-11-17 07:02   data-shell/data/elements/Pr.xml\r\n",
      "      306  2015-11-17 07:02   data-shell/data/elements/Pt.xml\r\n",
      "      324  2015-11-17 07:02   data-shell/data/elements/Pu.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Ra.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Rb.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Re.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Rh.xml\r\n",
      "      299  2015-11-17 07:02   data-shell/data/elements/Rn.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Ru.xml\r\n",
      "      318  2015-11-17 07:02   data-shell/data/elements/S.xml\r\n",
      "      322  2015-11-17 07:02   data-shell/data/elements/Sb.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Sc.xml\r\n",
      "      318  2015-11-17 07:02   data-shell/data/elements/Se.xml\r\n",
      "      320  2015-11-17 07:02   data-shell/data/elements/Si.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/Sm.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Sn.xml\r\n",
      "      310  2015-11-17 07:02   data-shell/data/elements/Sr.xml\r\n",
      "      305  2015-11-17 07:02   data-shell/data/elements/Ta.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Tb.xml\r\n",
      "      319  2015-11-17 07:02   data-shell/data/elements/Tc.xml\r\n",
      "      321  2015-11-17 07:02   data-shell/data/elements/Te.xml\r\n",
      "      314  2015-11-17 07:02   data-shell/data/elements/Th.xml\r\n",
      "      315  2015-11-17 07:02   data-shell/data/elements/Ti.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Tl.xml\r\n",
      "      312  2015-11-17 07:02   data-shell/data/elements/Tm.xml\r\n",
      "      324  2015-11-17 07:02   data-shell/data/elements/U.xml\r\n",
      "      319  2015-11-17 07:02   data-shell/data/elements/V.xml\r\n",
      "      302  2015-11-17 07:02   data-shell/data/elements/W.xml\r\n",
      "      309  2015-11-17 07:02   data-shell/data/elements/Xe.xml\r\n",
      "      310  2015-11-17 07:02   data-shell/data/elements/Y.xml\r\n",
      "      315  2015-11-17 07:02   data-shell/data/elements/Yb.xml\r\n",
      "      307  2015-11-17 07:02   data-shell/data/elements/Zn.xml\r\n",
      "      311  2015-11-17 07:02   data-shell/data/elements/Zr.xml\r\n",
      "      554  2015-11-17 07:02   data-shell/data/morse.txt\r\n",
      "        0  2015-11-17 07:02   data-shell/data/pdb/\r\n",
      "     1516  2015-11-17 07:02   data-shell/data/pdb/aldrin.pdb\r\n",
      "      306  2015-11-17 07:02   data-shell/data/pdb/ammonia.pdb\r\n",
      "     1444  2015-11-17 07:02   data-shell/data/pdb/ascorbic-acid.pdb\r\n",
      "     1030  2015-11-17 07:02   data-shell/data/pdb/benzaldehyde.pdb\r\n",
      "     1830  2015-11-17 07:02   data-shell/data/pdb/camphene.pdb\r\n",
      "     5049  2015-11-17 07:02   data-shell/data/pdb/cholesterol.pdb\r\n",
      "     1090  2015-11-17 07:02   data-shell/data/pdb/cinnamaldehyde.pdb\r\n",
      "     1694  2015-11-17 07:02   data-shell/data/pdb/citronellal.pdb\r\n",
      "     2452  2015-11-17 07:02   data-shell/data/pdb/codeine.pdb\r\n",
      "     1158  2015-11-17 07:02   data-shell/data/pdb/cubane.pdb\r\n",
      "      895  2015-11-17 07:02   data-shell/data/pdb/cyclobutane.pdb\r\n",
      "     1384  2015-11-17 07:02   data-shell/data/pdb/cyclohexanol.pdb\r\n",
      "      695  2015-11-17 07:02   data-shell/data/pdb/cyclopropane.pdb\r\n",
      "      622  2015-11-17 07:02   data-shell/data/pdb/ethane.pdb\r\n",
      "      691  2015-11-17 07:02   data-shell/data/pdb/ethanol.pdb\r\n",
      "     2396  2015-11-17 07:02   data-shell/data/pdb/ethylcyclohexane.pdb\r\n",
      "      765  2015-11-17 07:02   data-shell/data/pdb/glycol.pdb\r\n",
      "     4209  2015-11-17 07:02   data-shell/data/pdb/heme.pdb\r\n",
      "     1064  2015-11-17 07:02   data-shell/data/pdb/lactic-acid.pdb\r\n",
      "     2562  2015-11-17 07:02   data-shell/data/pdb/lactose.pdb\r\n",
      "    11193  2015-11-17 07:02   data-shell/data/pdb/lanoxin.pdb\r\n",
      "     3395  2015-11-17 07:02   data-shell/data/pdb/lsd.pdb\r\n",
      "     2562  2015-11-17 07:02   data-shell/data/pdb/maltose.pdb\r\n",
      "     2164  2015-11-17 07:02   data-shell/data/pdb/menthol.pdb\r\n",
      "      422  2015-11-17 07:02   data-shell/data/pdb/methane.pdb\r\n",
      "      490  2015-11-17 07:02   data-shell/data/pdb/methanol.pdb\r\n",
      "     1869  2015-11-17 07:02   data-shell/data/pdb/mint.pdb\r\n",
      "     2288  2015-11-17 07:02   data-shell/data/pdb/morphine.pdb\r\n",
      "     2123  2015-11-17 07:02   data-shell/data/pdb/mustard.pdb\r\n",
      "     1680  2015-11-17 07:02   data-shell/data/pdb/nerol.pdb\r\n",
      "     2729  2015-11-17 07:02   data-shell/data/pdb/norethindrone.pdb\r\n",
      "     1828  2015-11-17 07:02   data-shell/data/pdb/octane.pdb\r\n",
      "     1226  2015-11-17 07:02   data-shell/data/pdb/pentane.pdb\r\n",
      "     2287  2015-11-17 07:02   data-shell/data/pdb/piperine.pdb\r\n",
      "      825  2015-11-17 07:02   data-shell/data/pdb/propane.pdb\r\n",
      "     1256  2015-11-17 07:02   data-shell/data/pdb/pyridoxal.pdb\r\n",
      "     3303  2015-11-17 07:02   data-shell/data/pdb/quinine.pdb\r\n",
      "     2675  2015-11-17 07:02   data-shell/data/pdb/strychnine.pdb\r\n",
      "     1159  2015-11-17 07:02   data-shell/data/pdb/styrene.pdb\r\n",
      "     2562  2015-11-17 07:02   data-shell/data/pdb/sucrose.pdb\r\n",
      "     2787  2015-11-17 07:02   data-shell/data/pdb/testosterone.pdb\r\n",
      "     2196  2015-11-17 07:02   data-shell/data/pdb/thiamine.pdb\r\n",
      "     1508  2015-11-17 07:02   data-shell/data/pdb/tnt.pdb\r\n",
      "     2395  2015-11-17 07:02   data-shell/data/pdb/tuberin.pdb\r\n",
      "     2103  2015-11-17 07:02   data-shell/data/pdb/tyrian-purple.pdb\r\n",
      "     1361  2015-11-17 07:02   data-shell/data/pdb/vanillin.pdb\r\n",
      "      423  2015-11-17 07:02   data-shell/data/pdb/vinyl-chloride.pdb\r\n",
      "     2894  2015-11-17 07:02   data-shell/data/pdb/vitamin-a.pdb\r\n",
      "     8898  2015-11-17 07:02   data-shell/data/planets.txt\r\n",
      "       45  2015-11-17 07:02   data-shell/data/salmon.txt\r\n",
      "    73861  2015-11-17 07:02   data-shell/data/sunspot.txt\r\n",
      "        0  2015-11-17 07:02   data-shell/Desktop/\r\n",
      "        0  2015-11-17 07:02   data-shell/Desktop/.gitkeep\r\n",
      "        0  2015-11-17 07:02   data-shell/molecules/\r\n",
      "     1158  2015-11-17 07:02   data-shell/molecules/cubane.pdb\r\n",
      "      622  2015-11-17 07:02   data-shell/molecules/ethane.pdb\r\n",
      "      422  2015-11-17 07:02   data-shell/molecules/methane.pdb\r\n",
      "     1828  2015-11-17 07:02   data-shell/molecules/octane.pdb\r\n",
      "     1226  2015-11-17 07:02   data-shell/molecules/pentane.pdb\r\n",
      "      825  2015-11-17 07:02   data-shell/molecules/propane.pdb\r\n",
      "        0  2015-11-17 07:02   data-shell/north-pacific-gyre/\r\n",
      "        0  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/\r\n",
      "      184  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/goodiff\r\n",
      "      198  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/goostats\r\n",
      "     4406  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01729A.txt\r\n",
      "     4400  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01729B.txt\r\n",
      "     4371  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01736A.txt\r\n",
      "     4411  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01751A.txt\r\n",
      "     4409  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01751B.txt\r\n",
      "     4401  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01812A.txt\r\n",
      "     4395  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01843A.txt\r\n",
      "     4375  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01843B.txt\r\n",
      "     4372  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01971Z.txt\r\n",
      "     4381  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01978A.txt\r\n",
      "     4389  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE01978B.txt\r\n",
      "     3517  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE02018B.txt\r\n",
      "     4391  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE02040A.txt\r\n",
      "     4367  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE02040B.txt\r\n",
      "     4381  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE02040Z.txt\r\n",
      "     4386  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE02043A.txt\r\n",
      "     4393  2015-11-17 07:02   data-shell/north-pacific-gyre/2012-07-03/NENE02043B.txt\r\n",
      "       86  2015-11-17 07:02   data-shell/notes.txt\r\n",
      "       32  2015-11-17 07:02   data-shell/pizza.cfg\r\n",
      "    21583  2015-11-17 07:02   data-shell/solar.pdf\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/data/\r\n",
      "     3962  2015-11-17 07:02   data-shell/writing/data/one.txt\r\n",
      "    18034  2015-11-17 07:02   data-shell/writing/data/two.txt\r\n",
      "      218  2015-11-17 07:02   data-shell/writing/haiku.txt\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/old/\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/old/.gitkeep\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/thesis/\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/thesis/empty-draft.md\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/tools/\r\n",
      "       31  2015-11-17 07:02   data-shell/writing/tools/format\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/tools/old/\r\n",
      "        0  2015-11-17 07:02   data-shell/writing/tools/old/oldtool\r\n",
      "       26  2015-11-17 07:02   data-shell/writing/tools/stats\r\n",
      "---------                     -------\r\n",
      "   339880                     212 files\r\n"
     ]
    }
   ],
   "source": [
    "!unzip -l shell-novice-data.zip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "deletable": false,
    "nbgrader": {
     "checksum": "4d1a9ad9353f087a9492105c292e77f0",
     "grade": false,
     "grade_id": "4",
     "locked": true,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Archive:  shell-novice-data.zip\n",
      "   creating: data-shell/\n",
      "  inflating: data-shell/.bash_profile  \n",
      "   creating: data-shell/creatures/\n",
      "  inflating: data-shell/creatures/basilisk.dat  \n",
      "  inflating: data-shell/creatures/unicorn.dat  \n",
      "   creating: data-shell/data/\n",
      "  inflating: data-shell/data/amino-acids.txt  \n",
      "  inflating: data-shell/data/animals.txt  \n",
      "   creating: data-shell/data/elements/\n",
      "  inflating: data-shell/data/elements/Ac.xml  \n",
      "  inflating: data-shell/data/elements/Ag.xml  \n",
      "  inflating: data-shell/data/elements/Al.xml  \n",
      "  inflating: data-shell/data/elements/Am.xml  \n",
      "  inflating: data-shell/data/elements/Ar.xml  \n",
      "  inflating: data-shell/data/elements/As.xml  \n",
      "  inflating: data-shell/data/elements/At.xml  \n",
      "  inflating: data-shell/data/elements/Au.xml  \n",
      "  inflating: data-shell/data/elements/B.xml  \n",
      "  inflating: data-shell/data/elements/Ba.xml  \n",
      "  inflating: data-shell/data/elements/Be.xml  \n",
      "  inflating: data-shell/data/elements/Bi.xml  \n",
      "  inflating: data-shell/data/elements/Bk.xml  \n",
      "  inflating: data-shell/data/elements/Br.xml  \n",
      "  inflating: data-shell/data/elements/C.xml  \n",
      "  inflating: data-shell/data/elements/Ca.xml  \n",
      "  inflating: data-shell/data/elements/Cd.xml  \n",
      "  inflating: data-shell/data/elements/Ce.xml  \n",
      "  inflating: data-shell/data/elements/Cf.xml  \n",
      "  inflating: data-shell/data/elements/Cl.xml  \n",
      "  inflating: data-shell/data/elements/Cm.xml  \n",
      "  inflating: data-shell/data/elements/Co.xml  \n",
      "  inflating: data-shell/data/elements/Cr.xml  \n",
      "  inflating: data-shell/data/elements/Cs.xml  \n",
      "  inflating: data-shell/data/elements/Cu.xml  \n",
      "  inflating: data-shell/data/elements/Dy.xml  \n",
      "  inflating: data-shell/data/elements/Er.xml  \n",
      "  inflating: data-shell/data/elements/Es.xml  \n",
      "  inflating: data-shell/data/elements/Eu.xml  \n",
      "  inflating: data-shell/data/elements/F.xml  \n",
      "  inflating: data-shell/data/elements/Fe.xml  \n",
      "  inflating: data-shell/data/elements/Fm.xml  \n",
      "  inflating: data-shell/data/elements/Fr.xml  \n",
      "  inflating: data-shell/data/elements/Ga.xml  \n",
      "  inflating: data-shell/data/elements/Gd.xml  \n",
      "  inflating: data-shell/data/elements/Ge.xml  \n",
      "  inflating: data-shell/data/elements/H.xml  \n",
      "  inflating: data-shell/data/elements/He.xml  \n",
      "  inflating: data-shell/data/elements/Hf.xml  \n",
      "  inflating: data-shell/data/elements/Hg.xml  \n",
      "  inflating: data-shell/data/elements/Ho.xml  \n",
      "  inflating: data-shell/data/elements/I.xml  \n",
      "  inflating: data-shell/data/elements/In.xml  \n",
      "  inflating: data-shell/data/elements/Ir.xml  \n",
      "  inflating: data-shell/data/elements/K.xml  \n",
      "  inflating: data-shell/data/elements/Kr.xml  \n",
      "  inflating: data-shell/data/elements/La.xml  \n",
      "  inflating: data-shell/data/elements/Li.xml  \n",
      "  inflating: data-shell/data/elements/Lr.xml  \n",
      "  inflating: data-shell/data/elements/Lu.xml  \n",
      "  inflating: data-shell/data/elements/Md.xml  \n",
      "  inflating: data-shell/data/elements/Mg.xml  \n",
      "  inflating: data-shell/data/elements/Mn.xml  \n",
      "  inflating: data-shell/data/elements/Mo.xml  \n",
      "  inflating: data-shell/data/elements/N.xml  \n",
      "  inflating: data-shell/data/elements/Na.xml  \n",
      "  inflating: data-shell/data/elements/Nb.xml  \n",
      "  inflating: data-shell/data/elements/Nd.xml  \n",
      "  inflating: data-shell/data/elements/Ne.xml  \n",
      "  inflating: data-shell/data/elements/Ni.xml  \n",
      "  inflating: data-shell/data/elements/No.xml  \n",
      "  inflating: data-shell/data/elements/Np.xml  \n",
      "  inflating: data-shell/data/elements/O.xml  \n",
      "  inflating: data-shell/data/elements/Os.xml  \n",
      "  inflating: data-shell/data/elements/P.xml  \n",
      "  inflating: data-shell/data/elements/Pa.xml  \n",
      "  inflating: data-shell/data/elements/Pb.xml  \n",
      "  inflating: data-shell/data/elements/Pd.xml  \n",
      "  inflating: data-shell/data/elements/Pm.xml  \n",
      "  inflating: data-shell/data/elements/Po.xml  \n",
      "  inflating: data-shell/data/elements/Pr.xml  \n",
      "  inflating: data-shell/data/elements/Pt.xml  \n",
      "  inflating: data-shell/data/elements/Pu.xml  \n",
      "  inflating: data-shell/data/elements/Ra.xml  \n",
      "  inflating: data-shell/data/elements/Rb.xml  \n",
      "  inflating: data-shell/data/elements/Re.xml  \n",
      "  inflating: data-shell/data/elements/Rh.xml  \n",
      "  inflating: data-shell/data/elements/Rn.xml  \n",
      "  inflating: data-shell/data/elements/Ru.xml  \n",
      "  inflating: data-shell/data/elements/S.xml  \n",
      "  inflating: data-shell/data/elements/Sb.xml  \n",
      "  inflating: data-shell/data/elements/Sc.xml  \n",
      "  inflating: data-shell/data/elements/Se.xml  \n",
      "  inflating: data-shell/data/elements/Si.xml  \n",
      "  inflating: data-shell/data/elements/Sm.xml  \n",
      "  inflating: data-shell/data/elements/Sn.xml  \n",
      "  inflating: data-shell/data/elements/Sr.xml  \n",
      "  inflating: data-shell/data/elements/Ta.xml  \n",
      "  inflating: data-shell/data/elements/Tb.xml  \n",
      "  inflating: data-shell/data/elements/Tc.xml  \n",
      "  inflating: data-shell/data/elements/Te.xml  \n",
      "  inflating: data-shell/data/elements/Th.xml  \n",
      "  inflating: data-shell/data/elements/Ti.xml  \n",
      "  inflating: data-shell/data/elements/Tl.xml  \n",
      "  inflating: data-shell/data/elements/Tm.xml  \n",
      "  inflating: data-shell/data/elements/U.xml  \n",
      "  inflating: data-shell/data/elements/V.xml  \n",
      "  inflating: data-shell/data/elements/W.xml  \n",
      "  inflating: data-shell/data/elements/Xe.xml  \n",
      "  inflating: data-shell/data/elements/Y.xml  \n",
      "  inflating: data-shell/data/elements/Yb.xml  \n",
      "  inflating: data-shell/data/elements/Zn.xml  \n",
      "  inflating: data-shell/data/elements/Zr.xml  \n",
      "  inflating: data-shell/data/morse.txt  \n",
      "   creating: data-shell/data/pdb/\n",
      "  inflating: data-shell/data/pdb/aldrin.pdb  \n",
      "  inflating: data-shell/data/pdb/ammonia.pdb  \n",
      "  inflating: data-shell/data/pdb/ascorbic-acid.pdb  \n",
      "  inflating: data-shell/data/pdb/benzaldehyde.pdb  \n",
      "  inflating: data-shell/data/pdb/camphene.pdb  \n",
      "  inflating: data-shell/data/pdb/cholesterol.pdb  \n",
      "  inflating: data-shell/data/pdb/cinnamaldehyde.pdb  \n",
      "  inflating: data-shell/data/pdb/citronellal.pdb  \n",
      "  inflating: data-shell/data/pdb/codeine.pdb  \n",
      "  inflating: data-shell/data/pdb/cubane.pdb  \n",
      "  inflating: data-shell/data/pdb/cyclobutane.pdb  \n",
      "  inflating: data-shell/data/pdb/cyclohexanol.pdb  \n",
      "  inflating: data-shell/data/pdb/cyclopropane.pdb  \n",
      "  inflating: data-shell/data/pdb/ethane.pdb  \n",
      "  inflating: data-shell/data/pdb/ethanol.pdb  \n",
      "  inflating: data-shell/data/pdb/ethylcyclohexane.pdb  \n",
      "  inflating: data-shell/data/pdb/glycol.pdb  \n",
      "  inflating: data-shell/data/pdb/heme.pdb  \n",
      "  inflating: data-shell/data/pdb/lactic-acid.pdb  \n",
      "  inflating: data-shell/data/pdb/lactose.pdb  \n",
      "  inflating: data-shell/data/pdb/lanoxin.pdb  \n",
      "  inflating: data-shell/data/pdb/lsd.pdb  \n",
      "  inflating: data-shell/data/pdb/maltose.pdb  \n",
      "  inflating: data-shell/data/pdb/menthol.pdb  \n",
      "  inflating: data-shell/data/pdb/methane.pdb  \n",
      "  inflating: data-shell/data/pdb/methanol.pdb  \n",
      "  inflating: data-shell/data/pdb/mint.pdb  \n",
      "  inflating: data-shell/data/pdb/morphine.pdb  \n",
      "  inflating: data-shell/data/pdb/mustard.pdb  \n",
      "  inflating: data-shell/data/pdb/nerol.pdb  \n",
      "  inflating: data-shell/data/pdb/norethindrone.pdb  \n",
      "  inflating: data-shell/data/pdb/octane.pdb  \n",
      "  inflating: data-shell/data/pdb/pentane.pdb  \n",
      "  inflating: data-shell/data/pdb/piperine.pdb  \n",
      "  inflating: data-shell/data/pdb/propane.pdb  \n",
      "  inflating: data-shell/data/pdb/pyridoxal.pdb  \n",
      "  inflating: data-shell/data/pdb/quinine.pdb  \n",
      "  inflating: data-shell/data/pdb/strychnine.pdb  \n",
      "  inflating: data-shell/data/pdb/styrene.pdb  \n",
      "  inflating: data-shell/data/pdb/sucrose.pdb  \n",
      "  inflating: data-shell/data/pdb/testosterone.pdb  \n",
      "  inflating: data-shell/data/pdb/thiamine.pdb  \n",
      "  inflating: data-shell/data/pdb/tnt.pdb  \n",
      "  inflating: data-shell/data/pdb/tuberin.pdb  \n",
      "  inflating: data-shell/data/pdb/tyrian-purple.pdb  \n",
      "  inflating: data-shell/data/pdb/vanillin.pdb  \n",
      "  inflating: data-shell/data/pdb/vinyl-chloride.pdb  \n",
      "  inflating: data-shell/data/pdb/vitamin-a.pdb  \n",
      "  inflating: data-shell/data/planets.txt  \n",
      "  inflating: data-shell/data/salmon.txt  \n",
      "  inflating: data-shell/data/sunspot.txt  \n",
      "   creating: data-shell/Desktop/\n",
      " extracting: data-shell/Desktop/.gitkeep  \n",
      "   creating: data-shell/molecules/\n",
      "  inflating: data-shell/molecules/cubane.pdb  \n",
      "  inflating: data-shell/molecules/ethane.pdb  \n",
      "  inflating: data-shell/molecules/methane.pdb  \n",
      "  inflating: data-shell/molecules/octane.pdb  \n",
      "  inflating: data-shell/molecules/pentane.pdb  \n",
      "  inflating: data-shell/molecules/propane.pdb  \n",
      "   creating: data-shell/north-pacific-gyre/\n",
      "   creating: data-shell/north-pacific-gyre/2012-07-03/\n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/goodiff  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/goostats  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01729A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01729B.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01736A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01751A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01751B.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01812A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01843A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01843B.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01971Z.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01978A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE01978B.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE02018B.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE02040A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE02040B.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE02040Z.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE02043A.txt  \n",
      "  inflating: data-shell/north-pacific-gyre/2012-07-03/NENE02043B.txt  \n",
      "  inflating: data-shell/notes.txt    \n",
      "  inflating: data-shell/pizza.cfg    \n",
      "  inflating: data-shell/solar.pdf    \n",
      "   creating: data-shell/writing/\n",
      "   creating: data-shell/writing/data/\n",
      "  inflating: data-shell/writing/data/one.txt  \n",
      "  inflating: data-shell/writing/data/two.txt  \n",
      "  inflating: data-shell/writing/haiku.txt  \n",
      "   creating: data-shell/writing/old/\n",
      " extracting: data-shell/writing/old/.gitkeep  \n",
      "   creating: data-shell/writing/thesis/\n",
      " extracting: data-shell/writing/thesis/empty-draft.md  \n",
      "   creating: data-shell/writing/tools/\n",
      "  inflating: data-shell/writing/tools/format  \n",
      "   creating: data-shell/writing/tools/old/\n",
      " extracting: data-shell/writing/tools/old/oldtool  \n",
      " extracting: data-shell/writing/tools/stats  \n"
     ]
    }
   ],
   "source": [
    "!unzip shell-novice-data.zip"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "152f602792df2af81846d380bde22960",
     "grade": false,
     "grade_id": "5",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "*Note*: you only need to do this once per session while using Jupyter on datanotebook.org.  You can open a terminal now and work through the steps, and return to this notebook a little later, and the files will be available either way.  That's because you're working in the same local directory.\n",
    "\n",
    "**However**!  If you download this file, close your Jupyter session for the night, then come back tomorrow and open up a new Jupyter session on the server again, you'll need to get those sample files again.  Just execute the cells above to do it.\n",
    "\n",
    "Okay, let's get on with the exercise!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "20336e8a4415b37ddad44f9fcf537212",
     "grade": false,
     "grade_id": "6",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "## Navigating Files and Directories\n",
    "\n",
    "As you work through this section of the tutorial, complete the steps here as well, using the `!` shell escape command.  Execute each cell as you go.\n",
    "\n",
    "These steps aren't exactly the same as what's in the tutorial, where the file layout is a little different and where they're not using a notebook like we are.  That's okay.  Just consider this practice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "xingzhang\r\n"
     ]
    }
   ],
   "source": [
    "!whoami"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/home/xingzhang/Downloads\r\n"
     ]
    }
   ],
   "source": [
    "!pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data(2).zip\r\n",
      "data-shell/\t\t\t shell-novice-data.zip\r\n",
      "exercise-01.ipynb\t\t shell-novice-data.zip.1\r\n",
      "rstudio-0.99.903-amd64.deb\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(1).zip\t wk-01-b-Fall 2016-basic Python.ipynb\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data(2).zip\r\n",
      "data-shell/\t\t\t shell-novice-data.zip\r\n",
      "exercise-01.ipynb\t\t shell-novice-data.zip.1\r\n",
      "rstudio-0.99.903-amd64.deb\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(1).zip\t wk-01-b-Fall 2016-basic Python.ipynb\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "creatures/  Desktop/\tnorth-pacific-gyre/  pizza.cfg\twriting/\r\n",
      "data/\t    molecules/\tnotes.txt\t     solar.pdf\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F data-shell/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "./\t\t\t\t shell-novice-data(1).zip\r\n",
      "../\t\t\t\t shell-novice-data(2).zip\r\n",
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data.zip\r\n",
      "data-shell/\t\t\t shell-novice-data.zip.1\r\n",
      "exercise-01.ipynb\t\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      ".ipynb_checkpoints/\t\t wk-01-b-Fall 2016-basic Python.ipynb\r\n",
      "rstudio-0.99.903-amd64.deb\r\n"
     ]
    }
   ],
   "source": [
    "!ls -aF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "data-shell\t\t\t      wk-01-b-Fall 2016-basic Python.ipynb\r\n",
      "wk-01-a-Fall 2016-basic Python.ipynb  .ipynb_checkpoints\r\n",
      "shell-novice-data(2).zip\t      shell-novice-data.zip\r\n",
      "Anaconda3-4.1.1-Linux-x86_64.sh       shell-novice-data(1).zip\r\n",
      "exercise-01.ipynb\t\t      shell-novice-data.zip.1\r\n",
      ".\t\t\t\t      rstudio-0.99.903-amd64.deb\r\n",
      "..\r\n"
     ]
    }
   ],
   "source": [
    "!ls -af ."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "68b014c6f404b0d1d947f29e2bfcc486",
     "grade": false,
     "grade_id": "17",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "source": [
    "What is the difference between the two previous cells, and what does the single dot mean?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "096f49df2f3ad787d39504949efc14c8",
     "grade": true,
     "grade_id": "156",
     "locked": false,
     "points": 1,
     "solution": true
    }
   },
   "source": [
    "\"f\" means do not sort, so it does not show forward slash. Single dot \".\" means that on its own means ‘the current directory’."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "anaconda3/\t  Music/       Templates/\r\n",
      "Desktop/\t  numbers.txt  Untitled.ipynb\r\n",
      "Documents/\t  Pictures/    Videos/\r\n",
      "Downloads/\t  Public/      wk-01-b-Fall 2016-basic Python.ipynb\r\n",
      "examples.desktop  R/\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F .."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "7edc7fa8b245f34a03ead3d212893148",
     "grade": false,
     "grade_id": "18",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "source": [
    "What do the double dots mean?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "aa03dc1d4946820269aa3232690a8098",
     "grade": true,
     "grade_id": "155",
     "locked": false,
     "points": 1,
     "solution": true
    }
   },
   "source": [
    "’..’ means ‘the directory above the current one’;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "goodiff\t\tNENE01736A.txt\tNENE01843A.txt\tNENE01978B.txt\tNENE02040Z.txt\r\n",
      "goostats\tNENE01751A.txt\tNENE01843B.txt\tNENE02018B.txt\tNENE02043A.txt\r\n",
      "NENE01729A.txt\tNENE01751B.txt\tNENE01971Z.txt\tNENE02040A.txt\tNENE02043B.txt\r\n",
      "NENE01729B.txt\tNENE01812A.txt\tNENE01978A.txt\tNENE02040B.txt\r\n"
     ]
    }
   ],
   "source": [
    "!ls data-shell/north-pacific-gyre/2012-07-03/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "73813310a319b6fb2eaa47fd2e446113",
     "grade": false,
     "grade_id": "20",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "## Working with Files and Directories\n",
    "\n",
    "The following cells come from the next section of the tutorial."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data.zip\r\n",
      "data-shell/\t\t\t shell-novice-data.zip.1\r\n",
      "exercise-01.ipynb\t\t thesis/\r\n",
      "rstudio-0.99.903-amd64.deb\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(1).zip\t wk-01-b-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(2).zip\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mkdir: cannot create directory ‘thesis’: File exists\r\n"
     ]
    }
   ],
   "source": [
    "!mkdir thesis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": false,
    "deletable": false,
    "nbgrader": {
     "checksum": "d3b4bcc7173216067e71713971f56458",
     "grade": true,
     "grade_id": "121",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "import os\n",
    "assert \"thesis\" in os.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data.zip\r\n",
      "data-shell/\t\t\t shell-novice-data.zip.1\r\n",
      "exercise-01.ipynb\t\t thesis/\r\n",
      "rstudio-0.99.903-amd64.deb\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(1).zip\t wk-01-b-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(2).zip\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "066e9eefabbb9850efbaf78568d53cc1",
     "grade": false,
     "grade_id": "12",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "You can't use the nano editor here in Jupyter, so we'll use the `touch` command to create an empty file instead."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "!touch thesis/draft.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false,
    "deletable": false,
    "nbgrader": {
     "checksum": "fa8505bfc9fef49d61b9d88bd67c8ac8",
     "grade": true,
     "grade_id": "123",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "assert \"draft.txt\" in os.listdir(\"thesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "draft.txt\r\n"
     ]
    }
   ],
   "source": [
    "!ls -F thesis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "44efd4ee4fa259cb189e7d8755761bdd",
     "grade": false,
     "grade_id": "33",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "Removing files and directories."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "!rm thesis/draft.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "collapsed": true,
    "deletable": false,
    "nbgrader": {
     "checksum": "764dbb17e55a063f3a9414ce228ffee5",
     "grade": true,
     "grade_id": "125",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "assert \"draft.txt\" not in os.listdir(\"thesis\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "rm: cannot remove 'thesis': Is a directory\r\n"
     ]
    }
   ],
   "source": [
    "!rm thesis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "collapsed": true,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "!rmdir thesis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "collapsed": true,
    "deletable": false,
    "nbgrader": {
     "checksum": "afcbc0f82ee2883500630687cc14828f",
     "grade": true,
     "grade_id": "127",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "assert \"thesis\" not in os.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data(2).zip\r\n",
      "data-shell\t\t\t shell-novice-data.zip\r\n",
      "exercise-01.ipynb\t\t shell-novice-data.zip.1\r\n",
      "rstudio-0.99.903-amd64.deb\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(1).zip\t wk-01-b-Fall 2016-basic Python.ipynb\r\n"
     ]
    }
   ],
   "source": [
    "!ls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "deletable": false,
    "nbgrader": {
     "checksum": "87b89212f52afe53f74d19db0641c135",
     "grade": false,
     "grade_id": "32",
     "locked": true,
     "solution": false
    }
   },
   "source": [
    "Renaming and copying files."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": true,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "!touch draft.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": true,
    "deletable": false,
    "nbgrader": {
     "checksum": "1c7350af16e1e0bf1b73f739c590daea",
     "grade": true,
     "grade_id": "129",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "assert \"draft.txt\" in os.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": true,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "!mv draft.txt quotes.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": true,
    "deletable": false,
    "nbgrader": {
     "checksum": "acc883d214907d655164e9eaf1da7ee7",
     "grade": true,
     "grade_id": "130",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "assert \"quotes.txt\" in os.listdir()\n",
    "assert \"draft.txt\" not in os.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Anaconda3-4.1.1-Linux-x86_64.sh  shell-novice-data(2).zip\r\n",
      "data-shell\t\t\t shell-novice-data.zip\r\n",
      "exercise-01.ipynb\t\t shell-novice-data.zip.1\r\n",
      "quotes.txt\t\t\t wk-01-a-Fall 2016-basic Python.ipynb\r\n",
      "rstudio-0.99.903-amd64.deb\t wk-01-b-Fall 2016-basic Python.ipynb\r\n",
      "shell-novice-data(1).zip\r\n"
     ]
    }
   ],
   "source": [
    "!ls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": true,
    "nbgrader": {
     "grade": false,
     "locked": false,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "!cp quotes.txt quotations.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": true,
    "deletable": false,
    "nbgrader": {
     "checksum": "d695bea6d61e9647e20623f2257770c4",
     "grade": true,
     "grade_id": "134",
     "locked": true,
     "points": 1,
     "solution": false
    }
   },
   "outputs": [],
   "source": [
    "assert \"quotes.txt\" in os.listdir()\n",
    "assert \"quotations.txt\" in os.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
