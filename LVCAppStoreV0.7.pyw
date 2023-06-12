from tkinter import *
from tkinter import ttk
import os

def start():
    global root
    global bg
    root = Tk()
    root.title("App Store")
    dark()
    root.resizable(False, False)
    logon()
    root.mainloop()
    
def get_image_from_url(url):
    from PIL import Image
    from PIL import ImageTk
    import urllib.request
    img = ImageTk.PhotoImage(image = Image.open(urllib.request.urlopen(url)))
    return img

def dark():
    from tkinter import ttk
    global root
    global TCheckButton
    global TLabel
    global bg
    global fg
    ttk.Style().configure('.', foreground="#f2f4f5", background="#3c4043")
    ttk.Style().configure('TButton', foreground="black")
    bg = "#3c4043"
    root.config(bg=bg)
    fg = "#f2f4f5"

def light():
    global root
    global bg
    global fg
    ttk.Style().configure('.', foreground="black", background="lightgrey")
    ttk.Style().configure('TButton', foreground="black")
    bg = "lightgrey"
    root.config(bg=bg)
    fg = "black"
    
def logon():
    global root
    global admin
    global enterIcon
    global bg
    global fg
    import urllib.request
    global uninstallIcon
    global downloadIcon
    global nextIcon
    global backIcon
    global exitIcon
    global enterIcon
    dark()
    uninstallIcon = get_image_from_url("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/uninstall.png")
    downloadIcon = get_image_from_url("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/download.png")
    nextIcon = get_image_from_url("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/next.png")
    backIcon = get_image_from_url("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/back.png")
    exitIcon = get_image_from_url("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/exit.png")
    enterIcon = get_image_from_url("https://raw.githubusercontent.com/CrazyFox7048/LVCAppStore/main/enter.png")
    
    ttk.Label(root, text="Linton Village College App Store").grid(row=0, column=1, columnspan = 2, padx=5, pady=5)

    ttk.Label(root, text='LVC Username:').grid(row=1, column=0, pady=5)
    enteruser = Entry(root)
    enteruser.grid(row=1, column=1, pady=5)
    mode = BooleanVar(value=True)
    ttk.Checkbutton(root, text='Dark Mode', command=lambda: themeChange(mode), variable=mode, takefocus=0).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=enterIcon, command=lambda: logonCheck(enteruser)).grid(row=1, column=2, padx=5, pady=5)

def themeChange(mode):
    if mode.get():
        dark()
    elif not mode.get():
        light()
    else:
        print("error")
def logonCheck(enteruser):
    global user
    global admin
    global bg
    global fg
    user = enteruser.get()
    check = "C:\\Users\\"+user
    if not os.path.exists(check) or check == "C:\\Users\\":
        Label(root, text="Invalid User", bg=bg, fg="red").grid(row=3, column=1, padx=5, pady=5)
    else:
        admin = "C:\\Users\\"+user+"\\AppData\\Roaming\\Admin.bat"
        page1(user)

def Download(link, name, destination, shortcut, run, message):
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text="--- "+name+" Installation ---", bg=bg, fg=fg).grid(row=0, column=0, padx=5, pady=5)
    button = ttk.Button(root, text="Start", command=lambda: DownloadStart(link, name, destination, shortcut, run, message, button, msg, msg1))
    msg = Label(root, text="(Downloads May Take Up to 5 Minutes)", bg=bg, fg=fg)
    msg1 = Label(root, text="Follow all installation instructions during and after install for proper program function", bg=bg, fg=fg)
    msg.grid(row=1, column=0, padx=5, pady=5)
    msg1.grid(row=2, column=0, padx=5, pady=5)
    button.grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=5, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=5, column=1, padx=5, pady=5)

def DownloadStart(link, name, destination, shortcut, run, message, button, msg, msg1):
    global user
    global admin
    global root
    global exitIcon
    global backIcon
    global bg
    global fg
    from pathlib import Path
    import os, webbrowser, time, subprocess, shutil, urllib.request
    msg.destroy()
    msg1.destroy()
    button.destroy()
    Label(root, text="", bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)
    createBat(user)
    if not os.path.exists(destination):
        os.mkdir(destination)
    file = link.split("/")
    file = file[len(file)-1]
    if os.path.exists(destination + file):
        alreadyDownloaded()
        return
    urllib.request.urlretrieve(link, filename= destination + file)
    while not os.path.exists(destination + file):
        time.sleep(0.1)
    Label(root, text="Downloaded", bg=bg, fg=fg).grid(row=2, column=0, padx=5, pady=5)
    if run:
        subprocess.Popen([admin, destination + file])
    Label(root, text="Now Create A Shortcut To '"+shortcut+"' To Run It", bg=bg, fg=fg).grid(row=3, column=0, columnspan=3, padx=5, pady=5)
    Label(root, text=message, bg=bg, fg=fg).grid(row=4, column=0, padx=5, pady=5)

def Uninstall(directory, name):
    global root
    global exitIcon
    global backIcon
    global bg
    global fg
    
    for widget in root.winfo_children():
        widget.destroy()
    
    Label(root, text="--- "+name+" Uninstallation ---", bg=bg, fg=fg).grid(row=0, column=1, padx=5, pady=5)
    Label(root, text='', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)
    label = Label(root, text='Uninstalling...', bg=bg, fg=fg)
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
    Label(root, text='Uninstalled', bg=bg, fg=fg).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=4, column=1, padx=5, pady=5)
    
def manualDownload():
    global root
    global user
    global enterIcon
    global backIcon
    global bg
    global fg
    
    for widget in root.winfo_children():
        widget.destroy()
    file = Entry(root)
    link = Entry(root)
    destination=  Entry(root)
    Label(root, text='Manual Mode', bg=bg, fg=fg).grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='Download Link:', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)
    Label(root, text='Install Path:', bg=bg, fg=fg).grid(row=2, column=0, padx=5, pady=5)
    link.grid(row=1, column=1, padx=5, pady=5)
    destination.grid(row=2, column=1, padx=5, pady=5)
    run = BooleanVar(value=True)
    ttk.Checkbutton(root, text='Run file after instalation?', takefocus=0, variable = run).grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=enterIcon, command=lambda: manualDownloadStart(link, destination, run)).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page2(user)).grid(row=4, column=0, padx=5, pady=5)
    
def manualDownloadStart(link, destination, run):
    global bg
    global fg
    link = link.get()
    destination = destination.get()
    if link != "" and destination != "":
        Download(link, "MANUAL", destination, "EMPTY", run, "")
        return
    else:
        Label(root, text='All Feilds Must Be Filled', bg=bg, fg="red").grid(row=5, column=0, padx=5, pady=5)
        return

def manualUninstall():
    global bg
    global fg
    global root
    global user
    global enterIcon
    global backIcon
    for widget in root.winfo_children():
        widget.destroy()
    directory = Entry(root)
    Label(root, text='Manual Mode', bg=bg, fg=fg).grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='Directory:', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)
    directory.grid(row=1, column=1, padx=5, pady=5)
    ttk.Button(root, image=enterIcon, command=lambda: manualUninstallStart(directory)).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page2(user)).grid(row=4, column=0, padx=5, pady=5)
def manualUninstallStart(directory):
    global bg
    global fg
    directory=directory.get
    if directory != "":
        directory = [directory]
        Uninstall(directory, "MANUAL")
        return
    else:
        Label(root, text='All Feilds Must Be Filled', bg=bg, fg="red").grid(row=5, column=0, padx=5, pady=5)
        return
def alreadyDownloaded():
    global root
    global bg
    global fg
    global backIcon
    global exitIcon
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Error: Program Already Installed', bg=bg, fg="red").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=2, column=1, padx=5, pady=5)

def notInstalled():
    global root
    global bg
    global fg
    global backIcon
    global exitIcon
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Error: Program Not Found', bg=bg, fg="red").grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)
    ttk.Button(root, image=backIcon, command=lambda: page1(user)).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=exitIcon, command=root.destroy).grid(row=2, column=1, padx=5, pady=5)
    
def page1(user):
    global root
    global bg
    global fg
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Select Program', bg=bg, fg=fg).grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)

    global uninstallIcon
    global downloadIcon
    global nextIcon
    global backIcon
    
    Label(root, text='XYPlorer', bg=bg, fg=fg).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/XYplorerFree_17.40_Install.exe", "XYPlorer", "C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree\\", "C:/Users/"+user+"/AppData/Roaming/XYPlorerFree/XYplorerFree.exe", True, "Enter 'C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree' as the install location")).grid(row=2, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\XYPlorerFree"],'XYPlorer')).grid(row=2, column=2, padx=5, pady=5)

    Label(root, text="Steam", bg=bg, fg=fg).grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/SteamSetup.exe", "Steam", "C:\\Users\\"+user+"\\AppData\\Roaming\\Steam\\", "C:/Users/"+user+"/AppData/Roaming/Steam/SteamSetup.exe", True, "Enter 'C:\\Users\\"+user+"\\AppData\\Roaming\\Steam' as the install location")).grid(row=3, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\Steam", "C:\\Users\\"+user+"\\AppData\\Local\\Steam"], 'Steam')).grid(row=3, column=2, padx=5, pady=5)

    Label(root, text="OperaGX", bg=bg, fg=fg).grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/OperaSetup.exe", "OperaGX", "C:\\Users\\"+user+"\\AppData\\Roaming\\Opera Software\\", "C:/Users/"+user+"/AppData/Local/Programs/Opera/opera.exe", True, "")).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\Opera Software","C:\\Users\\"+user+"\\AppData\\Local\\Opera Software", "C:\\Users\\"+user+"\\AppData\\Local\\Programs\\Opera", "C:\\Users\\"+user+"\\AppData\\Local\\Temp\\.opera"], "OperaGX")).grid(row=4, column=2, padx=5, pady=5)

    Label(root, text="AT Launcher", bg=bg, fg=fg).grid(row=5, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/ATLauncher.jar", "AT Launcher", "C:\\Users\\"+user+"\\AppData\\Roaming\\ATLauncher\\", "C:/Users/"+user+"/AppData/Roaming/ATLauncher/ATLauncher.jar", False, "")).grid(row=5, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\ATLauncher"], 'AT Launcher')).grid(row=5, column=2, padx=5, pady=5)

    Label(root, text="Page 1", bg=bg, fg=fg).grid(row=6, column=1, padx=5, pady=5)
    ttk.Button(root, image=nextIcon, command=lambda: page2(user)).grid(row=6, column=0, padx=5, pady=5)
    
def page2(user):
    global root
    global bg
    global fg
    for widget in root.winfo_children():
        widget.destroy()
    Label(root, text='Select Program', bg=bg, fg=fg).grid(row=0, column=0, padx=5, pady=5)
    Label(root, text='', bg=bg, fg=fg).grid(row=1, column=0, padx=5, pady=5)

    global uninstallIcon
    global downloadIcon
    global nextIcon
    global backIcon
    
    Label(root, text="Advanced Ip Scanner", bg=bg, fg=fg).grid(row=2, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/Advanced_IP_Scanner_2.5.4594.1.exe", "Advanced Ip Scanner", "C:\\Users\\"+user+"\\AppData\\Roaming\\IPScanner\\", "C:/Users/"+user+"/AppData/Roaming/IPScanner/Advanced_IP_Scanner_2.5.4594.1.exe", True, "When Prompted, Select RUN, Not INSTALL")).grid(row=2, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\IPScanner"], 'Advanced Ip Scanner')).grid(row=2, column=2, padx=5, pady=5)

    Label(root, text="Cookie Clicker", bg=bg, fg=fg).grid(row=3, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://download1508.mediafire.com/fdll9lq5vbpgLHRjnkYac6HyQEYtf56_mnK7LrxVxPgClhmgnxz8Hi72E5QzbP_793V4TV2LWbqRCscle7GamPdMczitI8a_Zetzq0L2JKUk5pzh9kPPhv0Rt41Pj_XEEIW0rrQBYDILRposYLPs76XiNtB36Mj16P2wWb3eKg/cb5xca2mttby0s3/CookieClicker.exe", "Cookie Clicker", "C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker\\", "C:/Users/"+user+"/AppData/Roaming/CookieClicker/CookieClicker/Cookie Clicker.exe", True, "When promted, extract to 'C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker'")).grid(row=3, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\CookieClicker"], 'CookieClicker')).grid(row=3, column=2, padx=5, pady=5)

    Label(root, text="Animal Jam", bg=bg, fg=fg).grid(row=4, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=lambda: Download("https://github.com/CrazyFox7048/LVCAppStore/raw/main/AnimalJamInstaller.exe", "Animal Jam", "C:\\Users\\"+user+"\\AppData\\Roaming\\Animal Jam\\", "C:/Users/"+user+"/AppData/Local/Programs/WildWorks/Animal Jam/Launcher.exe", True, "")).grid(row=4, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=lambda: Uninstall(["C:\\Users\\"+user+"\\AppData\\Roaming\\Animal Jam", "C:\\Users\\"+user+"\\AppData\\Local\\Programs\\WildWorks", "C:\\Users\\"+user+"\\AppData\\LocalLow\\WildWorks", "C:\\Users\\"+user+"\\AppData\\Local\\Temp\\WildWorks\\"], 'Discord')).grid(row=4, column=2, padx=5, pady=5)
    
    Label(root, text="Manual Options:", bg=bg, fg=fg).grid(row=5, column=0, padx=5, pady=5)
    ttk.Button(root, image=downloadIcon, command=manualDownload).grid(row=5, column=1, padx=5, pady=5)
    ttk.Button(root, image=uninstallIcon, command=manualUninstall).grid(row=5, column=2, padx=5, pady=5)

    Label(root, text="Page 2", bg=bg, fg=fg).grid(row=6, column=1, padx=5, pady=5)
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
