# statistical-programming
Python-code to calculate processing-times for partitions on a GPU/CPU cluster
<br>

# Aims
  * parse `sacct` data to display the average processing time over the last 7 days
  * data classification into bins based on partition
  * bin data by requested timelimits
    * e.g. < 5min, 5-30m, 30m-2h, 2h-12h, 12-48, 48+
  * take number of requested cores into account
    * cores * timelimit = core-time as a metric to bin data by
    * Output should be divided in more than three categories.
* Visualize this data on a web page, e.g. using flask
* Perform prediction Analysis to supply a usefull classification for ex. using:
    * Analysis of discrete probabilities, (i.e based on the Number of jobs on the SSC queue)
    * continuous probabilities, (i.e based on processing-time (Number of seconds needed to complete jobs)
    * conditional probabilities, (i.e gpu beeing the central aim of the information)
    * Principal Component Analysis (PCA)
    * Connectivity Map (CMAP)
    * And/or oder Models.
 
# Examples on Linux:

## An help can be called with parameter `--help` or '-h'

<p align="center">
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/e5f9f8cf-79db-499e-9ac2-67143b168abb">
</p>

## Basic execution `cluster.py` (in CPUh)

<p align="center">
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/79f1ea67-9d17-42eb-8419-25dc4a9e6af7">
</p>

## `cluster.py --mem` or `cluster.py -m` (in GPUh)

<p align="center">
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/344776f5-fd44-4e36-9744-7ea2d514d501">
</p>


## `-p` or `--partition` to select partition(s) to be displayed and `-it` or `--init` to set a basis and the number of intervals to be taken into account:

<p align="center">
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/276677c9-f07b-4137-93e4-65ba41e26552"  /> <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/b2ed7c7a-4b16-4405-b2b9-14ce5c4df502"  />
</p>


# Visualization on Jupiter Lab:

# A - 



# Links

* [pep8 style guide](https://www.python.org/dev/peps/pep-0008/)
* [PyEcon](https://pyecon.org/lecture/)
