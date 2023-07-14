import streamlit as st
import pandas as pd

def load_data(file):
    if file.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.endswith(('.xls', '.xlsx')):
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

        # Perform your EDA here
        # You can use Streamlit widgets and plot your visualizations using libraries like matplotlib or seaborn

        # Example: Display summary statistics
        st.subheader("Summary Statistics")
        st.write(data.describe())

if __name__ == '__main__':
    main()
