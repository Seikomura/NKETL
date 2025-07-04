import streamlit as st
from pymongo import MongoClient
import tempfile, os
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION, TARGET_HEADERS
from etl_core import extract_tables_from_pdf

st.title("PDF Table ETL to MongoDB")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.info("Extracting table data...")
    extracted = extract_tables_from_pdf(temp_path, TARGET_HEADERS)
    st.success(f"Extracted {len(extracted)} rows.")

    if extracted:
        client = MongoClient(MONGO_URI)
        col = client[MONGO_DB][MONGO_COLLECTION]
        col.insert_many(extracted)
        st.success(f"Inserted {len(extracted)} records into MongoDB.")
        st.write(extracted[:5])  # preview

    # Clean up temp file
    os.remove(temp_path)
