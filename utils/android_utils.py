import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '11bd127d',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}


def get_device_udid():

    try:

        result = subprocess.run([f'{os.environ.get("ADB_PATH")}/adb', 'devices', '-l'], capture_output=True, text=True)
        output = result.stdout.strip()
        lines = output.split('\n')
        if len(lines) > 1:
            udid = lines[1].split()[0]
            return udid

    except subprocess.CalledProcessError:
        print("ADB executable not found.")
        return None
