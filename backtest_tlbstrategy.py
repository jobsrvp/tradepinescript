import pandas as pd
import numpy as np
import yfinance as yf

# ==============================
# PARAMETERS
# ==============================
symbols = ['NYKAA.NS']  # Add more symbols
pivot_lookback = 14
atr_length = 14
multiplier = 1

all_trades = []

# ==============================
# STRATEGY FUNCTION
# ==============================
def run_strategy(symbol):

    print(f"\nRunning for {symbol}...")

    df = yf.download(symbol, period="max", interval="1wk", auto_adjust=True)

    if df.empty:
        print("No data.")
        return []

    # ---- FIX MultiIndex columns ----
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.dropna(subset=["Open","High","Low","Close"])

    # ==============================
    # ATR CALCULATION
    # ==============================
    df["H-L"] = df["High"] - df["Low"]
    df["H-PC"] = abs(df["High"] - df["Close"].shift(1))
    df["L-PC"] = abs(df["Low"] - df["Close"].shift(1))
    df["TR"] = df[["H-L","H-PC","L-PC"]].max(axis=1)
    df["ATR"] = df["TR"].rolling(atr_length).mean()

    # ==============================
    # EMA
    # ==============================
    df["EMA14"] = df["Close"].ewm(span=14, adjust=False).mean()

    # ==============================
    # PIVOT HIGH DETECTION
    # ==============================
    pivot_indices = []

    for i in range(pivot_lookback, len(df) - pivot_lookback):
        current_high = float(df["High"].iloc[i])
        left = df["High"].iloc[i - pivot_lookback:i].values
        right = df["High"].iloc[i + 1:i + pivot_lookback + 1].values

        if current_high > left.max() and current_high > right.max():
            pivot_indices.append(i)

    trades = []
    in_position = False
    waiting_for_confirmation = False
    reference_close = None
    entry_price = None
    entry_date = None

    # ==============================
    # MAIN LOOP
    # ==============================
    for p in pivot_indices:

        if in_position:
            break

        pivot_price = df["High"].iloc[p]
        pivot_date = df.index[p]

        # Skip if ATR not ready
        if pd.isna(df["ATR"].iloc[p]):
            continue

        slope = df["ATR"].iloc[p] / (atr_length * multiplier)

        # ---------------- ENTRY LOOP ----------------
        for i in range(p + 1, len(df) - 2):

            row = df.iloc[i]
            next_row = df.iloc[i + 1]

            trendline_value = pivot_price - (i - p) * slope

            if not in_position and row["Close"] > trendline_value:

                entry_price = next_row["Open"]
                entry_date = next_row.name
                in_position = True
                waiting_for_confirmation = False
                break

        # ---------------- EXIT LOOP ----------------
        if in_position:

            for j in range(i + 1, len(df) - 2):

                row = df.iloc[j]
                next_row = df.iloc[j + 1]

                # Confirmation step
                if waiting_for_confirmation:

                    if row["Close"] < reference_close:

                        exit_price = next_row["Open"]
                        exit_date = next_row.name

                        trades.append({
                            "Symbol": symbol,
                            "Pivot Date": pivot_date,
                            "Pivot High": round(pivot_price, 2),
                            "Slope": round(slope, 4),
                            "Entry Date": entry_date,
                            "Entry Price": round(entry_price, 2),
                            "Exit Date": exit_date,
                            "Exit Price": round(exit_price, 2),
                            "Return %": round((exit_price / entry_price - 1) * 100, 2),
                            "Status": "CLOSED"
                        })

                        in_position = False
                        waiting_for_confirmation = False
                        break
                    else:
                        waiting_for_confirmation = False

                # Detect EMA weakness
                elif row["Close"] < row["EMA14"]:
                    reference_close = row["Close"]
                    waiting_for_confirmation = True

            # If still open after exit loop, break outer loop
            if in_position:
                break

    # ==============================
    # CAPTURE OPEN TRADE
    # ==============================
    if in_position:

        last_row = df.iloc[-1]

        trades.append({
            "Symbol": symbol,
            "Pivot Date": pivot_date,
            "Pivot High": round(pivot_price, 2),
            "Slope": round(slope, 4),
            "Entry Date": entry_date,
            "Entry Price": round(entry_price, 2),
            "Exit Date": last_row.name,
            "Exit Price": round(last_row["Close"], 2),
            "Return %": round((last_row["Close"] / entry_price - 1) * 100, 2),
            "Status": "OPEN"
        })

    return trades


# ==============================
# RUN FOR ALL SYMBOLS
# ==============================
for sym in symbols:
    trades = run_strategy(sym)
    all_trades.extend(trades)

# ==============================
# EXPORT RESULTS
# ==============================
trades_df = pd.DataFrame(all_trades)

print("\n======================")
print("ALL TRADES")
print("======================\n")
print(trades_df)

if not trades_df.empty:
    trades_df.to_excel("trendline_breakout_trades.xlsx", index=False)
    print("\nExcel file saved as trendline_breakout_trades.xlsx")
else:
    print("\nNo trades generated.")
