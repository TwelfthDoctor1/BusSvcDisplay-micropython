import network
import time


def connect_to_network(ssid: str, key: str, timeout: int or float):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    while wlan.isconnected() is False:
        try:
            wlan.connect(essid=ssid, key=key)
        
        except OSError as e:
            print(f"Error connecting via WiFi, retrying in {timeout} secs...")
            time.sleep(timeout)