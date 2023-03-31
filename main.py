import time
from machine import I2C, Pin
from lcd.lcd_api import LcdApi
from lcd.machine_i2c_lcd import I2cLcd
from BusStop import request_bus_stop_timing
from Credentials import API_KEY, URL
from TimeHandling import get_time
from TimeFuncs import *

# API Settings
LCD_I2C_ADDR = 0x27
LCD_ROWS = 4
LCD_COLS = 20
BUS_STOP = [77009, 77191, 77011, 65191, 65199]

# I2C & LCD
i2c = I2C(0)
lcd = I2cLcd(i2c, LCD_I2C_ADDR, LCD_ROWS, LCD_COLS)

lcd.putstr(f"====================\n")
lcd.putstr(f"Starting Service,\n")
lcd.putstr(f"Please wait...\n")
lcd.putstr(f"====================\n")

# Buttons
b1 = Pin(25, Pin.IN, Pin.PULL_UP)
b2 = Pin(15, Pin.IN, Pin.PULL_UP)

# Get Time & Set to RTC
get_time(8)

# Init Vars
ui_page = 1
bus_id = 0
has_called = False
bus_mem = 0


def get_button_values():
    global b1_value
    global b2_value
    global ui_page
    global bus_id
    global has_called
    b1_value = b1.value()
    b2_value = b2.value()
    print(f"{b1_value} | {b2_value}")
    
    if b1_value == 1 and b2_value == 1:
        has_called = False
    
    elif b1_value == 1:
        if ui_page < 2:
            ui_page += 1
        else:
            ui_page = 1
            has_called = False
    
    elif b2_value == 1:
        has_called = False
        if bus_id < 4:
            bus_id += 1
        else:
            bus_id = 0
    
    time.sleep(0.1)
        


while True:
    get_button_values()
    if ui_page == 1:
        if has_called is False:
            bus_stop_data = request_bus_stop_timing(BUS_STOP[bus_id], API_KEY, URL)
            has_called = True
            bus_mem = BUS_STOP[bus_id]
        lcd.clear()
        
        if len(bus_stop_data) == 0:
            get_button_values()
            lcd.putstr(f"====================\n")
            lcd.putstr(f"No Bus Services\n")
            lcd.putstr(f"Available for {BUS_STOP[bus_id]}\n")
            lcd.putstr(f"====================\n")
            time.sleep(5)
        
        for bus_num_data in bus_stop_data:
            get_button_values()
            lcd.clear()
            
            if ui_page != 1 or BUS_STOP[bus_id] != bus_mem:
                lcd.putstr(f"====================\n")
                lcd.putstr(f"Switching over,\n")
                lcd.putstr(f"Please Wait...\n")
                lcd.putstr(f"====================\n")
                time.sleep(2)
                lcd.clear()
                break
            
            lcd.putstr(f"[{BUS_STOP[bus_id]} - {bus_num_data[0]}]\n")
            lcd.putstr(f"{bus_num_data[2]}\n")
            lcd.putstr(f"{bus_num_data[3]}\n")
            lcd.putstr(f"{bus_num_data[4]}\n")
            
            time.sleep(5)
    
    elif ui_page == 2:
        get_button_values()
        if ui_page != 2:
            lcd.clear()
            lcd.putstr(f"====================\n")
            lcd.putstr(f"Switching over,\n")
            lcd.putstr(f"Please Wait...\n")
            lcd.putstr(f"====================\n")
            time.sleep(2)
            lcd.clear()
        
        dt = time.localtime()
        lcd.putstr(f"====================\n")
        lcd.putstr(f"Time: {convert_12hr(dt[3])}:{time_str(dt[4])}:{time_str(dt[5])} {get_12hr_iden(dt[3])}\n")
        lcd.putstr(f"Date: {time_str(dt[2])}/{time_str(dt[1])}/{dt[0]}\n")
        lcd.putstr(f"====================\n")
     