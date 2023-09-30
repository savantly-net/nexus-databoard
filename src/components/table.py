import streamlit as st

import streamlit as st

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

def show_download_csv_button(df, name: str ):
    csv = convert_df(df)
    if name == '':
        name = 'Data'
    st.download_button(
        "Download " + name + " CSV",
        csv,
        name.lower() + ".csv",
        "text/csv",
        key=name.lower() + '-csv'
    )

def display(df, name:str = '', show_download_button=True):
    st.write(f"### {name}")
    if show_download_button:
        show_download_csv_button(df, name)
    numRows = df.shape[0]
    height = min(800, (numRows + 1) * 35 + 3)
    st.dataframe(data=df, height=height)