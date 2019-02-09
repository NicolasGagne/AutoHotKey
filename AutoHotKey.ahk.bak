#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#InstallKeybdHook

;/////////////////////////////////////////////
;//////////  Global Script Variable //////////
Browser=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe


;///////////////////////////////////////////////
;/////////      Utilities   ////////////////////

^r:: ; reload autohot key script
    send, ^s   ; save the script
    reload ; Reload auto hot key script
return

;//////////////////////////////////////////////
;/////////////  Work Utilities ////////////////

^i:: ; Check ICAO code for name of the airport
    Send, ^c
    Sleep, 250
    ICAO=%clipboard% 
    If StrLen(clipboard) == 4{
        RunWait, dist\main_autohotkey.exe %ICAO% ; clipboard content
        Msgbox, 0, ICAO Check  -- %ICAO% --, %clipboard%, 2 ; message box with airport name
    }
    else{
        Msgbox, 0, ICAO Check  -- %ICAO% --, -- %ICAO% -- is NOT a valid 4 digits code !, 2
    }
return

;////////////////////////////////////////////////////
;/////////////   Internet shortcut  /////////////////

^g:: ; search google.com 
    Send, ^c
    Sleep, 250
    RunWait, %Browser% https://www.google.com/search?q=%Clipboard%
return

 
^y:: ; search youtube.com 
    Send, ^c
    Sleep, 250
    RunWait, %Browser% https://www.youtube.com//results?search_query=%Clipboard%
return

^w:: ; search wikepedia.com 
    Send, ^c
    Sleep, 250
    search_string := StrReplace(Clipboard, A_Space, "+")
    RunWait, %Browser% https://en.wikipedia.org?search=%search_string%
return
;/////////////////////////////////////////////////
