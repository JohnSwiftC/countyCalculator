import pandas as pd

class CountyCalc:
    def __init__(self, csv: str):
        data_frame = pd.read_csv(csv)
        self.data = data_frame
        self.data.columns = [column.replace(" ", "_") for column in self.data.columns]
        self.data.columns = [column.replace(",", "") for column in self.data.columns]
    
    def get_county_info(self, county: str):
        result = self.data.query('name == ' + county, inplace=False)
        return result


calculator = CountyCalc("data-xQ5ws.csv")

row = calculator.get_county_info("Polk_County_Iowa")

print(row)