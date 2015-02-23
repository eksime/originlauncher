from winreg import *
from os import getenv
from xml.dom import minidom

aKey = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Electronic Arts\EA Core")
originDir = QueryValueEx(aKey , r"EADM6InstallDir")[0]
CloseKey(aKey)  
   
xml = minidom.parse(getenv("APPDATA") + r"\origin\local.xml")
itemlist = xml.getElementsByTagName('Setting')

for s in itemlist :
    if s.attributes["key"].value == "DownloadInPlaceDir" :
        originGamesDir = s.attributes["value"].value
        break

print(originDir) 
print(originGamesDir) 