from battery.MacBattery import MacBattery
from datetime import datetime
import utils.excel_loader

excel_file = utils.excel_loader
mb = MacBattery()
# from schedules import execute_script
# Loop through the dictionary and print index number, key, and value
def write_battery_info():
#     return mac_info
    for index, (key, value) in enumerate(mac_info.items()):
        print(f"Index: {index}, Key: {key}, Value: {value}")


def add_info(attribute, value):
    """
    This adds information to the Mac Battery.
    Attribute: str (represents the name of the column in the Excel Sheet)
    value: var (varies on the result of the attribute passed in)
    """
    mac_info[attribute] = value


# def get_battery_info():
#     current_date = datetime.now().strftime('%Y-%m-%d')
#     current_time = datetime.now().strftime('%H:%M:%S')
#     mb = MacBattery()
#     add_info("Date", current_date)
#     add_info("Time", current_time)
#     add_info("PowerAdapter", mb.is_charger_plugged())
#     add_info("ChargeStatus", get_charging_status())
#     add_info("BatteryCondition", mb.get_battery_condition())
#     add_info("BatteryPercent", mb.get_battery_percent())
#     add_info("BatteryHealth", mb.get_battery_health())
#     add_info("CycleCount", mb.get_battery_cycle_count())
#     return mac_info


def run():
    battery_info = mb.get_battery_info()
    # excel_file.write_battery_info(battery_info)
    excel_file.write_battery_info(battery_info)


# def run():
#     mb = MacBattery()
#     print(f"Health: {mb.get_battery_health()}")
#     print(f"Cycle Count: {mb.get_battery_cycle_count()}")
#     print(f"Percent: {mb.get_battery_percent()}")
#     print(f"Charge status: {mb.get_charging_status()}")
#     print(f"Condition: {mb.get_battery_condition()}")
#     print(f"Charger connected: {mb.is_charger_plugged()}")


if __name__ == "__main__":
    mac_info = {}
    run()
