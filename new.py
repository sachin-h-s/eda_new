import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import base64

def download_link(object_to_download, download_filename, download_link_text):
    """
    Helper function to generate download links for generated reports.
    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    b64 = base64.b64encode(object_to_download.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'
    return href

def main():
    st.title("Pandas Profiling App")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the file
        df = pd.read_csv(uploaded_file)

        # Generate the pandas profiling report
        profile = ProfileReport(df, explorative=True)

        # Display the report using Streamlit
        st.write(profile.to_html(), unsafe_allow_html=True)

        # Download link for the report
        st.markdown(download_link(profile.to_file("report.html"), "report.html", "Download Report"), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
