
import subprocess


def resetnetwork():
    #######################################
    bashCommand = "cd /home/pi/Desktop/EbbScripts/Network/ && sudo ./resetNetwork.sh" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    ####################################


def startTrigerModbus():
    bashCommand = "cd /home/pi/Desktop/EbbScripts/Network/ && sudo ./modbusCrontabCreate.sh "
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
def sendNetwork(ip , subnetMask , gateway ):

    resetnetwork()
    bashCommand = "chmod u+x netSet.sh" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print("Error code " , error)
    bashCommand = "sudo ./netSet.sh" +  ip +" "+ subnetMask +" "+ gateway
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    startTrigerModbus()

def writedhcp():
    resetnetwork() 
    startTrigerModbus()
