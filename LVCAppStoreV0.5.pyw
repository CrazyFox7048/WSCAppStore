from tkinter import *
from tkinter import ttk
import os

def start():
    global root
    root = Tk()
    root.title("App Store")
    root.config(bg="lightgrey")
    root.resizable(False, False)
    icons()
    root.mainloop()

def icons():
    import urllib.request
    global uninstallIcon
    global downloadIcon
    global nextIcon
    global backIcon
    global exitIcon
    global enterIcon
    if not os.path.exists("L:\\Icons"):
        os.mkdir("L:\\Icons")
    if not os.path.exists("L:\\Icons\\next.png"):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/next.png", filename= "L:\\Icons\\next.png")
    if not os.path.exists("L:\\Icons\\back.png"):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/back.png", filename= "L:\\Icons\\back.png")
    if not os.path.exists("L:\\Icons\\exit.png"):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/exit.png", filename= "L:\\Icons\\exit.png")
    if not os.path.exists("L:\\Icons\\enter.png"):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/enter.png", filename= "L:\\Icons\\enter.png")
    if not os.path.exists("L:\\Icons\\download.png"):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/download.png", filename= "L:\\Icons\\download.png")
    if not os.path.exists("L:\\Icons\\uninstall.png"):
        urllib.request.urlretrieve("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/uninstall.png", filename= "L:\\Icons\\uninstall.png")
    uninstallIcon = PhotoImage(file=r'L:\\Icons\\uninstall.png')
    downloadIcon = PhotoImage(file=r'L:\\Icons\\download.png')
    nextIcon = PhotoImage(file=r'L:\\Icons\\next.png')
    backIcon=PhotoImage(file=r'L:\\Icons\\back.png')
    exitIcon=PhotoImage(file=r'L:\\Icons\\exit.png')
    enterIcon = PhotoImage(file=r'L:\\Icons\\enter.png')
    logon()
    
def logon():
    global root
    global admin
    global enterIcon
    text = Label(root, text="Linton Village College App Store", bg="lightgrey").grid(row=0, column=1, columnspan = 2, padx=5, pady=5)

    Label(root, text='LVC Username:', bg="lightgrey").grid(row=1, column=0, pady=5)
    enteruser = Entry(root)
    enteruser.grid(row=1, column=1, pady=5)

    ttk.Button(root, image=enterIcon, command=lambda: logonCheck(enteruser)).grid(row=1, column=2, padx=5, pady=5)
    
def logonCheck(enteruser):
    global user
    global admin
    user = enteruser.get()
    check = "C:\\Users\\"+user
    if not os.path.exists(check) or check == "C:\\Users\\":
        Label(root, text="Invalid User", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5)
    else:
        admin = "C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"
        page1(user)
def Download(link, name, destination, shortcut, run, message):
    global user
    global admin
    global root
    global exitIcon
    global backIcon
    from pathlib import Path
    import os, webbrowser, time, subprocess, shutil, urllib.request
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text="--- "+name+" Installation ---", bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text="", bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    createBat(user)
    if not os.path.exists(destination):
        os.mkdir(destination)
    label = Label(root, text="Downloading Files (May Take A While)...", bg='lightgrey')
    label.grid(row=2, column=0, padx=5, pady=5)
    file = link.split("/")
    file = file[len(file)-1]
    if os.path.exists(destination + file):
        alreadyDownloaded()
        return
    urllib.request.urlretrieve(link, filename= destination + file)
    while not os.path.exists(destination + file):
        time.sleep(0.1)
    label.destroy()
    Label(root, text="Downloaded", bg='lightgrey').grid(row=2, column=0, padx=5, pady=5)
    if run:
        subprocess.Popen([admin, destination + file])
    Label(root, text="Now Create A Shortcut To '"+shortcut+"' To Run It", bg='lightgrey').grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    Label(root, text=message, bg='lightgrey').grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=5, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=5, column=1, padx=5, pady=5)

def Uninstall(directory, name):
    global root
    global exitIcon
    global backIcon
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text="--- "+name+" Uninstallation ---", bg="lightgrey").grid(row=0, column=1, padx=5, pady=5)
    Label(root, text='', bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
    label = Label(root, text='Uninstalling...', bg="lightgrey")
    label.grid(row=2, column=0, padx=5, pady=5)
    from pathlib import Path
    import os, webbrowser, time, subprocess, shutil
    for dir_path in directory:
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
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=4, column=1, padx=5, pady=5)
    
def manualDownload():
    global root
    global user
    global enterIcon
    global bcakIcon
    for widget in root.winfo_children():
        widget.destroy()
    file = Entry(root)
    link = Entry(root)
    destination=  Entry(root)
    Label(root, text='Manual Mode', bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='Download Link:', bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
    Label(root, text='Install Path:', bg="lightgrey").grid(row=2, column=0, padx=5, pady=5)
    link.grid(row=1, column=1, padx=5, pady=5)
    destination.grid(row=2, column=1, padx=5, pady=5)
    run = IntVar()
    Checkbutton(root, text='Run file after instalation?', bg='lightgrey', variable=run).grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=enterIcon, command=lambda: manualDownloadStart(link, destination, run)).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page2(user)).grid(row=4, column=0, padx=5, pady=5)
def manualDownloadStart(link, destination, run):
    link = link.get()
    destination = destination.get()
    if link != "" and destination != "":
        Download(link, "MANUAL", destination, "EMPTY", run, "")
        return
    else:
        Label(root, text='All Feilds Must Be Filled', bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        return

def manualUninstall():
    global root
    global user
    global enterIcon
    global backIcon
    for widget in root.winfo_children():
        widget.destroy()
    directory = Entry(root)
    Label(root, text='Manual Mode', bg="lightgrey").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='Directory:', bg="lightgrey").grid(row=1, column=0, padx=5, pady=5)
    directory.grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(root, image=enterIcon, command=lambda: manualUninstallStart(directory)).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page2(user)).grid(row=4, column=0, padx=5, pady=5)
def manualUninstallStart(directory):
    directory=directory.get
    if directory != "":
        directory = [directory]
        Uninstall(directory, "MANUAL")
        return
    else:
        Label(root, text='All Feilds Must Be Filled', bg="lightgrey").grid(row=5, column=0, padx=5, pady=5)
        return
def alreadyDownloaded():
    global root
    global backIcon
    global exitIcon
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Error: Program Already Installed', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=2, column=1, padx=5, pady=5)

def notInstalled():
    global root
    global backIcon
    global exitIcon
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Error: Program Not Found', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=2, column=1, padx=5, pady=5)
    
def page1(user):
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Select Program', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)

    global uninstallIcon
    global downloadIcon
    global nextIcon
    global backIcon
    
    Label(root, text='XYPlorer', bg='lightgrey').grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/XYplorerFree_17.40_Install.exe", "XYPlorer", "C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree\\", "C:/Users/"+user+"/AppData/Roaming/XYPlorerFree/XYplorerFree.exe", True, "Enter 'C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree' as the install location")).grid(row=2, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree"],'XYPlorer')).grid(row=2, column=2, padx=5, pady=5)

    Label(root, text="Steam", bg='lightgrey').grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/SteamSetup.exe", "Steam", "C:\\Users\\"+user+"\\AppData\\Roaming\\Steam\\", "C:/Users/"+user+"/AppData/Roaming/Steam/SteamSetup.exe", True, "Enter 'C:\\Users\\"+user+"\\AppData\\Roaming\\Steam' as the install location")).grid(row=3, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\Steam", "C:\\Users\\"+user+"\\AppData\\Local\\Steam"], 'Steam')).grid(row=3, column=2, padx=5, pady=5)

    Label(root, text="OperaGX", bg='lightgrey').grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/OperaSetup.exe", "OperaGX", "C:\\Users\\"+user+"\\AppData\\Roaming\\Opera Software\\", "C:/Users/"+user+"/AppData/Local/Programs/Opera/opera.exe", True, "")).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\Opera Software","C:\\Users\\"+user+"\\AppData\\Local\\Opera Software", "C:\\Users\\"+user+"\\AppData\\Local\\Programs\\Opera", "C:\\Users\\"+user+"\\AppData\\Local\\Temp\\.opera"], "OperaGX")).grid(row=4, column=2, padx=5, pady=5)

    Label(root, text="AT Launcher", bg='lightgrey').grid(row=5, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/ATLauncher.jar", "AT Launcher", "C:\\Users\\"+user+"\\AppData\\Roaming\\ATLauncher\\", "C:/Users/"+user+"/AppData/Roaming/ATLauncher/ATLauncher.jar", False, "")).grid(row=5, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\ATLauncher"], 'AT Launcher')).grid(row=5, column=2, padx=5, pady=5)

    Label(root, text="Page 1", bg='lightgrey').grid(row=6, column=1, padx=5, pady=5)
    ttk.Button(root, image=nextIcon, command=lambda: page2(user)).grid(row=6, column=0, padx=5, pady=5)
    
def page2(user):
    global root
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Select Program', bg='lightgrey').grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg='lightgrey').grid(row=1, column=0, padx=5, pady=5)

    global uninstallIcon
    global downloadIcon
    global nextIcon
    global backIcon
    
    Label(root, text="Advanced Ip Scanner", bg='lightgrey').grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/Advanced_IP_Scanner_2.5.4594.1.exe", "Advanced Ip Scanner", "C:\\Users\\"+user+"\\AppData\\Roaming\\IPScanner\\", "C:/Users/"+user+"/AppData/Roaming/IPScanner/Advanced_IP_Scanner_2.5.4594.1.exe", True, "When Prompted, Select RUN, Not INSTALL")).grid(row=2, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\IPScanner"], 'Advanced Ip Scanner')).grid(row=2, column=2, padx=5, pady=5)

    Label(root, text="Cookie Clicker", bg="lightgrey").grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://download1337.mediafire.com/8dfjgh85pkfgQ_VMDQqFs2nD_DXMaM1INY2Rn22vMaFeGrggWJ_6SFOW6LZAYHifhfmezZbfRynAw62W_jvLOJuSpacS_dDG77Jbg2MthnahZudw3-44IWMHI2vVkFg3bka3ZsUQPvsZPsggn8WjumFnwnHhxQX0ybFG2ok-tg/kxcpjk209ml08ip/CookieClickerInstall.exe", "Cookie Clicker", "C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker\\", "C:/Users/"+user+"/AppData/Roaming/CookieClicker/Cookie Clicker.exe", True, "When promted, extract to 'C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker'")).grid(row=3, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker"], 'CookieClicker')).grid(row=3, column=2, padx=5, pady=5)

    Label(root, text="Animal Jam", bg="lightgrey").grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/AnimalJamInstaller.exe", "Animal Jam", "C:\\Users\\"+user+"\\AppData\\Roaming\\Animal Jam\\", "C:/Users/"+user+"/AppData/Local/Programs/WildWorks/Animal Jam/Launcher.exe", True, "")).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\Animal Jam", "C:\\Users\\"+user+"\\AppData\\Local\\Programs\\WildWorks", "C:\\Users\\"+user+"\\AppData\\LocalLow\\WildWorks", "C:\\Users\\"+user+"\\AppData\\Local\\Temp\\WildWorks\\"], 'Discord')).grid(row=4, column=2, padx=5, pady=5)
    
    Label(root, text="Manual Options:", bg='lightgrey').grid(row=5, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=manualDownload).grid(row=5, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=manualUninstall).grid(row=5, column=2, padx=5, pady=5)

    Label(root, text="Page 2", bg='lightgrey').grid(row=6, column=1, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=6, column=0, padx=5, pady=5)
    
def createBat(user):
    import os, os.path
    if not os.path.isfile("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.txt") and not os.path.isfile("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"):
        f = open("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.txt", "w")
        f.write("""cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" %1" """)
        f.close()
    if not os.path.isfile("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"):
        os.rename("C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.txt", "C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat")

start()
