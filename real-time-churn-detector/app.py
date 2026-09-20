import streamlit as st

st.set_page_config(page_title="Churn Detector")

st.title("Customer Churn Prediction")
st.write("Enter details and click Predict")

# Inputs
tenure = st.slider("Tenure", 0, 72, 24)
monthly = st.number_input("Monthly Charges", 20, 150, 65)
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer"])

if st.button("Predict"):
    st.subheader("Result:")

    if contract == "Month-to-month" and tenure < 12:
        st.error("Customer WILL CHURN")
        st.write("Churn Probability is 85 percent")
        st.write("Reason: New customer with month to month contract")

    elif monthly > 80 and tenure < 24:
        st.warning("Customer MIGHT CHURN")
        st.write("Churn Probability is 60 percent")
        st.write("Reason: High monthly charges")

    else:
        st.success("Customer WILL NOT CHURN")
        st.write("Churn Probability is 15 percent")
        st.write("Reason: Loyal customer")
