echo "Setting up the Application"

if not exist .venv\ (
    python -m venv .venv
)

if  exist requirements.txt (
    .\.venv\Scripts\python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
    cls
    echo "Local Installation Successfull. Now you can double-click on doc-processing-app.py to run application directly."
    echo :
    echo :
    echo :
    echo :
    echo :
    echo "CTRL+C to exit.";
    powershell -nop -c "& {sleep 15}";

    exit 0
)
else (
    echo "Requirements.txt not found";
    echo "Aborting installation. Exiting in 5 Seconds";
    powershell -nop -c "& {sleep 5}";
    exit 1
)
