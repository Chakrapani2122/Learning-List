import streamlit as st
import nbformat
from nbconvert import HTMLExporter

# Set the title of the browser tab
st.set_page_config(page_title="Learning Library")

# List of Jupyter notebooks in the current directory
notebooks = [
    "Big_Data_Analytics.ipynb",
    "DBMS_SQL.ipynb",
    "DBMS.ipynb",
    "Mac_Keyboard_Shortcuts.ipynb",
    "Machine_Learning.ipynb",
    "Python_Programming.ipynb",
    "R_Programming.ipynb",
    "SQL.ipynb"
]

# Sidebar for navigation
st.sidebar.title("Jupyter Notebooks")
selected_notebook = st.sidebar.radio("Select a notebook", notebooks)

# Display the selected notebook
st.title(f"{selected_notebook}")

try:
    with open(selected_notebook, "r", encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)

    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook_content)

    st.components.v1.html(body, height=800, scrolling=True)
except Exception as e:
    st.error(f"Error loading notebook: {e}")