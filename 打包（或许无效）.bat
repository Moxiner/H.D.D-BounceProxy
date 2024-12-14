pyinstaller -F .\main.py -i .\Image\Icon.ico --exclude-module PyQt5 --add-binary="C:\Users\Moxiner\AppData\Local\Programs\Python\Python38\Lib\site-packages\vgamepad\win\vigem\client\x64\ViGEmClient.dll;vgamepad\win\vigem\client\x64"
mkdir .\dist
mkdir .\dist\Sound\
mkdir .\dist\Font\
mkdir .\dist\Image\
mkdir .\dist\ZZZSoundTrigger\
del .\*.spec
copy .\Sound .\dist\Sound\*
copy .\Image .\dist\Image\*
copy .\Font .\dist\Font\*
copy .\config.ini .\dist\
copy ZZZSoundTrigger\sample.wav .\dist\ZZZSoundTrigger\*
rd /s /q .\build
rd /s /q ..\__pycache__
