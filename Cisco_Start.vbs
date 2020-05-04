Set WshShell = WScript.CreateObject("WScript.Shell")

WshShell.Run """%PROGRAMFILES(x86)%\Cisco\Cisco AnyConnect Secure Mobility Client\vpnui.exe"""

WScript.Sleep 3000

WshShell.AppActivate "Cisco AnyConnect Secure Mobility Client"


WshShell.SendKeys "{ENTER}"

WScript.Sleep 5000

WshShell.SendKeys "PASSWORD"
WshShell.SendKeys "{ENTER}"