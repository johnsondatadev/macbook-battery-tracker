from mbt.macbattery.MacBattery import MacBattery

import mbt.utils.excel_loader

excel_file = mbt.utils.excel_loader
mb = MacBattery()


def run():
    battery_info = mb.get_battery_info()
    excel_file.write_battery_info(battery_info)


if __name__ == "__main__":
    pass