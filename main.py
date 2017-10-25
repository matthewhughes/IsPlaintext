#!/usr/bin/env

import requests
import json

email = "me@matthewhughes.co.uk"
endpoint = "https://haveibeenpwned.com/api/v2/breachedaccount/"

def Check_HIBP_API():
    print("""
    Connecting to the Have I Been Pwned API.
    Address: """ + endpoint + email)

    output = requests.get(endpoint + email)
    return output

def main():
    output = Check_HIBP_API()
    output_json = output.json()
    for x in range(len(output_json)):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Title: " + output_json[x]["Title"])
        if(len(output_json[x]["Domain"])) == 0:
            print("No domain associated with this dump")
        else:
            print(output_json[x]["Domain"])

if __name__ == "__main__":
    main()
