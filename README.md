# statistical-programming
Python-code to calculate processing-times for partitions on a GPU/CPU cluster
<br><br>

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
    * Analysis of discrete probabilities, (i.e based on the Number of jobs given in brackets)
    * continuous probabilities, (i.e based on processing-time (Number of seconds, minutes, hours, days, an weeks needed to complete jobs)
    * conditional probabilities, `gpu`-partition beeing the central aim of the information i.e the target
    * Principal Component Analysis (PCA)
    * Connectivity Map (CMAP)
    * And/or oder Models.
<br>

# Examples on Linux

### An help can be called with parameter `--help` or '-h'

<p >
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/e5f9f8cf-79db-499e-9ac2-67143b168abb">
</p>

### Basic execution `cluster.py` (in CPUh)

<p >
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/79f1ea67-9d17-42eb-8419-25dc4a9e6af7">
</p>

### `cluster.py --mem` or `cluster.py -m` (in GPUh)

<p >
  <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/344776f5-fd44-4e36-9744-7ea2d514d501">
</p>


### `-p` or `--partition` to select partition(s) to be displayed and `-it` or `--init` to set a basis and the number of intervals to be taken into account:

<p >
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/276677c9-f07b-4137-93e4-65ba41e26552"  /> <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/b2ed7c7a-4b16-4405-b2b9-14ce5c4df502"  />
</p>
<br>

# Visualization on Jupiter Lab
### A - Subprocessing the programm and giving the output an adequate form

<p >
<img width="800" height="250"  src="https://github.com/etchoum9519/statistical-programming/assets/157910011/bb36c7b6-3a78-40f0-b007-a1fada923fa3"  /> 
</p>

### B - (L) Visualizing frequences and correlations between partitions, (R) Time-Frequency plots per partitions (last steps describe the means)

<p >
<img width="350" height="250" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/0fa9262a-d70e-4c35-9c4d-7922f0d78c26"  /><img width="450" height="350" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/a0019f89-b442-4e18-a71c-e98d81ec4231"  />
</p>




### C - Conditional-Variance-Analysis

<p >
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/314260e5-1603-4c59-84c7-4959355154aa"  /> <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/b2759f9f-65c2-4e6a-8309-cdc4045488e0"  />
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/1b5d82c2-3d7e-4917-86cf-058f39806d33"  /> <img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/c74781be-274e-4536-ad9b-dd1aa4ca317d"  />
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/43bf1a77-fc7b-4475-8826-a69dd629b028"  />
</p>

### D - PCA (Two componants)
<p >
<img width="400" height="200" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/d1453f84-29f8-4174-b9a5-028dfc61350b"  /> <img  width="400" height="200" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/a1c7128b-eb3a-4180-b0a3-e8ea808a0fc2"  />
</p>


### E - PCA (Three componants)
<p >
<img width="400" height="200" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/1995fafc-0279-4fc5-bb9c-8158f3da7542"  /> <img width="400" height="200" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/53b2f463-4805-4bb0-ace1-ad5a4ce9547d"  />
</p>

### F - Connectivity map (CMAP) to visualize large-scale perturbation databases (i.e the Loss-function)

<p >
<img width="450" height="350" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/1205c8d5-4b58-4f0e-9a60-519d4d13f744"  />
</p>

<br>

# Links
<br>

* GWDG: [https://gwdg.de/about-us/gwdg-news/2021/GN_10-11-2021_www.pdf]
* GPU-Computing with Python: [https://hps.vi4io.org/teaching/summer_term_2023/scap]
* The Guide i used: [pep8 style guide](https://www.python.org/dev/peps/pep-0008/)
* Lecture for Business applications: [PyEcon](https://pyecon.org/lecture/)
