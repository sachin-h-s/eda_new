import pandas as pd
import streamlit as st
import pandas_profiling


def load_data(file):
    file_extension = file.name.split(".")[-1]

    if file_extension == "csv":
        return pd.read_csv(file)
    elif file_extension == "xlsx":
        return pd.read_excel(file)
    elif file_extension == "txt":
        return pd.read_csv(file, delimiter="\t")
    else:
        return None


def main():
    st.title("Exploratory Data Analysis App")

    # Data loading options
    data_source = st.sidebar.selectbox("Select Data Source", ["CSV", "XLSX", "TXT"])

    if data_source == "CSV":
        file = st.file_uploader("Upload CSV file", type=["csv"])
    elif data_source == "XLSX":
        file = st.file_uploader("Upload XLSX file", type=["xlsx"])
    elif data_source == "TXT":
        file = st.file_uploader("Upload TXT file", type=["txt"])
    else:
        file = None

    if file is not None:
        df = load_data(file)

        if df is not None:
            st.subheader("Preview of the Dataset")
            st.dataframe(df.head())

            if st.button("Generate Report"):
                profile = pandas_profiling.ProfileReport(df)
                st_profile_report(profile)


if __name__ == "__main__":
    main()
