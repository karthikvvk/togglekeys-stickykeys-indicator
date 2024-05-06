# togglekeys-stickykeys-indicator

Initial status of the capslock and numlock is obtained using win32api.
It uses the pynput library to listen to the keystrokes.
Note:
    Due to listening to keystrokes, this application may FLAGGED as MALWARE.
    So in order to use it PLEASE add the APPLICATION in the EXCLUSION list in antivirus.
    ->cmd command to do so(RUN CMD AS ADMINISTRATOR): 
        powershell -Command Add-MpPreference -ExclusionProcess "REPLACE_THIS_WITH_ABSOLUTE_PATH_TO_THIS_APPLICATION"
