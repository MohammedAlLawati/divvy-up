import streamlit as st
import pandas as pd

st.title("💸 Bill Splitter")

# Session state to hold contributors
if "contributors" not in st.session_state:
    st.session_state.contributors = []

# --- Input Form ---
with st.form("contributor_form"):
    name = st.text_input("Name")
    amount = st.number_input("Contribution", min_value=0.0, step=0.01)
    submitted = st.form_submit_button("Add Contributor")
    if submitted and name:
        st.session_state.contributors.append({"Name": name, "Contribution": amount})

# --- Display Contributions ---
if st.session_state.contributors:
    df = pd.DataFrame(st.session_state.contributors)
    st.write("### Current Contributions")
    st.dataframe(df)

    # --- Core Calculation ---
    total = df["Contribution"].sum()
    avg = total / len(df)

    df["Balance"] = df["Contribution"] - avg
    df["Status"] = df["Balance"].apply(
        lambda x: "Owes" if x < 0 else "Is Owed" if x > 0 else "Settled"
    )

    # --- Show Result ---
    st.write("### Settlement")
    st.dataframe(df[["Name", "Contribution", "Balance", "Status"]])

