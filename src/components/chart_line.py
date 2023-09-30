from typing import Sequence

import streamlit as st
from pandas import DataFrame
import numpy as np
from data.dfunc import get_datetime_columns_of_data_frame


def simple(
    df: DataFrame,
    date_field: str = "dob",
    value_field: str | None = "amount",
    dimension: str | None = None,
) -> None:
    
    # if the date_field doesn't exist, find the first date field
    if date_field not in df.columns:
        date_fields = get_datetime_columns_of_data_frame(df)
        if len(date_fields) == 0:
            st.error("No date field found")
            return
        date_field = date_fields[0]

    spec = {
        "mark": {"type": "line", "tooltip": True},
        "encoding": {
            "x": {"field": date_field, "type": "temporal", "timeUnit": "yearmonthdate"},
            "y": {"field": value_field, "type": "quantitative"},
        },
    }
    if dimension is not None and dimension in df.columns:
        spec["encoding"]["color"] = {"field": dimension, "type": "nominal"}
        # group by dimension and date_field
        df = df.groupby([date_field, dimension])[value_field].sum().reset_index()
    if dimension is None:
        # group by date_field
        df = df.groupby(date_field)[value_field].sum().reset_index()

    st.vega_lite_chart(df, spec, use_container_width=True, theme="streamlit")
