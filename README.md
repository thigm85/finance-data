# finance-data
Obtain and manage available financial data.

# Get current price

* **Definition of current price**: Closing price of the asset at the previous business day. In case this is not 
available, it will be the closing price on the previous business day, and so on.
* **Design choices**:
  * *Meaningful verbose option*: Possible to understand what hapenned internally using human-readable format.
  * *Database connection*: Possible to specify database connection to manage historical data and avoid unnecessary
     replication of work.
  * *Human-readable config file*: For each asset, the parameters necessary to obtain financial data from a specific source will be defined in configuration file exposed to the user.

# External API

A python script that will write to standard output a tab-separated table containing one row for each requested asset and 
three columns: (asset name, date, price)

Usage example:

```bash
PATH=$BUILD_DIR:$PATH PYTHONPATH=$BUILD_DIR:$PYTHONPATH get_current_data.py -i $INPUT_FILE > $OUTPUT_FILE
``` 
where
* BUILD_DIR: contains the directory where this library is built.
* INPUT_FILE: Text file containing allowed asset code names that you want to retrieve info.
* OUTPUT_FILE: Text file that you want the result to be stored into.