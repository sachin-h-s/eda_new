import numpy as np
import pandas as pd
import pandas_profiling
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Function to load data from a CSV file
@st.cache
def load_csv(file):
	return pd.read_csv(file)

#Function to load data from an XLSX file
@st.cache
def load_xlsx(file):
	return pd.read_excel(file)

#Function to load data from a SQL database
@st.cache
def load_sql(query, con):
	return pd.read_sql(query, con)

#Function to generate a pandas profiling report
def ProfileReport(df):
	return pandas_profiling.ProfileReport(df)

#Main function

def main():
	st.title("Exploratory Data Analysis App")


# Select data source
data_source = st.sidebar.selectbox("Select Data Source", ["CSV", "XLSX", "SQL"])

# Load data
if data_source == "CSV":
    file = st.file_uploader("Upload CSV file", type="csv")
    if file is not None:
        df = load_csv(file)
elif data_source == "XLSX":
    file = st.file_uploader("Upload XLSX file", type="xlsx")
    if file is not None:
        df = load_xlsx(file)
elif data_source == "SQL":
    query = st.text_input("SQL Query")
    con = st.text_input("SQL Connection String")
    if query and con:
        df = load_sql(query, con)
# Generate report
if "df" in locals():
	if st.button("Generate report"):
		report = ProfileReport(df, explorative=True)
		st_profile_report(report)
		st.write(report)
	
	
if __name__=='__main__':
    main()
