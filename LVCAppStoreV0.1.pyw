from tkinter import *
import os

def start():
    global root
    root = Tk()
    root.title("App Store")
    root.config(bg="lightgrey")
    #root.geometry("600x400")
    page1()
    root.mainloop()
def page1():
    global root
    global admin
    text = Label(root, text="Linton Village College App Store", bg="lightgrey").grid(row=0, column=1, columnspan = 2, padx=5, pady=5)

    Label(root, text='LVC Username:', bg="lightgrey").grid(row=1, column=0, pady=5)
    enteruser = Entry(root)
    enteruser.grid(row=1, column=1, pady=5)

    Button(root, text="Next", bg="lightgrey", command=lambda: page1nextcheck(enteruser)).grid(row=2, column=1, padx=5, pady=5)
    
def page1nextcheck(enteruser):
    global user
    global admin
    user = enteruser.get()
    check = "C:\\Users\\"+user
    if not os.path.exists(check) or check == "C:\\Users\\":
        Label(root, text="Invalid User", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5)
    else:
        admin = "C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"
        page2(user)
def Install(file, link, name, destination, shortcut, run, message):
    global user
    global admin
    global root
    from pathlib import Path
    import os, webbrowser, time, subprocess, shutil, urllib.request
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text="--- "+name+" Installation ---", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text="", bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    createBat(user)
    if not os.path.exists(destination):
        os.mkdir(destination)
    else:
        alreadyInstalled()
        return
    label = Label(root, text="Downloading Files...", bg='lightgrey')
    label.grid(row=2, column=0, padx=5, pady=5)
    urllib.request.urlretrieve(link, filename="L:\\"+file)
    while not os.path.exists("L:/"+file):
        time.sleep(0.1)
    label.destroy()
    label=Label(root, text="Installing...", bg='lightgrey')
    label.grid(row=2, column=0, padx=5, pady=5)
    time.sleep(1)
    shutil.move("L:\\"+file, destination + file)
    while not os.path.exists(destination + file):
        time.sleep(0.1)
    label.destroy()
    Label(root, text="Installed", bg='lightgrey').grid(row=2, column=0, padx=5, pady=5)
    if run:
        subprocess.Popen([admin, destination + file])
    Label(root, text="Now Create A Shortcut To '"+shortcut+"' To Run It", bg='lightgrey').grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    Label(root, text=message, bg='lightgrey').grid(row=4, column=0, padx=5, pady=5)
    Button(root, text="Back", bg="lightgrey", command=lambda: page2(user)).grid(row=5, column=0, padx=5, pady=5)
    Button(root, text="Exit", bg="lightgrey", command=root.destroy).grid(row=5, column=1, padx=5, pady=5)
def Uninstall(dir_path, name):
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text="--- "+name+" Uninstallation ---", bg="lightgrey").grid(row=0, column=1, padx=5, pady=5)
    Label(root, text='', bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
    label = Label(root, text='Uninstalling...', bg="lightgrey")
    label.grid(row=2, column=0, padx=5, pady=5)
    from pathlib import Path
    import os, webbrowser, time, subprocess, shutil
    new_sub_dirs = []
    paths = []
    path_dirs = []
    new_sub_dirs1 = []
    file_names = []
    found_sub_dir = False
    run = False
    sub_dirs = [dir_path]
    if not os.path.exists(dir_path):
        notInstalled()
        return
    for path in os.scandir(dir_path):
        path_dirs.append(dir_path)
        if path.is_file():
            file_names.append(path.name)
            path = dir_path + "\\" + path.name
            paths.append(path)
        else:
            path = dir_path + "\\" + path.name
            new_sub_dirs.append(path)
            found_sub_dir = True
            run = True
    while run == True:
        found_new_sub_dir = False
        for i in range(0,len(new_sub_dirs)):
            dir_path = new_sub_dirs[i]
            path_dirs.append(dir_path)
            for path in os.scandir(dir_path):
                if path.is_file():
                    file_names.append(path.name)
                    path = dir_path + "\\" + path.name
                    paths.append(path)
                else:
                    path = dir_path + "\\" + path.name
                    new_sub_dirs1.append(path)
                    found_new_sub_dir = True
                    run = True
        sub_dirs.extend(new_sub_dirs)
        new_sub_dirs = new_sub_dirs1
        new_sub_dirs1 = []
        if found_new_sub_dir == False:
            run = False
        elif found_new_sub_dir == True:
            run = True
    for i in range(0, len(paths)):
        try:
            os.remove(paths[i])
        except Exception:
            pass
    path_dirs.reverse()
    for i in range(0, len(path_dirs)):
        try:
            os.rmdir(path_dirs[i])
        except Exception:
            pass
    try:
        os.rmdir(dir_path)
    except Exception:
        pass
    global user
    label.destroy()
    Label(root, text='Uninstalled', bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
    Button(root, text="Back", bg="lightgrey", command=lambda: page2(user)).grid(row=4, column=0, padx=5, pady=5)
    Button(root, text="Exit", bg="lightgrey", command=root.destroy).grid(row=4, column=1, padx=5, pady=5)

def UninstallOpera():
    Uninstall("C:\\Users\\"+user+"\\AppData\\Roaming\\Opera Software", "OperaGX")
    Uninstall("C:\\Users\\"+user+"\\AppData\\Local\\Opera Software", "OperaGX")
    Uninstall("C:\\Users\\"+user+"\\AppData\\Local\\Programs\\Opera", "OperaGX")
    
def manual():
    global root
    global user
    for widget in root.winfo_children():
        widget.destroy()
    file = Entry(root)
    link = Entry(root)
    destination=  Entry(root)
    Label(root, text='Manual Mode', bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='File Name:', bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
    Label(root, text='Download Link:', bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
    Label(root, text='Install Path:', bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
    file.grid(row=1, column=1, padx=5, pady=5)
    link.grid(row=2, column=1, padx=5, pady=5)
    destination.grid(row=3, column=1, padx=5, pady=5)
    run = IntVar()
    Checkbutton(root, text='Run file after instalation?', bg='lightgrey', variable=run).grid(row=4, column=0, padx=5, pady=5)
    Button(root, text="Enter", bg="lightgrey", command=lambda: manual2(file, link, destination, run)).grid(row=5, column=0, padx=5, pady=5)
def manual2(file, link, destination, run):
    file = file.get()
    link = link.get()
    destination = destination.get()
    Install(file, link, "MANUAL", destination, "EMPTY", run, "")
    
def alreadyInstalled():
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Error: Program Already Installed', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    Button(root, text="Back", bg="lightgrey", command=lambda: page2(user)).grid(row=2, column=0, padx=5, pady=5)
    Button(root, text="Exit", bg="lightgrey", command=root.destroy).grid(row=2, column=1, padx=5, pady=5)

def notInstalled():
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Error: Program Not Found', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    Button(root, text="Back", bg="lightgrey", command=lambda: page2(user)).grid(row=2, column=0, padx=5, pady=5)
    Button(root, text="Exit", bg="lightgrey", command=root.destroy).grid(row=2, column=1, padx=5, pady=5)
    
def page2(user):
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Select Program', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)

    Label(root, text='XYPlorer', bg='lightgrey').grid(row=2, column=0, padx=5, pady=5)
    Button(root, text='Install', bg='lightgrey', command=lambda: Install("XYplorerFree_17.40_Install.exe", "https://github.com/CrazyFox7048/LVCAppStore/raw/main/XYplorerFree_17.40_Install.exe", "XYPlorer", "C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree\\", "C:/Users/"+user+"/AppData/Roaming/XYPlorerFree/XYplorerFree.exe", True, "Enter 'C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree' as the install location")).grid(row=2, column=1, padx=5, pady=5)
    Button(root, text='Uninstall', bg='lightgrey', command=lambda: Uninstall("C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree",'XYPlorer')).grid(row=2, column=2, padx=5, pady=5)

    Label(root, text="Steam", bg='lightgrey').grid(row=3, column=0, padx=5, pady=5)
    Button(root, text='Install', bg='lightgrey', command=lambda: Install("SteamSetup.exe", "https://github.com/CrazyFox7048/LVCAppStore/raw/main/SteamSetup.exe", "Steam", "C:\\Users\\"+user+"\\AppData\\Roaming\\Steam\\", "C:/Users/"+user+"/AppData/Roaming/Steam/SteamSetup.exe", True, "Enter 'C:\\Users\\"+user+"\\AppData\\Roaming\\Steam' as the install location")).grid(row=3, column=1, padx=5, pady=5)
    Button(root, text='Uninstall', bg='lightgrey', command=lambda: Uninstall("C:\\Users\\"+user+"\\AppData\\Roaming\\Steam", 'Steam')).grid(row=3, column=2, padx=5, pady=5)

    Label(root, text="OperaGX", bg='lightgrey').grid(row=4, column=0, padx=5, pady=5)
    Button(root, text='Install', bg='lightgrey', command=lambda: Install("OperaSetup.exe", "https://github.com/CrazyFox7048/LVCAppStore/raw/main/OperaSetup.exe", "OperaGX", "C:\\Users\\"+user+"\\AppData\\Roaming\\Opera Software\\", "C:/Users/"+user+"/AppData/Local/Programs/Opera/opera.exe", True, "")).grid(row=4, column=1, padx=5, pady=5)
    Button(root, text='Uninstall', bg='lightgrey', command= UninstallOpera).grid(row=4, column=2, padx=5, pady=5)

    Label(root, text="AT Launcher", bg='lightgrey').grid(row=5, column=0, padx=5, pady=5)
    Button(root, text='Install', bg='lightgrey', command=lambda: Install("ATLauncher.jar", "https://github.com/CrazyFox7048/LVCAppStore/raw/main/ATLauncher.jar", "AT Launcher", "C:\\Users\\"+user+"\\AppData\\Roaming\\ATLauncher\\", "C:/Users/"+user+"/AppData/Roaming/ATLauncher/ATLauncher.jar", False, "")).grid(row=5, column=1, padx=5, pady=5)
    Button(root, text='Install', bg='lightgrey', command=lambda: Uninstall("C:\\Users\\"+user+"\\AppData\\Roaming\\ATLauncher", 'AT Launcher')).grid(row=5, column=2, padx=5, pady=5)

    Label(root, text="Page 1", bg='lightgrey').grid(row=6, column=1, padx=5, pady=5)
    Button(root, text='Next', bg='lightgrey', command=lambda: page3(user)).grid(row=6, column=0, padx=5, pady=5)
    
def page3(user):
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Select Program', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    
    Label(root, text="Advanced Ip Scanner", bg='lightgrey').grid(row=2, column=0, padx=5, pady=5)
    Button(root, text="Install", bg='lightgrey', command=lambda: Install("Advanced_IP_Scanner_2.5.4594.1.exe", "https://github.com/CrazyFox7048/LVCAppStore/raw/main/Advanced_IP_Scanner_2.5.4594.1.exe", "Advanced Ip Scanner", "C:\\Users\\"+user+"\\AppData\\Roaming\\IPScanner\\", "C:/Users/"+user+"/AppData/Roaming/IPScanner/Advanced_IP_Scanner_2.5.4594.1.exe", True, "When Prompted, Select RUN, Not INSTALL")).grid(row=2, column=1, padx=5, pady=5)
    Button(root, text="Uninstall", bg='lightgrey', command=lambda: Uninstall("C:\\Users\\"+user+"\\AppData\\Roaming\\IPScanner", 'Advanced Ip Scanner')).grid(row=2, column=2, padx=5, pady=5)

    Label(root, text="Cookie Clicker", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
    Button(root, text="Install", bg='lightgrey', command=lambda: Install("CookieClickerInstall.exe", "https://download1337.mediafire.com/x866qnu32jkg6kmTI5SksKkfY4h_sjC2EPWNeCJ1TjXOVw3Zyu5Zp8yDwX3F7Qkb-U1eziysk1gcLBrprhYGXR4bRMdHNAZJm_90FyiGidQ_nwEdKZPkT70KP3Jmj3f_YWEa3mEii3MzgpQcj7boLBi8IgGEBf1GfI-LyCgBqQ/kxcpjk209ml08ip/CookieClickerInstall.exe", "Cookie Clicker", "C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker\\", "C:/Users/"+user+"/AppData/Roaming/CookieClicker/CookieClicker.exe", True, "When promted, extract to 'C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker'")).grid(row=3, column=1, padx=5, pady=5)
    Button(root, text="Uninstall", bg='lightgrey', command=lambda: Uninstall("C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker", 'CookieClicker')).grid(row=3, column=2, padx=5, pady=5)
    
    Label(root, text="Manual Mode", bg='lightgrey').grid(row=4, column=0, padx=5, pady=5)
    Button(root, text="Enter", bg='lightgrey', command=manual).grid(row=4, column=1, padx=5, pady=5)
    
    Label(root, text="Page 2", bg='lightgrey').grid(row=5, column=1, padx=5, pady=5)
    Button(root, text='Back', bg='lightgrey', command=lambda: page2(user)).grid(row=5, column=0, padx=5, pady=5)
    
def createBat(user):
    import os, os.path
    if not os.path.isfile("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.txt") and not os.path.isfile("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"):
        f = open("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.txt", "w")
        f.write("""cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" %1" """)
        f.close()
    if not os.path.isfile("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"):
        os.rename("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.txt", "C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat")

start()
