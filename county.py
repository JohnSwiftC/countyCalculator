import pandas as pd
import math

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
        val = self.get_county_info(
            county)['effective_prop_tax_rate_23'].iloc[0]

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

    def get_average_per_state(self):
        states = {}

        for (i, row) in self.data.iterrows():
            name_split = row['name'].split(", ")
            name = name_split[-1]
            if name in states:
                try:
                    states[name].update(float(row['effective_prop_tax_rate_23']))
                except ValueError:
                    pass
            else:
                states[name] = RollingAvg()

                try:
                    states[name].update(float(row['effective_prop_tax_rate_23']))
                except ValueError:
                    pass

        ret = {}

        i = 0
        for k, v in states.items():
            avg = v.get_avg()
            if not math.isnan(avg):
                ret[k] = avg
            else:
                ret[k] = 0.0
            i = i + 1

        print(i)
        return ret

class RollingAvg:
    def __init__(self):
        self.val = 0
        self.count = 0
    
    def update(self, val):
        self.count = self.count + 1
        self.val = self.val + val
    
    def get_avg(self):
        return self.val / self.count

def main():

    calculator = CountyCalc("data-xQ5ws.csv")
    avgs = calculator.get_average_per_state()

    print(avgs)

if __name__ == '__main__':
    main()
