#!/usr/bin/env

import requests
import json

email = "me@matthewhughes.co.uk"
endpoint = "https://haveibeenpwned.com/api/v2/breachedaccount/"

def Check_HIBP_API():
    print("""
    Connecting to the Have I Been Pwned API.
    Address: """ + email + endpoint)

    output = requests.get(endpoint + email)
    return output

def main():
    output = Check_HIBP_API()
    print(output['title'])
    #print(type(output))
    #dump_json = json.dumps(Check_HIBP_API().text)
    #print(len(dump_json))
    #for x in output:
    #    print(output[5])

if __name__ == "__main__":
    main()
