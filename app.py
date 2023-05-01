import pandas as pd
import plotly.express as px
import streamlit as st





# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_icon=":bar_chart:",
                   layout="wide",
                   )

df = pd.read_excel('Summary.xlsx', engine='openpyxl',  nrows=100,
                   )


st.sidebar.header("Please Filter Here:")

type= st.sidebar.multiselect(
    "Select the Investment type",
    options=df['Tipo'].unique(),
    default=df['Tipo'].unique()
)


rate= st.sidebar.multiselect(
    "Select the Yield",
    options=df['Yield'].unique(),
    default=df['Yield'].unique()
)


available= st.sidebar.multiselect(
    "Select the investment Maturity",
    options=df['Carência'].unique(),
    default=df['Carência'].unique()
)


df_selection = df.query(
    "Tipo == @type & Yield==@rate & Carência==@available"
)


st.dataframe(df_selection)

st.title(":bar_chart: Resumão DASHBOARD")
st.markdown("##")

total_investido = df_selection['Valor'].sum()
average_available = float(round(df_selection['Valor'].mean(),2))
#star_available =  ":star:" * int(round(average_available, 0))
#average_spent_by_transaction = round(df_selection['Total_Consumido'].mean())


left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Valor")
    st.subheader(f" Investimento { total_investido:,}")
with right_column:
    st.subheader("Média Investimento:")
    st.subheader(f"{average_available} ")


st.markdown("---")

investment_by_type = (
    df_selection.groupby(by=["Tipo"]).sum()[["Valor"]].sort_values(by="Valor")
)

fig_investment_by_type = px.bar(
    investment_by_type,
    x= "Valor",
    y= investment_by_type.index,
    orientation="h",
    title= "<b>Investimento por Tipo</b>",
    color_discrete_sequence=["#008388"] * len(investment_by_type),
    template="plotly_white",
)

fig_investment_by_type.update_layout(
    plot_bgcolor= 'rgba(0,0,0,0)',
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_investment_by_type)


# hide_st_style = """"
#                 <style>
#                 #MainMenu {visibility: hiden;}
#                 footer {visibility: hidden;}
#                 header {visibility: hidden;}
#                 </style>
# """


# st.markdown(hide_st_style, unsafe_allow_html=True)