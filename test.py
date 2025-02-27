import polars as pl
import polars.selectors as cs
import plotly.express as px

who2 = pl.read_csv("data/who2.csv", null_values="")

(
    who2.unpivot(
        index=["country", "year"], 
        variable_name="key", 
        value_name="count"
    )
    .with_columns(
        key=pl.col("key")
        .str.split("_")
        .list.to_struct()
        .struct.rename_fields(["diagnosis", "gender", "age"])
    )
    .unnest("key")
)
