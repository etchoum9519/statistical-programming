#################################################################
#  Part I : Function for initial  Configurations                #
#################################################################
def initialize(basis_pot=4, 
               nb_int=7, 
               on_clust = 'No'):
    if on_clust != 'No':
#  First call sinfo to get a list of available partitions
#  in 'slurm' and save it in partition_list.
#  Those will help for selecting
#  partitions one would want to calculate waitingtimes for
        sinfo = subprocess.run([
                "sinfo", "-o", "%R"],
                stdout=subprocess.PIPE, shell=False)
        decode = sinfo.stdout.decode('utf-8').splitlines()
        partition_list = [i for i in decode[1:-1]]
    else:
        partition_list = ["medium", "gpu", "fat", "fat+", "int"]
#  Define set-lists that one would want to separate waitingtimes 
#  into:perform changes in head_lists to adapt time repartitions
    interval_mem = [0]
    interval_cpu = [0]
#  it is important to leave a space inbetween values and units
#  in head lists for automation reason; start at 4GBh & 3CPUh
    minGB_head = ["Partition"]
    minCPU_head = ["Partition"]
    borders = [basis_pot**k for k in range(nb_int)[1:]]
    for lis in [minGB_head, minCPU_head]:
        if lis == minGB_head:
            unit = "GBh"
        elif lis == minCPU_head:
            unit = "CPUh"
        lis.append(f"< {borders[0]} {unit}")
        for bord in range(len(borders)-1):
            lis.append(
          f"{borders[bord]} {unit} - {borders[bord+1]} {unit}")
        lis.append(f"> {borders[-1]} {unit}")
    for a, b in zip(minGB_head[1:-1], minCPU_head[1:-1]):
        interval_cpu.append(3600*int(b.split(' ')[-2]))
        interval_mem.append(3600*1024*int(a.split(' ')[-2]))
    return (partition_list,interval_cpu,interval_mem,
            minGB_head,minCPU_head)


#################################################################
#  Part II : Automation-Functions for PARSING                   #
#################################################################
#  to convert memory 'mem' (M,G or T) in MB
def get_MB_from_mem(mem):
    memory = mem[:-1]
    if 'M' in mem:
        memory = float(memory)
    elif 'G' in mem:
        memory = 1024*float(memory)
    elif 'T' in mem:
        memory = 1024**2*float(memory)
    return memory


#  to convert time format [DD-[HH:]]MM:SS in secondes
def get_seconds_from_time(time):
    tosec = [24 * 60 * 60, 60 * 60, 60, 1]
    tmp = []
    for f in time.split("-"):
        tmp += f.split(":")
    tmp = [0] * (4 - len(tmp)) + tmp
    seconds = sum([int(a)*b for a, b in zip(tmp, tosec)])
    return seconds

#  to call sacct stored data from any partition list
def call_sacct(partition_list, test_list):
    print('test_list:', ' ', test_list)
#   ['../gpu_com_with_pyth/slurm_outputs/slurm_output0']):
    dic = {i: [] for i in partition_list}
    partitions = ','.join(partition_list)

#    sacct = subprocess.run([
#            "sacct", "-a", "-X", "-T", "-p",
#            "-r", partitions, "-o",
#            "reserved, partition, ReqMem, ReqCPUS, Timelimit",
#            "-sCD,R", "-Snow-1days", "-Enow"],
#            stdout=subprocess.PIPE, shell=False)
#    decode = sacct.stdout.decode('utf-8').splitlines()[2:]
    f = open(test_list)           # Mac and Linux
    decode = f.readlines()[1:]
    for a in decode:
        line = a.split("|")
#  in case some informations should be missing
#  calculated waitingtimes have to remind trustfull
        if line[0] == '' or line[4] == 'UNLIMITED':
            continue
        a_2 = str(line[1])
        if a_2 in dic:
            a_1 = get_seconds_from_time(line[0])
            a_2 = str(line[1])
            a_3 = get_MB_from_mem(line[2])
            a_4 = int(line[3])
            a_5 = get_seconds_from_time(line[4])
#  save waiting/reservedtime(in seconds), timelimit*memory
#  (in memh),timelimit*CPUs(in CPUh),resp.in dic
            dic[a_2].append((a_1, a_5*a_3, a_5*a_4))
        else: 
            pass
    return dic


#  to display waitingtimes for any single partition, where
def get_waiting_averages(partition, param, dic):
    averages = [partition]
    if param == 'cpu':
        interval = interval_cpu
    elif param == 'mem':
        interval = interval_mem
#  'dic' is dictionary including waitingtimes for all
#  partitionslst records the waiting time for every 
# single job lt records the number of jobs
    lst = [0]*(len(interval))
    lt = [0]*(len(interval))
    for i, j, k in dic[partition]:
        if param == 'cpu':
            m = k
        elif param == 'mem':
            m = j
        for s in range(len(interval)-1):
            if interval[s] < m <= interval[s+1]:
                lst[s] = lst[s] + i
                lt[s] = lt[s] + 1
        if m > interval[-1]:
            lst[-1] = lst[-1] + i
            lt[-1] = lt[-1] + 1
#  b or 1 ensures non-zero division
    for a, b in zip(lst, lt):
        averages.append([round(a/(b or 1), 2), b])
    return averages


#  to automate the value of the output-waitingtimes
#  secondes, minutes, hours, days or weeks
def get_walltimes(averages):
    datings = [averages[0]]
    times = [0, 60, 3600, 86400, 604800]
    dates = ['s', 'm', 'h', 'd', 'w']
    var = [1, 60, 3600, 3600/24, 3600/24/7]
    for t in averages[1:]:
        if t[0] == 0:
            datings.append('NA')
        for s in range(len(times)-1):
            if times[s] < t[0] <= times[s+1]:
                date = dates[s]
                value = [round(t[0]/var[s], 1), t[1]]
                datings.append(
                 f'{value[0]} {date} ({value[1]})')
        if t[0] > times[-1]:
            datings.append(
             f'{round(t[0]/var[-1], 1)} {dates[-1]} ({t[1]})')
    return datings


