import streamlit as st

from st_clipboard import copy_to_clipboard, copy_to_clipboard_unsecured


# Create two columns: HTTPS (left), HTTP (right)
col_https, col_http = st.columns(2)

with col_https:
    st.markdown("### HTTPS Clipboard Copy")
    https_text = st.text_input("Enter text to copy (HTTPS):", value="Hello HTTPS")
    if st.button("Copy to clipboard (HTTPS)"):
        copy_to_clipboard(https_text)
        st.success("Copied to clipboard using secure method!")

with col_http:
    st.markdown("### HTTP Clipboard Copy")
    http_text = st.text_input("Enter text to copy (HTTP):", value="Hello HTTP")
    if st.button("Copy to clipboard (HTTP)"):
        copy_to_clipboard_unsecured(http_text)
        st.success("Copied to clipboard using unsecured method!")
