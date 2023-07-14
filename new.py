import streamlit as st
import pandas as pd
import pandas_profiling as pp

def load_data(file):
    if file.name.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        data = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")
    return data

def main():
    st.title("Exploratory Data Analysis")
    st.sidebar.title("File Upload")

    file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xls", "xlsx"])
    if file is not None:
        data = load_data(file)
        st.success(f"File '{file.name}' successfully loaded!")

        st.subheader("Data Preview")
        st.dataframe(data.head())

        # Generate pandas profiling report
        profile = pp.ProfileReport(data)

        # Display the report using Streamlit
        st.subheader("Pandas Profiling Report")
        st.write(profile.to_html(), unsafe_allow_html=True)

        # Perform additional EDA and visualizations if needed

if __name__ == '__main__':
    main()
