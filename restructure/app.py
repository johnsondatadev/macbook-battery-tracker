
import excel_loader
import MacBattery

excel_file = excel_loader
mb = MacBattery.MacBattery()


def run():
    battery_info = mb.get_battery_info()
    excel_loader.write_battery_info(battery_info)


if __name__ == "__main__":
    run()
