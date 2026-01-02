import streamlit as st

from constant import CURRENCIES
from currency_convertor import convert_currency, get_exchange_rate

st.title("💰 Currency Convertor")
st.write(
    "This tool converts amounts between different currencies 🌍.\
          Enter the amounts and choose the currencies to see the results."
)


base_currency = st.selectbox("From currency (base):", CURRENCIES)
target_currency = st.selectbox("to currency (target):", CURRENCIES)
amounts = st.number_input("Amount to Convert:")

if amounts and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        target_amount = convert_currency(amounts, exchange_rate)
        st.success(f"Exchange Rate: {exchange_rate:.2f}")

        col1, col2, col3 = st.columns(3)

        col1.metric("Base Currency", f"{amounts} {base_currency}")
        col2.markdown("## ->")
        col3.metric("Target Currency", f"{target_amount:.2f} {target_currency}")

    else:
        st.error("Error fetching exchange rate. Please try again later.")

st.divider()

st.markdown("""
### About this Tool:
This currency converter app allows you to convert amounts between different currencies using real-time exchange rates fetched from an external API. Simply select the base and target currencies, enter the amount you wish to convert, and the app will display the converted amount along with the current exchange rate.
""")
