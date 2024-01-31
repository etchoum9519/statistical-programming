# statistical-programming
Python-code to calculate processing-times for partitions on a GPU/CPU cluster
<br>

# Aims
  * parse `sacct` data to display the average waiting time over the last 7 days
  * data classification into bins based on partition
  * bin data by requested timelimits
    * e.g. < 5min, 5-30m, 30m-2h, 2h-12h, 12-48, 48+
  * take number of requested cores into account
    * cores * timelimit = core-time as a metric to bin data by
    * Output should be divided in more than three categories.
* Visualize this data on a web page, e.g. using flask
* Perform prediction Analysis to supply classification of processing times for ex. using:
    * Analysis of Discrete Probabilities, (based on the Number of jobs on the SSC queue)
    * Continuous Probabilities, (based on processing-time (Number of seconds needed to complete jobs)
    * Conditional Probabilities, (gpu beeing the central aim of the information)
    * PCA (Principal Component Analysis)
    * Connectivity Map (CMAP)
    * And/or oder Models
 
# Examples on Linux:

## An help can be called with parameter `--help` or '-h'

<p align="center">
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/a6c5e193-e0d4-4099-860e-f575e7e78345">
</p>

## Basic execution `cluster.py` (in CPUh)

<p align="center">
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/370c2a79-7772-4ff6-bf5b-43f70a6771cd">
</p>


## `cluster.py --mem` or `cluster.py -m` (in GPUh)

<p align="center">
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/ed97d25b-9f12-43d9-ba52-6631d732cfaf">
</p>


## `-p` or `--partition` to select partition(s) to be displayed and `-it` or `--init` to set a basis and the number of intervals to be taken into account:

<p align="center">
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/76290142-e1e5-4157-a0cd-6d2c2f5dfda1"   width="600" height="250" /> <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/cb341b40-e951-4533-8916-045e395413dd"   width="600" height="250" />
</p>


# Visualization on Jupiter Lab:

# A - 



# Links

* [pep8 style guide](https://www.python.org/dev/peps/pep-0008/)
* [PyEcon](https://pyecon.org/lecture/)
