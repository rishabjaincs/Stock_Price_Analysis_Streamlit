import streamlit as st
import yfinance as yf
import datetime
st.write("""
         # Stock Price Analyzer
         """)



symbol = st.selectbox('Select Stock Symbol',('AAPL','GOOG','TSLA','MSFT','NFLX'))

date_col1,date_col2 = st.columns(2)

with date_col1:
    start_date = st.date_input("Please Enter the Start Date",datetime.date(2019,1,1))
with date_col2:
    end_date = st.date_input("Please Enter the End Date",datetime.date(2019,12,31))


ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period='1d',start=start_date,end=end_date)

st.write(f"""### {symbol} Stock Price Data""")

st.dataframe(ticker_df)

st.write(f"""### {symbol} Closing Price Chart""")

st.line_chart(ticker_df['Close'].round(2))

st.write(f"""### {symbol} Opening Price Chart""")

st.line_chart(ticker_df['Open'].round(2))

st.write(f"""### {symbol} Volume Chart""")

st.line_chart(ticker_df['Volume'].round(2))
