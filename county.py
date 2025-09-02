import pandas as pd

class CountyCalc:
    def __init__(self, csv: str):
        data_frame = pd.read_csv(csv)
        self.data = data_frame
    
    def get_county_info(self, county: str):
        return self.data.loc[self.data['name'] == county]
    
    def show_data(self):
        print(self.data)


calculator = CountyCalc("data-xQ5ws.csv")

print(calculator.get_county_info("Polk County, Iowa")['effective_prop_tax_rate_23'])

