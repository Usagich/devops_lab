import psutil
import datetime
import time
import configparser

config = configparser.ConfigParser()
config.read('/home/student/IdeaProjects/ss/src/conf.cfg')

class GetUtil:

    __snapshotNumber = int(config.get('common', 'initSnapNumber'))

    def __init__(self):
        ##Overall CPU load per each core in one the interval (blocking)
        self.__perCPU = str(psutil.cpu_percent(interval=1, percpu=True))
        ##Overall MB memory usage (physical memory)
        self.__physicalMemoryMB = str(int(psutil.virtual_memory().total / 1024 / 1024))
        ##Overall MB memory usage (used RAM)
        self.__usedRamMemoryMB = str(int(psutil.virtual_memory().active / 1024 / 1024))
        ##IO information
        self.__IO = str(psutil.Process().io_counters())
        ##NIC (network interface card) info
        self.__NIC = str(psutil.net_if_addrs())
        ##snapshot static counter
        self.__snapshotNumber += 1

    def getTimestamp(self):
        timeInit = time.time()
        timestamp = datetime.datetime.fromtimestamp(timeInit).strftime('%Y-%m-%d %H:%M:%S')
        return timestamp

    def getPerCPU(self):
        return ("Overall CPU load per each core in one the interval (blocking)\n" + self.__perCPU)

    def getPhysicalMemoryMB(self):
        return ("Overall MB memory usage (physical memory)\n" + self.__physicalMemoryMB)

    def getUsedRamMemoryMB(self):
        return ("Overall MB memory usage (used RAM)\n" + self.__usedRamMemoryMB)

    def getIO(self):
        return ("IO information\n" + self.__IO)

    def getNIC(self):
        return ("NIC (network interface card) info\n" + self.__NIC)

    def getSnapshotNumber(self):
        return self.__snapshotNumber


analyzer1 = GetUtil()
print("SNAPSHOT " + str(analyzer1.getSnapshotNumber()) + ": " + analyzer1.getTimestamp() + ": \n"
      + analyzer1.getPerCPU() + "\n"
      + analyzer1.getPhysicalMemoryMB() + "\n"
      + analyzer1.getUsedRamMemoryMB() + "\n"
      + analyzer1.getIO() + "\n"
      + analyzer1.getNIC())