# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

import requests
import os
from datetime import datetime

lat="45.657974"
lon="25.601198"
key="3c8ed3ac65cb597f0d30d0c07259b6ff"
CONNECTION_STRING = "HostName=WeatherData.azure-devices.net;DeviceId=DataSender;SharedAccessKey=FChK/5Ls4g4a37TaMp8jhQdsXjyQwILDFHAhieM+Ymw="

def call_api():
    #complete_api_link = "https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&appid="+key
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=brasov&appid="+key

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    return api_data

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message with simulated telemetry values.
            
            api_data=call_api()
            
            message = Message(str(api_data))

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(20)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()