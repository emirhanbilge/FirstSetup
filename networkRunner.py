
import subprocess


def exec():
    bashCommand = "chmod u+x manageNetwork.sh" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


def sendNetwork(ip , subnetMask , gateway ):

    exec()
    bashCommand = "sudo ./manageNetwork.sh" +  ip +" "+ subnetMask +" "+ gateway
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def writedhcp():
    exec()
    bashCommand = "sudo ./manageNetwork.sh" 
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
