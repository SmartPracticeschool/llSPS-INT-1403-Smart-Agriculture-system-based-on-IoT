import time
import sys
import ibmiotf.application
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "24uoem" # repalce it with organization ID
deviceType = "Motors" #replace it with device type
deviceId = "12345" #repalce with device id
authMethod = "token"
authToken = "rH-JL-@iElw52Kp_0s"#repalce with token

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)        
        if cmd.data['command']=='motoron':
                print("MOTOR ON")
        elif cmd.data['command'] == 'motoroff':
            print("MOTOR OFF")
                
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        T=50;
        H=32;
        #Send Temperature & Humidity to IBM Watson
        data = { 'Temperature' : T, 'Humidity': H }
        #print data
        #def myOnPublishCallback():
            #print ("Published Temperature = %s C" % T, "Humidity = %s %%" % H, "to IBM Watson")

        #success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        #if not success:
            #print("Not connected to IoTF")
        time.sleep(1)
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()