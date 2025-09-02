import pandas as pd

class CountyCalc:
    def __init__(self, csv: str):
        data_frame = pd.read_csv(csv)
        self.data = data_frame
        self.data["name"] = self.data["name"].str.lower()

    # Always use for getting the county row, applies input sanitization
    def get_county_info(self, county: str):
        county = county.lower()
        return self.data.loc[self.data['name'] == county]
    
    def get_county_rate(self, county: str, pretty=False):
        val = self.get_county_info(county)['effective_prop_tax_rate_23'].iloc[0]

        if pretty:
            val = val * 100

        return val
    
    def get_cost_for_county(self, taxable_amount, county):
        return self.get_county_rate(county) * taxable_amount
    
    def get_nth_highest_rate(self, n):
        return self.data.sort_values('effective_prop_tax_rate_23', ascending=False).head(n)

    def get_nth_lowest_rate(self, n):
        return self.data.sort_values('effective_prop_tax_rate_23', ascending=True).head(n)

    def show_data(self):
        print(self.data)

calculator = CountyCalc("data-xQ5ws.csv")

print(calculator.get_cost_for_county(100000, "pOLk coUnty, iOwa"))
print(calculator.get_nth_highest_rate(1))
