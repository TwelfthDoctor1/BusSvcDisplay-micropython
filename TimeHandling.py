import network
import usocket
import ustruct
import utime
from machine import RTC
from Networking import connect_to_network

SSID='TD1 WiFi' # Network SSID
KEY='MrSirAdm@TD1Esquire'  # Network key

TIMESTAMP = 2208988800


def get_time(tz: int = 0):
    # Init wlan module and connect to network
    print("Trying to connect... (may take a while)...")

    # Connect to WiFi
    connect_to_network(SSID, KEY, 5)

    # Create new socket
    client = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
    client.bind(("", 8080))
    #client.settimeout(3.0)

    # Get addr info via DNS
    addr = usocket.getaddrinfo("pool.ntp.org", 123)[0][4]

    # Send query
    client.sendto('\x1b' + 47 * '\0', addr)
    data, address = client.recvfrom(1024)

    # Extract data into Time + Handle Timezone
    t = ustruct.unpack(">IIIIIIIIIIII", data)[10] - TIMESTAMP
    dt = utime.localtime(t + (tz * 3600))
    RTC().datetime((dt[0], dt[1], dt[2], dt[6], dt[3], dt[4], dt[5], 0))
    
    print(dt)
    print(f"Time: {dt[3]}:{dt[4]}:{dt[5]}")
    print(f"Date: {dt[2]}/{dt[1]}/{dt[0]}")
    print(f"{t} | {utime.mktime(RTC().datetime())}")
    
#get_time(8)
