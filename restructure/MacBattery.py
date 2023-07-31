import psutil
import subprocess
from datetime import datetime


def get_output(cmd):
    """
    A helper method to verify the subprocess before sending an output of the particular macbattery information requested.
    """
    return subprocess.check_output(cmd, shell=True, universal_newlines=True).strip()


class MacBattery:
    """
    Class for defining the macbattery status
    """

    def __init__(self):
        """
            Initializes the BatteryStatus instance.
        """
        self.battery = psutil.sensors_battery()
        self.battery_info = {}

    def is_charger_plugged(self):
        """
        Indicates if the macbattery is currently plugged (True) or unplugged (False).
        """
        return "Plugged" if self.battery.power_plugged else "Unplugged"

    @staticmethod
    def get_battery_health():
        """
        Indicates the health status of the macbattery in percentage (%)
        """
        health_cmd = "system_profiler SPPowerDataType | awk '/Condition/{getline; print $NF}'"
        return get_output(health_cmd)

    def get_battery_percent(self):
        """
        Returns the current percentage of the macbattery
        """
        percent_cmd = "pmset -g batt | awk '/InternalBattery/{print substr($3, 0, length($3)-1)}'"
        # return self.get_output(percent_cmd)
        return self.battery.percent

    @staticmethod
    def get_battery_condition():
        """
        Returns the condition of the macbattery. If the macbattery is still in good condition, it should be NORMAL
        """
        condition_cmd = "system_profiler SPPowerDataType | grep \"Condition\" | awk '{print $2}'"
        return get_output(condition_cmd)

    @staticmethod
    def get_battery_cycle_count():
        """
        Returns the macbattery cycle count.
        """
        cycle_count_cmd = "system_profiler SPPowerDataType | grep \"Cycle Count\" | awk '{print $3}'"
        return get_output(cycle_count_cmd)

    @staticmethod
    def get_charging_status():
        """
        Returns the charging status of the macbattery -
        charged - when fully charged, AC - when charging or discharging - when using the macbattery as its power source
        """
        power_source_cmd = "pmset -g batt | awk '/-InternalBattery-0/{getline; print $4}'"
        return get_output(power_source_cmd)

    def add_info(self, attribute, value):
        """
        This adds information to the Mac Battery.
        Attribute: str (represents the name of the column in the Excel Sheet)
        value: var (varies on the result of the attribute passed in)
        """
        self.battery_info[attribute] = value

    def get_battery_info(self):
        """
        Returns the macbattery info as a dictionary in the format that will be used in the excel file.
        Sample:
        Index: 0, Key: Date, Value: 2023-07-08
        Index: 1, Key: Time, Value: 14:58:21
        Index: 2, Key: PowerAdapter, Value: Plugged
        Index: 3, Key: ChargeStatus, Value: charging;
        Index: 4, Key: BatteryCondition, Value: Normal
        Index: 5, Key: BatteryPercent, Value: 77
        Index: 6, Key: BatteryHealth, Value: 96%
        Index: 7, Key: CycleCount, Value: 52
        Where Index:, Key:, and Value: are indicators of the index, key and value of the dictionary items
        """
        current_date = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')
        self.add_info("Date", current_date)
        self.add_info("Time", current_time)
        self.add_info("PowerAdapter", self.is_charger_plugged())
        self.add_info("ChargeStatus", self.get_charging_status())
        self.add_info("BatteryCondition", self.get_battery_condition())
        self.add_info("BatteryPercent", self.get_battery_percent())
        self.add_info("BatteryHealth", self.get_battery_health())
        self.add_info("CycleCount", self.get_battery_cycle_count())
        return self.battery_info
