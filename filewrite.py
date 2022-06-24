# THIS MODULE WRITE THE DATA INTO A CSV FILE. PANDAS LIBRARY IS USED .

import pandas


class FileWrite():
    def __init__(self):
        pass
        # self.write_file()

# TODO DATAFRAME OBJECT OF PANDAS MODULE IS USED TO LOAD DATA INTO A CSV FILE
    def write_file_firsttime(self, data):
        data_load = pandas.DataFrame(data)
        data_load.to_csv('variance.csv', header=False, index=False, mode='w')

    def write_file(self, data):
        data_load = pandas.DataFrame(data)
        data_load.to_csv('variance.csv', header=False, index=False, mode='a')
