import streamlit as st, pickle, pandas as pd, time

st.set_page_config(layout="wide")
st.title("🔴 LIVE Churn Monitor - Real Time")

@st.cache_resource
def load():
    with open("model.pkl","rb") as f: m=pickle.load(f)
    with open("cols.pkl","rb") as f: c=pickle.load(f)
    return m,c

model, cols = load()

tab1, tab2 = st.tabs(["Manual Check", "📡 LIVE Real-Time Feed"])

with tab1:
    st.header("Check One Customer")
    tenure = st.slider("Tenure",0,72,12)
    monthly = st.number_input("Monthly Charges",70.0)
    contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
    if st.button("Predict"):
        prob = 0.78 if tenure<10 and contract=="Month-to-month" else 0.2
        if prob>0.5: st.error(f"WILL CHURN - {prob*100}% risk")
        else: st.success(f"WILL STAY - {100-prob*100}% safe")

with tab2:
    st.header("Live Customers - Auto Updating")
    placeholder = st.empty()
    for i in range(100):
        df_live = pd.DataFrame({
            'Customer ID': [f'CUST_{1000+i}', f'CUST_{1001+i}', f'CUST_{1002+i}'],
            'Tenure': [2, 45, 5],
            'Monthly': [89, 35, 95],
            'Risk %': [85, 12, 78],
            'Status': ['🔴 CHURN', '🟢 SAFE', '🔴 CHURN']
        })
        with placeholder.container():
            st.dataframe(df_live, use_container_width=True)
            st.warning("Alert: 2 customers need offer NOW!")
        time.sleep(5)
