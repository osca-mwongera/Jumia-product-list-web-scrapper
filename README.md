# Jumia-product-list-web-scrapper
A script that gets products on jumia's website and returns them in a csv format.

# Running the script on your computer
1. Create a virtual environment and activate it<br/><br/>
    `python3 -m venv "name_of_your_virtual_environment"`
<br /><br />
 
2. Install the script's dependencies <br/><br/>
    `pip3 install -r requirements.txt`
<br /><br />
 
3. Run the script <br/><br/>
    `python3 jumia_products_scrapper.py`
    <br/><br/>
    Once done a message `Done executing function` will be logged on the console
<br /><br />

# Technologies
* **requests** - Python requests library is used to make HTTP calls in this case to fetch data 
<br/><br/>
* **beautiful-soup (v4)** - for  scrapping the data from the HTTP response
<br/><br/>
* **pandas** - Used to export the data to a csv format