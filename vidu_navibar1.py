import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu # pip install streamlit-option-menu
import pandas as pd  # pip install pandas
import numpy as np 
import plotly.express as px  # pip install plotly-express
import plotly.graph_objects as go
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import altair as alt
import math 
from pickletools import decimalnl_short
from tracemalloc import start    


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    #return st.markdown(href, unsafe_allow_html=True)

def generate_html_download_link(fig):
    # Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download Plot</a>'
    #return st.markdown(href, unsafe_allow_html=True)

st.set_page_config(page_title="REPORT GMV 2022", page_icon=":tada:", layout="wide")
st.title(':point_right:' 'SALE-OUT BY PLATFORM')


# 1) DATA ---------
#LZD_logo = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\Python Streamlit\\Sidebar_Navigator_Streamlit\\LZD_logo_4.png')
#plt.imshow(LZD_logo)

data = pd.read_excel('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Sidebar_Navibar_Streamlit\\ALL_GMV_2022(R1).xlsx')
#data['VIEW'] = data['VIEW'].replace(['-'], '0')
#data['VISIT'] = data['VISIT'].replace(['-'], '0')
data.replace([',', '0'],['s','0'])
data['STORE'] = data['STORE'].replace(['gift_Parroti_NG01'], 'gift_Parroti')
sort_data = data.sort_values(by=['STORE'])
#st.write(sort_data)

LZD_data = sort_data.loc[sort_data['STORE'] == 'LZD']
TIKI_data = sort_data.loc[sort_data['STORE'] == 'TIKI']
SPE_data = sort_data.loc[sort_data['STORE'] == 'SPE']

# 2) NAVIBAR ---------

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="PLATFORM: ",  # required
                options=["LAZADA", "TIKI", "SHOPEE"],  # required
                icons=['bar-chart', "bar-chart", "bar-chart"],  # optional
                menu_icon="bar-chart-line-fill",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["LAZADA", "TIKI", "SHOPEE"],  # required
            icons=["bar-chart-fill", "bar-chart-fill", "bar-chart-fill"],  # optional
            menu_icon="bar-chart-line-fill",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(                                     # pip install streamlit-option-menu
            menu_title=None,                                        # required
            options=["LAZADA", "TIKI", "SHOPEE"],                   # required
            icons=["shop", "shop", "shop"],                         # optional
            menu_icon="bar-chart-line-fill",                                       # optional
            default_index=0,                                        # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "grey"},
            },
        )
        return selected

# 3) CONTENT OF PAGES ---------

selected = streamlit_menu(example=3)

if selected == "LAZADA":
    #st.title(f"You have selected {selected}")
    
    col1, col2, col3, col4, col5 = st.columns([1,2.75,1.5,2,2])
    with col1:        
        LZD_logo = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\GitHub\\Sidebar_Navibar_Streamlit\\LZD_logo_4.png')
        st.image(LZD_logo)
            
    with col2:
        #st.markdown("##### @ LAZADA YTD Aug'22 (mil VND): ")   
        LZD_GMV = LZD_data['GMV VALUE (+VAT)'].sum()
        LZD_GMV1 = round(LZD_GMV)
        LZD_GMV2 ='{0:,}'.format(LZD_GMV1)              #  add thousand separator to numeric pandas       
        
        st.markdown("GMV value (đ):" )
        def header(url):
            st.markdown(f'<p style="background-color:#003399; text-align:center;color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(LZD_GMV2)        
    
    with col3:
        LZD_VOL = LZD_data['GMV VOL'].sum()
        LZD_VOL1 = '{0:,}'.format(LZD_VOL)
        st.markdown("Units sold:" )
        def header(url):
            st.markdown(f'<p style="background-color:#003399; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(LZD_VOL1)  

    with col4:
        LZD_view = LZD_data['VIEW'].sum()
        LZD_view1 = '{0:,}'.format(LZD_view)
        st.markdown("SKU Views:" )
        #st.write(LZD_view1)
        def header(url):
            st.markdown(f'<p style="background-color:#003399; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(LZD_view1)
        
    with col5:
        LZD_visit = LZD_data['VISIT'].sum()
        LZD_visit1 = '{0:,}'.format(LZD_visit)
        st.markdown("SKU Visitors:" )
        
        def header(url):
            st.markdown(f'<p style="background-color:#003399; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(LZD_visit1)

    with st.container():
        st.write("GMV by month: ")
        #LZD_groupby = LZD_data.groupby('promo MONTH').sum().reset_index()
        #LZD_bymonth= pd.DataFrame(LZD_groupby['GMV VALUE (+VAT)'], LZD_data ['CAT'] ).reset_index()
        #st.write(LZD_data)
        LZD_data1 = LZD_data[['promo MONTH','GMV VALUE (+VAT)', 'CAT']]
        #st.write(LZD_data1)
        LZD_GMV1 = LZD_data1.pivot_table(index ='promo MONTH', columns = 'CAT', values= 'GMV VALUE (+VAT)', margins=False,aggfunc=np.sum )  # nếu mốn có thêm cột All thì chọn : margins= True
        LZD_GMV = pd.DataFrame(LZD_GMV1)
        st.write(LZD_GMV)
        st.header("chart: ")
        #X = LZD_GMV(['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10'])
        #Y = [] 
        
        chart1 = pd.DataFrame(LZD_GMV)
        st.bar_chart(chart1)

        chart = alt.Chart(LZD_GMV). mark_bar().encode(
            x=LZD_GMV,
            y='X',
            )


        st.altair_chart(chart,use_container_width=True)

            
# https://discuss.streamlit.io/t/turn-vertical-bar-chart-to-horizontal/20107/4     
# https://discuss.streamlit.io/t/turn-vertical-bar-chart-to-horizontal/20107/4

    st.write('Stacked bar chart')
    
if selected == "TIKI":
    #st.title(f"You have selected {selected}")
    col1, col2, col3, col4, col5 = st.columns([1,2.75,1.5,2,2])

    with col1 :
        TIKI_logo = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\Python Streamlit\\Sidebar_Navigator_Streamlit\\TIKI_logo_4.png')
        st.image(TIKI_logo)

    with col2 :
        TIKI_GMV = TIKI_data['GMV VALUE (+VAT)'].sum()
        TIKI_GMV1 = round(TIKI_GMV)
        TIKI_GMV2 = '{0:,}'.format(TIKI_GMV1)                  #  add thousand separator to numeric pandas  
        #TIKI_GMV2 = pd.to_numeric([TIKI_GMV1], downcast='float')

        st.markdown("GMV value (đ):" )
        def header(url):
            st.markdown(f'<p style="background-color:#1aa7ff; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(TIKI_GMV2)
    
    with col3:
        TIKI_VOL = TIKI_data['GMV VOL'].sum()
        TIKI_VOL1 = '{0:,}'.format(TIKI_VOL)
        st.markdown("Unit sold:" )
        def header(url):
            st.markdown(f'<p style="background-color:#1aa7ff; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(TIKI_VOL1)

    with col4:
        TIKI_view = TIKI_data['VIEW'].sum()
        TIKI_view1 = '{0:,}'.format(TIKI_view)
        st.markdown("SKU Views:" )
        def header(url):
            st.markdown(f'<p style="background-color:#1aa7ff; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(TIKI_view1)

    with col5:
        TIKI_visit = TIKI_data['VISIT'].sum()
        TIKI_visit1 = '{0:,}'.format(TIKI_visit)
        st.markdown("SKU Visitors:" )
        def header(url):
            st.markdown(f'<p style="background-color:#1aa7ff; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(TIKI_visit1)


if selected == "SHOPEE":
    #st.title(f"You have selected {selected}")
    col1, col2, col3, col4, col5 = st.columns([1,2.75,1.5,2,2])

    with col1 :
        SPE_logo = mpimg.imread('C:\\Users\\tmlluu\\OneDrive\\Coding LuuLinh\\Python Streamlit\\Sidebar_Navigator_Streamlit\\SPE_logo_4.png')
        st.image(SPE_logo)

    with col2 :
        SPE_GMV = SPE_data['GMV VALUE (+VAT)'].sum()
        SPE_GMV1 = round(SPE_GMV)
        SPE_GMV2 = '{0:,}'.format(SPE_GMV)
        st.markdown("GMV value (đ):" )
        def header(url):
            st.markdown(f'<p style="background-color:#ff6600; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(SPE_GMV2)
    
    with col3:
        SPE_VOL = SPE_data['GMV VOL'].sum()
        SPE_VOL1 = '{0:,}'.format(SPE_VOL)
        st.markdown("Units sold:" )
        def header(url):
            st.markdown(f'<p style="background-color:#ff6600; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(SPE_VOL1)

    with col4:
        SPE_view = SPE_data['VIEW'].sum()
        SPE_view1 = '{0:,}'.format(SPE_view)
        st.markdown("SKU Views:" )
        def header(url):
            st.markdown(f'<p style="background-color:#ff6600; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(SPE_view1)

    with col5:
        SPE_visit = SPE_data['VISIT'].sum()
        SPE_visit1 = '{0:,}'.format(SPE_visit)
        st.markdown("SKU Visitors:" )
        def header(url):
            st.markdown(f'<p style="background-color:#ff6600; text-align:center; color:#ffffff;font-size:48px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
        header(SPE_visit1)

