import argparse
import teslapy
import requests
from twilio.rest import Client

def parse():
    parser = argparse.ArgumentParser(description='Tesla Charge Reminder via Twilio')
    requredParser =parser.add_argument_group('Required arguments')

    requredParser.add_argument('-e', '--email', help='Email for authentication.',required=True)
    requredParser.add_argument('-p', '--password', help='Password for authentication.',required=True)
    parser.add_argument('-o', '--otp', help='OTP for 2FA (OPTIONAL).', default='')

    args = parser.parse_args()

    email = args.email
    password = args.password
    otp = args.otp
    return email, password, otp

def checkStatus(email,password,otp):
    acceptedCharge = 75

    with teslapy.Tesla(email, password) as tesla: # add lambda:'passcode' if mfa is enabled, it's not yet supported
        tesla.fetch_token()
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()
        chargePercentage = vehicles[0].get_vehicle_data()['charge_state']['battery_level']
        if (vehicles[0].get_vehicle_data()['charge_state']['charging_state'] != "Charging"):
            if(chargePercentage > acceptedCharge):
                txt = "Car not plugged in and has "+str(chargePercentage)+"% Charge! Plug it in"
                sendTextMessage(txt)
        else:
            txt = "Car is plugged in and has "+str(chargePercentage)+"% Charge."
            sendTextMessage(txt)


def sendTextMessage(txt):
    client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz") #Get API and secret from Twilio
    yourNumber = "+15552221422"

    client.messages.create(to=yourNumber, from_="+FromNumber", body=txt)

if __name__ == '__main__':
    email, password,otp = parse()
    checkStatus(email, password,otp)
