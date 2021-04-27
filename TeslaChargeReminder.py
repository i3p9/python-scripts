import teslapy
import requests
from twilio.rest import Client

def checkStatus():
    email = "something@me.com"
    password = "hunter2"
    acceptedCharge = 75

    with teslapy.Tesla(email, password) as tesla: # add lambda:'passcode' if mfa is enabled
        tesla.fetch_token()
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()
        chargePercentage = vehicles[0].get_vehicle_data()['charge_state']['battery_level']
        if (vehicles[0].get_vehicle_data()['charge_state']['charging_state'] != "Charging"):
            if(chargePercentage > acceptedCharge):
                txt = "Car not plugged in and has "+chargePercentage+"% Charge! Plug it in"
                sendTextMessage(txt)
        else:
            txt = "Car is plugged in and has "+chargePercentage+"% Charge."
            sendTextMessage(txt)


def sendTextMessage(txt):
    client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz") #Get API and secret from Twilio
    yourNumber = "+15552221422"

    client.messages.create(to=yourNumber, from_="+FromNumber", body=txt)

if __name__ == '__main__':
    checkStatus()
