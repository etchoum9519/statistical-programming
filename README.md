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

# Visualization on Jupiter Lab (Basis = 2, Number of intervals = 12)
### A - Subprocessing the programm and giving the output an adequate form

<p >
<img width="800" height="250"  src="https://github.com/etchoum9519/statistical-programming/assets/157910011/bb36c7b6-3a78-40f0-b007-a1fada923fa3"  /> 
</p>

### B - (L) Visualizing frequences and correlations between partitions, (R) Time-Frequency plots per partitions (last steps describe the means)

<p >
<img width="350" height="250" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/0fa9262a-d70e-4c35-9c4d-7922f0d78c26"  />        <img width="350" height="250" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/ea10a355-1071-41b2-ae25-a2671b8016b6"  />
</p>





### C - Conditional-Variance-Analysis

<p >
<img src="https://github.com/etchoum9519/statistical-programming/assets/157910011/be62ea34-025b-4044-8add-fb8ac9d950bd"/>
 </p>



### D - Connectivity map (CMAP) to visualize large-scale perturbation databases (i.e Loss-function)

<p >
<img width="450" height="350" src="https://github.com/etchoum9519/statistical-programming/assets/157910011/1205c8d5-4b58-4f0e-9a60-519d4d13f744"  />
</p>

<br>

# Links
<br>

* GWDG: ["https://gwdg.de/about-us/gwdg-news/2021/GN_10-11-2021_www.pdf#page=21"]
* GPU-Computing with Python: [https://hps.vi4io.org/teaching/summer_term_2023/scap]
* The Guide i used: [pep8 style guide](https://www.python.org/dev/peps/pep-0008/)
* Lecture for Business applications: [PyEcon](https://pyecon.org/lecture/)
