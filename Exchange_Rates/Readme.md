XE Currency Data Extractor - Python

XE.com Inc. is the World's Trusted Currency Authority. This project provides an interface with the XE Currency Data (XECD) product.

XE Currency Data is a REST API that gives access to daily or live rates and mid-market conversion rates between all supported currencies.

An account ID and API key are needed to access the API. This can be gotten through a 7-day free trial account or full account.

This script runs effectively in a Python3 environment.

Installation 

1. Create a Python3 virtual environment
    python3 -m venv venv

2. Activate the virtual environment using the following command:
    venv/Scripts/activate.bat

3. Install the libraries from the Requirements file:

    pip install -r requirements.txt


4. Make sure to supply the Account ID and API key values to the config.py file. Also, the currencies can be changed as required.

5. Run 'python app.py' in the terminal.

