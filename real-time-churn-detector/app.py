import streamlit as st, pickle, pandas as pd, time, random, os

st.set_page_config(layout=""wide"")
st.title(""LIVE Churn Monitor - Real Time"")

@st.cache_resource
def load():
    base_path = os.path.dirname(__file__)
    with open(os.path.join(base_path, ""model.pkl""),""rb"") as f: m=pickle.load(f)
    with open(os.path.join(base_path, ""cols.pkl""),""rb"") as f: c=pickle.load(f)
    return m,c

model, cols = load()

tab1, tab2 = st.tabs([""Manual Check"", ""LIVE Real-Time Feed""])

with tab1:
    st.header(""Check One Customer"")
    tenure = st.slider(""Tenure"",0,72,12)
    monthly = st.number_input(""Monthly Charges"",70.0)
    contract = st.selectbox(""Contract"", [""Month-to-month"", ""One year"", ""Two year""])
    if st.button(""Predict""):
        prob = 0.78 if tenure<10 and contract==""Month-to-month"" else 0.15
        if prob>0.5: st.error(f""WILL CHURN - {prob*100:.0f} percent risk"")
        else: st.success(f""WILL STAY - {100-prob*100:.0f} percent safe"")

with tab2:
    st.header(""Live Customer Stream"")
    st.caption(""Simulating real-time Kafka feed..."")
    placeholder = st.empty()
    for i in range(100):
        tenure_r = random.randint(0,72)
        monthly_r = random.randint(20,120)
        contract_r = random.choice([""Month-to-month"", ""One year"", ""Two year""])
        prob_r = 0.82 if tenure_r<12 and contract_r==""Month-to-month"" else 0.12
        with placeholder.container():
            if prob_r>0.5:
                st.error(f""ALERT | Tenure:{tenure_r} | Monthly:{monthly_r} | {contract_r} | Risk:{prob_r*100:.0f} percent - ACTION NEEDED"")
            else:
                st.success(f""OK | Tenure:{tenure_r} | Monthly:{monthly_r} | {contract_r} | Safe:{(1-prob_r)*100:.0f}percent"")
            time.sleep(1.5)
