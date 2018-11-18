#! /bin/python
import psutil
import platform
import sys




def getSocketInfo(pid):
	procName = psutil.Process(pid).name()
	procExe = psutil.Process(pid).exe()
	procPpid = psutil.Process(pid).ppid()
	procCmd = psutil.Process(pid).cmdline()
	procUser = psutil.Process(pid).username()

	# Check info for parent process
	PprocName = psutil.Process(procPpid).name()
	PprocExe = psutil.Process(procPpid).exe()
	PprocCmd = psutil.Process(procPpid).cmdline()
	return "[*] Process Id: {} \n *******************************************************************************\n Process Name:{} \n Process User: {} \n   Process Exe :{} \n Process cmdline: {} \n Parent Process Id :{} \n Parent Process Name: {} \n Parent Process Exe: {} \n Parent Process Cmdline: {} \n \n ".format(pid, procName, procUser, procExe, procCmd, procPpid, PprocName, PprocExe, PprocCmd)



print "System info: \n [!] Computer Name:{} \n[!] System OS:{} \n [!] System Version:{}  \n [!] Python Version: {} \n".format(platform.node(), platform.system(), platform.version(), platform.python_version())
print "******************************************************************************"

#if sys.argv[1] = "details":
for netCon in psutil.net_connections():
	pid = netCon.pid

	print getSocketInfo(pid)


