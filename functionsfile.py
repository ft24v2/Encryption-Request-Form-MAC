## This is the File which will contain all of the messy code and functions
import socket, platform, sys, os, datetime
import subprocess
from subprocess import Popen, PIPE

# System Information Stuff:

#====> Hostname

hostname = str(platform.node())

#====> OS Version
def osversion():

    proc = subprocess.Popen('sw_vers', shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    line = output   
      
    osver = line[38:45]

    osversionresult = "OSX {}".format(osver)
    osresults=str.join(" ", osversionresult.splitlines())
    return osresults


#====> User Name
username = "USERNAME"

# Model Number
def modelnumber():

    proc = subprocess.Popen('sysctl hw.model', shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    line = output   
      
    model = line[9:50]

    modelnumber = str.join(" ", model.splitlines())
    return modelnumber

#====> Serial Number
def serialnumber():

    proc = subprocess.Popen("system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'", shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    line = output   

    serialnumber = str.join(" ", output.splitlines())
    return serialnumber

#====> Free Space
def freespace():
    s = os.statvfs('/')
    freespace = (s.f_bavail * s.f_frsize) / 1024 / 1024 /1024
    freespaceresultval = freespace
    return ("{} GB'S ".format(str(freespaceresultval))) 
    

#===> Smart 
def smart():

    proc = subprocess.Popen("system_profiler SPStorageDataType | awk '/S.M.A.R.T/ {print $3}'", shell=True, stdout=subprocess.PIPE)
    output = proc.communicate()[0]
    line = output[0:9]   

    #smartresult = str.join(" ", output.splitlines())
    smartresult = str(line)
    return smartresult
#===> Model Number via SYSTEMINFO CMD


#===> Current Date
now = datetime.datetime.now()
currentdate = str(now)
