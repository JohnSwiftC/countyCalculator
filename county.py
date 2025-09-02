import pandas as pd

class CountyCalc:
    def __init__(self, csv: str):
        data_frame = pd.read_csv(csv)
        self.data = data_frame
    
    def get_county_info(self, county: str):
        return self.data.loc[self.data['name'] == county]
    
    def get_county_rate(self, county: str, pretty=False):
        val = self.get_county_info(county)['effective_prop_tax_rate_23']

        if pretty:
            val = val * 100

        return val
    
    def get_cost_for_county(self, taxable_amount, county):
        return self.get_county_rate(county) * taxable_amount
    
    def show_data(self):
        print(self.data)


calculator = CountyCalc("data-xQ5ws.csv")

print(calculator.get_cost_for_county(100000, "Polk County, Iowa"))
