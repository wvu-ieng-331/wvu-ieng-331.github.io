import marimo

__generated_with = "0.11.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import plotly.express as px
    import polars as pl
    import polars.selectors as cs
    return cs, mo, pl, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""1. Does it matter what order you used DataFrame.fi<er()DataFrame.filter() and DataFrame.sort()DataFrame.sort() if you’re using both? Why/why not? Think about the results and how much work the functions would have to do.""")
    return


@app.cell
def _(mo):
    mo.md(r"""Yes. If you use DataFrame.fi<er()DataFrame.filter() before DataFrame.sort()DataFrame.sort(), there will be less rows for sort()sort() to work with, which is more efficient.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""2. What happens if you specify the name of the same variable multiple times in a DataFrame.se≤ct()DataFrame.select() call?""")
    return


@app.cell
def _(pl):
    penguins = pl.read_csv(r"learning-modules\data\penguins.csv")
    penguins

    penguins.select("species", "island", "island")
    return (penguins,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""3. Using the pengu∈spenguins dataset, make a scatter plot of billdepthmmbill_depth_mm vs. bill≤n>hmmbill_length_mm. That is, make a scatter plot with billdepthmmbill_depth_mm on the y-axis and bill≤n>hmmbill_length_mm on the x-axis. Describe the relationship between these two variables.""")
    return


@app.cell
def _(penguins, px):
    px.scatter(
        penguins,
        x="bill_length_mm",
        y="bill_depth_mm"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""4. From the flightsflights dataset, compare deptimedep_time, scheddeptimesched_dep_time, and dep∂aydep_delay. How would you expect those three numbers to be related?""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        5. In a single pipeline for each condition, find all flights that meet the condition:

            - Had an arrival delay of two or more hours
            - Flew to Houston (IAH or HOU)
            - Were operated by United, American, or Delta
            - Departed in summer (July, August, and September)
            - Arrived more than two hours late but didn’t leave late
            - Were delayed by at least an hour, but made up over 30 minutes in flight
        """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""6. Find the flights that are most delayed upon departure from each destination.""")
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""7. How do delays vary over the course of the day? Illustrate your answer with a plot.""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
