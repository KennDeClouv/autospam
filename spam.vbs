Set WshShell = WScript.CreateObject("WScript.Shell")

' The message to send
message = "Hello, this is a test message!"

' Number of times to send the message
count = 10

' Wait for 5 seconds to allow the user to switch to WhatsApp Desktop
WScript.Sleep 5000

' Send the message repeatedly
For i = 1 To count
    WshShell.SendKeys message
    WshShell.SendKeys "{ENTER}"
    WScript.Sleep 1000 ' 1 second delay between messages
Next
