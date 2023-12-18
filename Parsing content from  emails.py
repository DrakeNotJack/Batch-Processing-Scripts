import os
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

url = r'Your_Email_folder_path_here'

dir_path = os.path.abspath(url)

files = os.listdir(url)

for file in files:
    if file.endswith('.msg'):
        file_path = os.path.join(dir_path,file)
        msg = outlook.OpenSharedItem(file_path)
        print(msg.SenderName)
        print(msg.SenderEmailAddress)
        print(msg.SentOn)
        print(msg.To)
        print(msg.CC)
        print(msg.BCC)
        print(msg.Subject)
        print(msg.Body)
        msg = None
        print('-----------------------------------------------------')
