pyinstaller -F .\main.py -i .\Image\Icon.ico 
del .\*.spec
copy .\dist\* .\
rd /s /q .\dist
rd /s /q .\build
rd /s /q ..\__pycache__