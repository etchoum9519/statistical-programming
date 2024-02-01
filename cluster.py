#!/usr/bin/env python
import argparse
import subprocess
from tabulate import tabulate
import time
#  print Time/Day/Hour
d2= time.strftime ("%B %d, %Y %H:%M")
print('|{}: \n'.format(d2))


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
    print('test_list:', ' ', test_list, '\n')
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


#################################################################
#  Part III : PARSING average waiting times with the CLI        #
#################################################################
test_list=["slurm_output0","slurm_output1","slurm_output2",
           "slurm_output3","slurm_output4","slurm_output5"]
partition_list=initialize()[0]
################################################################
#  define parser
parser = argparse.ArgumentParser(
            prog='cluster.py',
            usage='%(prog)s [options]',
            description='Calculate processing-times on a cluster'
            'with GPU/CPU based on selected'
            ' partition(s) in CPUh and GBh')
#  define parser arguments
parser.add_argument(
            '-it',
            '--init',
            nargs=1,
            help='Set basis and number of intervals to take'
            ' into account: Choices = "int","int"')
parser.add_argument(
            '-p',
            '--partition',
            nargs=1,
            help=f'Display walltimes based on number of CPU'
            ': Choices =' + f'{partition_list}')
parser.add_argument(
            '-m',
            '--mem',
            action='store_true',
            help=f'Display walltimes based on required GPU'
            ' memory')
parser.add_argument( 
            '-t',
            '--test',
            nargs=1,
            help=f'Display results for a selected slurm_output')
#            ':' + f' Choices = {test_list}')
args = parser.parse_args()

######################################################### L1 ##
#  call introducing functions yet
if args.init:
    if len(args.init[0].split(',')) <1:
        print('No initialization parameter given; the will be'
              ' selected automatically')
        b,n,on_c=4,7,'No'
    if len(args.init[0].split(',')) ==1:
        b,n,on_c=int(rgs.init[0].split(',')[0]),7,'No'
    if len(args.init[0].split(',')) ==2:
        b,n,on_c=int(args.init[0].split(',')[0]),int(
                 args.init[0].split(',')[1]),'No'
    if len(args.init[0].split(',')) >=3:
        b,n,on_c=int(args.init[0].split(',')[0]),int(
                 args.init[0].split(
                 ',')[1]),args.init[0].split(',')[1]
    init = initialize(basis_pot= b,
               nb_int= n,
               on_clust= on_c)
else:
    init = initialize()
partition_list,interval_cpu,interval_mem = (init[0],
                                            init[1],
                                            init[2])
minGB_head,minCPU_head = init[3],init[4]
test_list=["slurm_output0","slurm_output1","slurm_output2",
           "slurm_output3","slurm_output4","slurm_output5"]
######################################################### L2 ##

if args.test:
    pfads = [
      '../gpu_com_with_pyth/Data/slurm_outputs/slurm_output0',
      '../gpu_com_with_pyth/Data/slurm_outputs/slurm_output1', 
      '../gpu_com_with_pyth/Data/slurm_outputs/slurm_output2', 
      '../gpu_com_with_pyth/Data/slurm_outputs/slurm_output3', 
      '../gpu_com_with_pyth/Data/slurm_outputs/slurm_output4', 
      '../gpu_com_with_pyth/Data/slurm_outputs/slurm_output5']
    m = args.test[0].split(',')
#  make sure sacct doesn't run if command is'nt true
    for n in m:
        if n not in test_list:
            print('error - please call_sacct_for existing'
                  ' list')
            exit(1)   
    test_list = pfads[test_list.index(m[0])]
    print(test_list)
else:
    link_part1 = '../gpu_com_with_pyth/Data/slurm_outputs/'
    link_part2 = 'slurm_output0'
    test_list = link_part1 + link_part2

if args.partition:
    m = args.partition[0].split(',')
#  make sure sacct doesn't run if command is'nt true
    for n in m:
        if n not in partition_list:
            print('error - please call_sacct_for existing'
                  ' partition(s)')
            exit(1)
    partition_list = m
#  call 'sacct' only one time,
#  to limit bugs occurence in the programm itself
sacct = call_sacct(partition_list, test_list)
#  and give parser conditions
if args.mem:
    output = [minGB_head]
    for i in partition_list:
        mem = get_walltimes(get_waiting_averages(
                                 i, 'mem', sacct))
        output.append(mem)
    print(tabulate(output, headers='firstrow'))
else:
    output = [minCPU_head]
    for i in partition_list:
        cpu = get_walltimes(get_waiting_averages(
                                 i, 'cpu', sacct))
        output.append(cpu)
    print(tabulate(output, headers='firstrow'))


#################################################################
#                               END                             #
#s################################################################y on
