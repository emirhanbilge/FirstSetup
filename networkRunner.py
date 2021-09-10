
import subprocess


def resetnetwork():
    #######################################
    bashCommand = "cd /home/pi/Desktop/EbbScripts/Network/" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "sudo ./resetNetwork" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    ####################################


def startTrigerModbus():
    bashCommand = "cd /home/pi/Desktop/EbbScripts/Network/" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    bashCommand = "sudo ./modbusCrontabCreate "
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
def sendNetwork(ip , subnetMask , gateway ):

    resetnetwork()
    bashCommand = "chmod u+x netSet.sh " 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("Error code " , error)
    bashCommand = "./netSet.sh" +  ip +" "+ subnetMask +" "+ gateway
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def writedhcp():
    resetnetwork() 
