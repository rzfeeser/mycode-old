#!/usr/bin/python3

# python3 -m pip install requests
import requests

def main():

  # make http request to http://api.open-notify.org/iss-now.json
  resp = requests.get('http://api.open-notify.org/iss-now.json')

  # assign data from response to resp
  resp = resp.json()


  #resp =  {"message": "success", "timestamp": 1672960388, "iss_position": {"latitude": "100.5055", "longitude": "-0.7373"}}


  # Display status of the mission
  print('Status of the mission:', resp["message"])
  print(f'Status of the mission: {resp.get("message")}')

  # Display just latitude
  print('Status of the mission:', resp["iss_position"]["latitude"])
  print(f'ISS latitude: {resp.get("iss_position").get("latitude")}')

  
  if abs(float(resp.get("iss_position").get("latitude"))) < 15:
      print("close to the equator!")


if __name__ == "__main__":
    main()
