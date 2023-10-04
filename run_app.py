#! .\.venv\Scripts\python
from time import sleep

try :
    from mainapp import create_app
    create_app().run(debug=True)
    print("Starting")
except ImportError as i :
    print("Import Error :",i)
    print("Please double-click and run the script -> install_app.bat. Exiting in 5 seconds...")
    sleep(5)
except Exception() as e :
    print("Uncaught Exception :",e,"Exiting in 5 seconds...")
    sleep(5)

