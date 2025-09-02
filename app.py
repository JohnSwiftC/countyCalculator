from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from county import CountyCalc

calc = CountyCalc("data-xQ5ws.csv")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static/templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={}
    )


@app.get("/rate")
async def get_rate(request: Request, county=""):

    result = calc.get_county_rate(county, pretty=True)

    result = str("%.2f" % round(result, 2)) + "%"

    return templates.TemplateResponse(
        request=request, name="answer.html", context={"answer": result, "title": "Rate for " + county}
    )


@app.get("/calculate_cost")
async def get_cost(request: Request, taxable: float = 0.0, county=""):

    result = calc.get_cost_for_county(taxable, county)

    result = "$" + str("%.2f" % round(result, 2))

    details = {"Taxable Amount": "$" + str("%.2f" % round(taxable, 2))}

    return templates.TemplateResponse(
        request=request, name="answer.html", context={"answer": result, "title": "Cost in " + county, "details": details}
    )

@app.get("/most_expensive")
async def get_most_expensive(request: Request, n: int = 1):

    result = calc.get_nth_highest_rate(n)

    details = {}

    for (i, row) in result.iterrows():
        details[row['name']] = str("%.2f" % round(row['effective_prop_tax_rate_23'] * 100, 2)) + "%"

    return templates.TemplateResponse(
        request=request, name="answer.html", context={"title": "Most Expensive Counties", "details": details}
    )