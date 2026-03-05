import pandas as pd
import numpy as np
import yfinance as yf

#symbols = ['FEDERALBNK.NS', 'NYKAA.NS','NAM-INDIA.NS'] # Add your full list
symbols=['360ONE.NS','3MINDIA.NS','ACC.NS','ACMESOLAR.NS','AIAENG.NS','APLAPOLLO.NS','AUBANK.NS','AWL.NS','AADHARHFC.NS',           'AARTIIND.NS','AAVAS.NS','ABBOTINDIA.NS','ACE.NS','ATGL.NS','ABCAPITAL.NS','ABFRL.NS','ABLBL.NS','ABREL.NS','ABSLAMC.NS','AEGISLOG.NS','AEGISVOPAK.NS','AFCONS.NS','AFFLE.NS',           'AJANTPHARM.NS','AKUMS.NS','AKZOINDIA.NS','APLLTD.NS','ALKEM.NS','ALKYLAMINE.NS','ALOKINDS.NS','ARE&M.NS','AMBER.NS','ANANDRATHI.NS','ANANTRAJ.NS','ANGELONE.NS','APARINDS.NS',           'APOLLOTYRE.NS','APTUS.NS','ASAHIINDIA.NS','ASHOKLEY.NS','ASTERDM.NS','ASTRAZEN.NS','ASTRAL.NS','ATHERENERG.NS','ATUL.NS','AUROPHARMA.NS','AIIL.NS','BASF.NS','BEML.NS','BLS.NS',           'BSE.NS','BALKRISIND.NS','BALRAMCHIN.NS','BANDHANBNK.NS','BANKINDIA.NS','MAHABANK.NS','BATAINDIA.NS','BAYERCROP.NS','BERGEPAINT.NS','BDL.NS','BHARATFORG.NS','BHEL.NS',           'BHARTIHEXA.NS','BIKAJI.NS','BIOCON.NS','BSOFT.NS','BLUEDART.NS','BLUEJET.NS','BLUESTARCO.NS','BBTC.NS','FIRSTCR.NS','BRIGADE.NS','MAPMYINDIA.NS','CCL.NS','CESC.NS',           'CRISIL.NS','CAMPUS.NS','CANFINHOME.NS','CAPLIPOINT.NS','CGCL.NS','CARBORUNIV.NS','CASTROLIND.NS','CEATLTD.NS','CENTRALBK.NS','CDSL.NS','CENTURYPLY.NS','CERA.NS','CHALET.NS',           'CHAMBLFERT.NS','CHENNPETRO.NS','CHOICEIN.NS','CHOLAHLDNG.NS','CUB.NS','CLEAN.NS','COCHINSHIP.NS','COFORGE.NS','COHANCE.NS','COLPAL.NS','CAMS.NS','CONCORDBIO.NS','CONCOR.NS',           'COROMANDEL.NS','CRAFTSMAN.NS','CREDITACC.NS','CROMPTON.NS','CUMMINSIND.NS','CYIENT.NS','DCMSHRIRAM.NS','DOMS.NS','DABUR.NS','DALBHARAT.NS','DATAPATTNS.NS','DEEPAKFERT.NS',           'DEEPAKNTR.NS','DELHIVERY.NS','DEVYANI.NS','DIXON.NS','AGARWALEYE.NS','LALPATHLAB.NS','EIDPARRY.NS','EIHOTEL.NS','ELECON.NS','ELGIEQUIP.NS','EMAMILTD.NS','EMCURE.NS','ENDURANCE.NS','ENGINERSIN.NS','ERIS.NS','ESCORTS.NS','EXIDEIND.NS','NYKAA.NS','FEDERALBNK.NS','FACT.NS','FINCABLES.NS','FINPIPE.NS','FSL.NS','FIVESTAR.NS','FORCEMOT.NS','FORTIS.NS','GVT&D.NS','GMRAIRPORT.NS','GRSE.NS','GICRE.NS','GILLETTE.NS','GLAND.NS','GLAXO.NS','GLENMARK.NS','MEDANTA.NS','GODIGIT.NS','GPIL.NS','GODFRYPHLP.NS','GODREJAGRO.NS','GODREJIND.NS','GODREJPROP.NS','GRANULES.NS','GRAPHITE.NS','GRAVITA.NS','GESHIP.NS','FLUOROCHEM.NS','GUJGASLTD.NS','GMDCLTD.NS','GSPL.NS','HEG.NS','HBLENGINE.NS','HDFCAMC.NS','HFCL.NS','HAPPSTMNDS.NS','HEROMOTOCO.NS','HEXT.NS','HSCL.NS','HINDCOPPER.NS','HINDPETRO.NS','POWERINDIA.NS','HOMEFIRST.NS','HONASA.NS','HONAUT.NS','HUDCO.NS','ICICIPRULI.NS','IDBI.NS','IDFCFIRSTB.NS','IFCI.NS','IIFL.NS','INOXINDIA.NS','IRB.NS','IRCON.NS','ITCHOTELS.NS','ITI.NS','INDGN.NS','INDIACEM.NS','INDIAMART.NS','INDIANB.NS','IEX.NS','IOB.NS','IRCTC.NS','IREDA.NS','IGL.NS','INDUSTOWER.NS','INDUSINDBK.NS','INOXWIND.NS','INTELLECT.NS','IGIL.NS','IKS.NS','IPCALAB.NS','JBCHEPHARM.NS','JKCEMENT.NS','JBMA.NS','JKTYRE.NS','JMFINANCIL.NS','JSWCEMENT.NS','JSWINFRA.NS','JPPOWER.NS','J&KBANK.NS','JINDALSAW.NS','JSL.NS','JUBLFOOD.NS','JUBLINGREA.NS','JUBLPHARMA.NS','JWL.NS','JYOTHYLAB.NS','JYOTICNC.NS','KPRMILL.NS','KEI.NS','KPITTECH.NS','KSB.NS','KAJARIACER.NS','KPIL.NS','KALYANKJIL.NS','KARURVYSYA.NS','KAYNES.NS','KEC.NS','KFINTECH.NS','KIRLOSBROS.NS','KIRLOSENG.NS','KIMS.NS','LTF.NS','LTTS.NS','LICHSGFIN.NS','LTFOODS.NS','LATENTVIEW.NS','LAURUSLABS.NS','THELEELA.NS','LEMONTREE.NS','LINDEINDIA.NS','LLOYDSME.NS','LUPIN.NS','MMTC.NS','MRF.NS','MGL.NS','MAHSCOOTER.NS','MAHSEAMLES.NS','M&MFIN.NS','MANAPPURAM.NS','MRPL.NS','MANKIND.NS','MARICO.NS','MFSL.NS','METROPOLIS.NS','MINDACORP.NS','MSUMI.NS','MOTILALOFS.NS','MPHASIS.NS','MCX.NS','MUTHOOTFIN.NS','NATCOPHARM.NS','NBCC.NS','NCC.NS','NHPC.NS','NLCINDIA.NS','NMDC.NS','NSLNISP.NS','NTPCGREEN.NS','NH.NS','NATIONALUM.NS','NAVA.NS','NAVINFLUOR.NS','NETWEB.NS','NEULANDLAB.NS','NEWGEN.NS','NAM-INDIA.NS','NIVABUPA.NS','NUVAMA.NS','NUVOCO.NS','OBEROIRLTY.NS','OIL.NS','OLAELEC.NS','OLECTRA.NS','PAYTM.NS','ONESOURCE.NS','OFSS.NS','POLICYBZR.NS','PCBL.NS','PGEL.NS','PIIND.NS','PNBHOUSING.NS','PTCIL.NS','PVRINOX.NS','PAGEIND.NS','PATANJALI.NS','PERSISTENT.NS','PETRONET.NS','PFIZER.NS','PHOENIXLTD.NS','PPLPHARMA.NS','POLYMED.NS','POLYCAB.NS','POONAWALLA.NS','PRAJIND.NS','PREMIERENE.NS','PRESTIGE.NS','PGHH.NS','RRKABEL.NS','RBLBANK.NS','RHIM.NS','RITES.NS','RADICO.NS','RVNL.NS','RAILTEL.NS','RAINBOW.NS','RKFORGE.NS','RCF.NS','REDINGTON.NS','RELINFRA.NS','RPOWER.NS','SBFC.NS','SBICARD.NS','SJVN.NS','SRF.NS','SAGILITY.NS','SAILIFE.NS','SAMMAANCAP.NS','SAPPHIRE.NS','SARDAEN.NS','SAREGAMA.NS','SCHAEFFLER.NS','SCHNEIDER.NS','SCI.NS','SHYAMMETL.NS','SIGNATURE.NS','SOBHA.NS','SONACOMS.NS','SONATSOFTW.NS','STARHEALTH.NS','SAIL.NS','SUMICHEM.NS','SUNTV.NS','SUNDARMFIN.NS','SUNDRMFAST.NS','SUPREMEIND.NS','SUZLON.NS','SWANCORP.NS','SWIGGY.NS','SYNGENE.NS','SYRMA.NS','TBOTEK.NS','TATACHEM.NS','TATACOMM.NS','TATAELXSI.NS','TATAINVEST.NS','TATATECH.NS','TTML.NS','TECHNOE.NS','TEJASNET.NS','NIACL.NS','RAMCOCEM.NS','THERMAX.NS','TIMKEN.NS','TITAGARH.NS','TORNTPOWER.NS','TARIL.NS','TRIDENT.NS','TRIVENI.NS','TRITURBINE.NS','TIINDIA.NS','UCOBANK.NS','UNOMINDA.NS','UPL.NS','UTIAMC.NS','UNIONBANK.NS','UBL.NS','USHAMART.NS','VGUARD.NS','DBREALTY.NS','VTL.NS','MANYAVAR.NS','VENTIVE.NS','VIJAYA.NS','VMM.NS','IDEA.NS','VOLTAS.NS','WAAREEENER.NS','WELCORP.NS','WELSPUNLIV.NS','WHIRLPOOL.NS','WOCKPHARMA.NS','YESBANK.NS','ZFCVINDIA.NS','ZEEL.NS','ZENTEC.NS','ZENSARTECH.NS','ECLERX.NS']
pivot_lookback = 14
atr_length = 14
multiplier = 1

all_trades = []

def run_strategy(symbol):
    print(f"Analyzing {symbol}...")
    df = yf.download(symbol, period="max", interval="1wk", auto_adjust=True)
    if df.empty: return []
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df = df.dropna(subset=["Open","High","Low","Close"])

    # Indicators
    df["ATR"] = (df["High"] - df["Low"]).rolling(atr_length).mean()
    df["EMA14"] = df["Close"].ewm(span=14, adjust=False).mean()
    df["EMA30W"] = df["Close"].ewm(span=30, adjust=False).mean()
    df["Vol_Avg"] = df["Volume"].rolling(10).mean()
    df["High_52W"] = df["High"].rolling(52).max()

    # Find All Pivot Highs
    pivot_indices = []
    for i in range(pivot_lookback, len(df)):
        current_high = df["High"].iloc[i]
        left = df["High"].iloc[i-pivot_lookback:i].max()
        right_limit = min(i + pivot_lookback + 1, len(df))
        right = df["High"].iloc[i+1:right_limit].max() if i+1 < len(df) else 0
        if current_high > left and (i+pivot_lookback >= len(df) or current_high > right):
            pivot_indices.append(i)

    trades = []
    last_exit_idx = 0

    # Sequential Processing with "New Pivot Reset"
    p_idx = 0
    while p_idx < len(pivot_indices):
        p = pivot_indices[p_idx]
        if p < last_exit_idx:
            p_idx += 1
            continue

        pivot_price = df["High"].iloc[p]
        pivot_atr = df["ATR"].iloc[p]
        if pd.isna(pivot_atr): 
            p_idx += 1
            continue
        slope = pivot_atr / (atr_length * multiplier)

        # Determine when the NEXT pivot occurs
        next_pivot_idx = pivot_indices[p_idx + 1] if p_idx + 1 < len(pivot_indices) else len(df)

        # SCAN FOR ENTRY (Only until the next pivot occurs)
        entry_idx = -1
        for i in range(p + 1, next_pivot_idx):
            trendline_val = pivot_price - (i - p) * slope
            if df["Close"].iloc[i] > trendline_val:
                entry_idx = i + 1 
                # Capture breakout context...
                vol_mult = round(df["Volume"].iloc[i] / df["Vol_Avg"].iloc[i], 2) if df["Vol_Avg"].iloc[i] > 0 else 0
                dist_52w = round((df["Close"].iloc[i] / df["High_52W"].iloc[i] - 1) * 100, 2)
                above_ema30 = bool(df["Close"].iloc[i] > df["EMA30W"].iloc[i])
                break
        
        if entry_idx != -1:
            # Entry found! Now scan for Exit (Exit can happen after the next pivot)
            waiting_for_confirmation = False
            trade_closed = False
            max_drawdown = 0
            entry_price = df["Open"].iloc[entry_idx]

            for j in range(entry_idx, len(df) - 1):
                low_pct = (df["Low"].iloc[j] / entry_price - 1) * 100
                if low_pct < max_drawdown: max_drawdown = low_pct

                if waiting_for_confirmation:
                    if df["Close"].iloc[j] < reference_close:
                        exit_price = df["Open"].iloc[j+1]
                        trades.append({
                            "Symbol": symbol, "Status": "CLOSED", "Pivot Date": df.index[p],
                            "Entry Date": df.index[entry_idx], "Exit Date": df.index[j+1],
                            "Return %": round((exit_price / entry_price - 1) * 100, 2),
                            "MAE %": round(max_drawdown, 2), "Vol_Mult": vol_mult, "Above_EMA30W": above_ema30
                        })
                        last_exit_idx = j + 1
                        trade_closed = True
                        break
                    else: waiting_for_confirmation = False
                elif df["Close"].iloc[j] < df["EMA14"].iloc[j]:
                    reference_close = df["Close"].iloc[j]
                    waiting_for_confirmation = True

            if not trade_closed:
                # Capture Open Position
                last_idx = len(df) - 1
                trades.append({
                    "Symbol": symbol, "Status": "OPEN", "Pivot Date": df.index[p],
                    "Entry Date": df.index[entry_idx], "Exit Date": df.index[last_idx],
                    "Return %": round((df["Close"].iloc[last_idx] / entry_price - 1) * 100, 2),
                    "MAE %": round(max_drawdown, 2), "Vol_Mult": vol_mult, "Above_EMA30W": above_ema30
                })
                return trades # Stop if we are in an open trade

        p_idx += 1 # Move to next pivot (either because entry was closed or no entry found)

    return trades

# Execute
for sym in symbols:
    all_trades.extend(run_strategy(sym))
pd.DataFrame(all_trades).to_excel("pivot_reset_results.xlsx", index=False)
