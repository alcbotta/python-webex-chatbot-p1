from webexteamssdk import WebexTeamsAPI
import os
import sys

def main():
    
        # Check access token
    access_token = os.environ.get("ACCESS_TOKEN")
    if not access_token:
        print("Please provide your Access Token to be able to execute this code.")
        sys.exit(2)
    api = WebexTeamsAPI(access_token=access_token)
    room = api.rooms.create("a super cool name")
    print (room)


if __name__ == "__main__":
    main()
