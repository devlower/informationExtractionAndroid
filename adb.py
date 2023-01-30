import subprocess

local_ADB = 'C:\\Temp\\scan-android-device\\platform-tools'

def get_devices():
    output = subprocess.Popen('adb devices', cwd=local_ADB, shell=True, stdout=subprocess.PIPE).communicate()[0]
    output = str(output).split('attached')[1]
    output = output.split('device')[0]
    output = output.replace("\\n", "").replace("\\r", "")
    output = output.replace("\\t", "")
    return output

def get_manufacturer():
    output = subprocess.Popen('adb shell getprop ro.product.manufacturer', cwd=local_ADB, shell=True, stdout=subprocess.PIPE).communicate()[0]
    output = str(output).split('attached')[0]
    output = output.replace("\\n", "").replace("\\r", "")
    output = output.replace("\\t", "")
    output = output[1:]
    return output

def get_name():
    output = subprocess.Popen('adb shell getprop ro.product.name', cwd=local_ADB, shell=True, stdout=subprocess.PIPE).communicate()[0]
    output = str(output).split('attached')[0]
    output = output.replace("\\n", "").replace("\\r", "")
    output = output.replace("\\t", "")
    output = output[1:]
    return output

def get_model():
    output = subprocess.Popen('adb shell getprop ro.product.model', cwd=local_ADB, shell=True, stdout=subprocess.PIPE).communicate()[0]
    output = str(output).split('attached')[0]
    output = output.replace("\\n", "").replace("\\r", "")
    output = output.replace("\\t", "")
    output = output[1:]
    return output

def get_contacts(path):
    output = subprocess.Popen('adb shell content query --uri content://com.android.contacts/data/phones', cwd=local_ADB, shell=True, stdout=subprocess.PIPE).communicate()[0]
    output = str(output).split('attached')[0]
    output = output.replace("\\n", "").replace("\\r", "")
    output = output.replace("\\t", "")

    with open(path, 'w') as f:
        f.write(output[2:])

    return output
    