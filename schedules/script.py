import time
import subprocess
import constants


def execute_script():
    schedule_script_execution()
    subprocess.call(["python", constants.APP_PATH])


def schedule_script_execution():
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time in ["02:00:00", "09:00:00", "12:00:00", "15:00:00", "20:15:00", "22:47:00", "00:00:00"]:
            execute_script()
        time.sleep(1)


def run():
    execute_script()


# main()
if __name__ == "__main__":
    run()
