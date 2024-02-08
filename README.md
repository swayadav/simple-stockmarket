# simple-stockmarket

To Clone the Repo:
    -At any accessible windows path open a cmd & run "git clone https://github.com/swayadav/simple-stockmarket"

Follow below steps after cloning the Repo on your machine:

1) Make sure python is installed on your system.
    
    If it's not already Installed
    -Follow: https://www.digitalocean.com/community/tutorials/install-python-windows-10
    To get it Installed

2) After Installation:

    -Route to "/simple-stockmarket/" path where the project is cloned.
    -Open a cmd on path "/simple-stockmarket/.
    -Execute command "python -m venv virtualenv" to create a virtual environment.
    -You will see a virtualenv folder at path "/simple-stockmarket/" once the virtual environment is created.
    -Type "virtualenv\Scripts\activate" & hit Enter to activate the virtual environment.
    -Execute: "pip install -r requirements.txt" on cmd to install all the required packages.

    -You are good to Run the project now!!!

    -Route inside "/code/" folder.
    -Run "python stocks_ui.py" on cmd
    * This will launch a "Stock Market Trade" GUI


3) Run the Use-cases:

    1)BUY/SEL Trade:
        - Select the Stock Symbol from the drop down you want to Trade in
        - Enter the Input Price(Total Amount to Invest)
        - Select the Operation "Trade" from the Dropdown
        - Select BUY/SELL Trade from the Dropdown.
        - Hit Execute
            - For Buy, Trade gets executed for 100 Rs each share price for provided Amount to Invest.
            - For Sell, Trade gets executed preassuming the user holds 1000 Shres of the provided Stock Symbol.

    2)Dividend Yeild:
        - Select the Stock Symbol from the drop down you want get the dividend yeild for.
        - Enter the Input Price.
        - Select the Operation "Dividend Yeild" from the Dropdown
        - **NO ACTION on BUY/SELL**
        - Hit Execute

    2)P/E Ratio:
        - Select the Stock Symbol from the drop down you want get the P/E Ratio for.
        - Enter the Input Price.
        - Select the Operation "P/E Ratio" from the Dropdown
        - **NO ACTION on BUY/SELL**
        - Hit Execute


    

    
        




