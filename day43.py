# Vitual Enviroment

import pandas as pd
print(pd.__version__)

# Create a virtual enviroment
python -m venv myenv

# Activate the virtual enviroment (Linux/macos)
source myenv/bin/activate

#Activate the virtual enviroment (Window`s)
myenv\Scripts\activate.bat

# Deactivate the virtual enviroment
deactivate

#The "requirements.txt" file

# Output the list of intalled package and their version in a file
pip freeze > requirements.txt

# install the package listed in the requirements.txt file
pip install -r requirements.txt