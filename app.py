import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Turbine Insight", layout="wide", initial_sidebar_state="expanded")

# --- SESSION STATE FOR NAVIGATION ---
if 'active_page' not in st.session_state:
    st.session_state.active_page = "Dashboard"

def set_page(page_name):
    st.session_state.active_page = page_name

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        .block-container { padding-top: 5rem; }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #ffffff;
        }

        /* Style for all sidebar buttons */
        .stButton > button {
            width: 100%;
            border-radius: 8px;
            border: none;
            text-align: left;
            background-color: transparent;
            color: #4A5568;
            padding: 8px 12px;
            transition: all 0.3s;
            justify-content: flex-start;
        }

        /* Hover effect */
        .stButton > button:hover {
            background-color: #F7FAFC;
            color: #2D3748;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 💠 Digital Turbine Insight\n*Marketing Analytics*")
    st.divider()
    
    # Navigation Groups with Material Icons
    menu_structure = {
        "ANALYTICS": {
            "Dashboard": "dashboard",
            "Operations": "vital_signs",
            "Campaign Performance": "bar_chart",
            "Attribution & MMM": "automation",
            "Incrementality Tests": "experiment",
            "Marketing Funnel": "filter_alt"
        },
        "CHANNELS": {
            "Retail Media": "shopping_cart",
            "Walled Gardens": "lock"
        },
        "INTELLIGENCE": {
            "Creative Intelligence": "palette",
            "Audience Intelligence": "groups",
            "Financial & Budget": "payments",
            "Competitive Intel": "swords"
        },
        "TOOLS": {
            "AI Assistant": "chat_bubble",
            "Settings": "settings"
        }
    }

    for section, items in menu_structure.items():
        st.markdown(f"**{section}**")
        for item, icon_name in items.items():
            is_active = st.session_state.active_page == item
            
            if st.button(
                item, 
                icon=f":material/{icon_name}:", 
                key=f"btn_{item}", 
                on_click=set_page, 
                args=(item,),
                type="secondary" if not is_active else "primary"
            ):
                pass
        st.write("") # Spacer

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("👤 **John Doe**\n\nAdmin")


# --- GLOBAL DATA & COLOR MAP ---
color_map = {
    'Meta': '#2a9d8f', 
    'Google': '#219ebc', 
    'TikTok': '#7209b7', 
    'Amazon': '#ffb703', 
    'Pinterest': '#e63946', 
    'Snap': '#06d6a0'
}
channels = ['Meta', 'Google', 'TikTok', 'Amazon', 'Pinterest', 'Snap']

# --- MAIN CONTENT LOGIC ---
if st.session_state.active_page == "Dashboard":
    
    # --- TOP HEADER & FILTERS ---
    filter_col1, filter_col2, filter_col3, _ = st.columns([2, 2, 3, 5])
    with filter_col1:
        st.selectbox("Organization", ["Acme Corp", "Globex", "Initech"], key="dash_org", label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Products", ["All Products", "Software", "Hardware"], key="dash_prod", label_visibility="collapsed")
    with filter_col3:
        st.date_input("Date Range", [], key="dash_date", label_visibility="collapsed")

    st.title("Dashboard")
    st.markdown("Unified marketing performance overview")

    # --- KPI METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric(label="Total Spend", value="$765K", delta="12.5%")
    with m2:
        with st.container(border=True):
            st.metric(label="ROAS", value="4.2x", delta="8.3%")
    with m3:
        with st.container(border=True):
            st.metric(label="Conversions", value="18.5K", delta="-3.2%")
    with m4:
        with st.container(border=True):
            st.metric(label="CPA", value="$41.35", delta="-5.1%", delta_color="inverse")

    # --- DATA PREP ---
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    roas_data = pd.DataFrame({'Month': months, 'ROAS': [3.2, 3.5, 3.1, 3.8, 4.2, 4.0, 4.5, 4.1, 3.9, 4.3, 4.8, 5.1]})
    spend_data = pd.DataFrame({'Channel': channels, 'Spend': [270, 200, 90, 160, 40, 50]}).iloc[::-1] 

    # --- ROW 1 CHARTS ---
    col1, col2 = st.columns([1.2, 1])
    with col1:
        with st.container(border=True):
            st.markdown("**ROAS Trend** \n*Last 12 months*")
            fig_roas = px.line(roas_data, x='Month', y='ROAS')
            fig_roas.update_traces(fill='tozeroy', line_color='#2a9d8f')
            fig_roas.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=300, yaxis_range=[0, 8])
            st.plotly_chart(fig_roas, use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Spend by Channel** \n*Current period*")
            fig_spend = px.bar(spend_data, x='Spend', y='Channel', orientation='h', color='Channel', color_discrete_map=color_map)
            fig_spend.update_layout(showlegend=False, margin=dict(l=0, r=0, t=20, b=0), height=300, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig_spend, use_container_width=True)

    # --- ROW 2 CHARTS ---
    col3, col4, col5 = st.columns(3)
    with col3:
        with st.container(border=True):
            st.markdown("**Channel ROAS**")
            fig_ch_roas = px.bar(pd.DataFrame({'Channel': channels, 'ROAS': [4, 5, 2.5, 3, 1.5, 2]}), x='Channel', y='ROAS')
            fig_ch_roas.update_traces(marker_color='#2a9d8f')
            fig_ch_roas.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=250, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig_ch_roas, use_container_width=True)

    with col4:
        with st.container(border=True):
            st.markdown("**Budget Allocation**")
            fig_donut = px.pie(spend_data, values='Spend', names='Channel', hole=0.6, color='Channel', color_discrete_map=color_map)
            fig_donut.update_layout(showlegend=False, margin=dict(l=0, r=0, t=20, b=0), height=250)
            st.plotly_chart(fig_donut, use_container_width=True)

    with col5:
        with st.container(border=True):
            st.markdown("**Monthly Spend**")
            spend_trend = pd.DataFrame({'Month': months, 'Spend': [100, 110, 105, 130, 120, 140, 135, 145, 140, 150, 160, 190]})
            fig_spend_trend = px.line(spend_trend, x='Month', y='Spend')
            fig_spend_trend.update_traces(line_color='#0077b6')
            fig_spend_trend.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=250, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig_spend_trend, use_container_width=True)

# --- OPERATIONS PAGE ---
elif st.session_state.active_page == "Operations":
    
    # --- TOP HEADER & FILTERS ---
    filter_col1, filter_col2, filter_col3, _ = st.columns([2, 2, 3, 5])
    with filter_col1:
        st.selectbox("Organization", ["Acme Corp", "Globex", "Initech"], key="op_org", label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Products", ["All Products", "Software", "Hardware"], key="op_prod", label_visibility="collapsed")
    with filter_col3:
        st.date_input("Date Range", [], key="op_date", label_visibility="collapsed")

    st.title("Operations Dashboard")
    st.markdown("Real-time campaign delivery metrics for Acme Corp")

    # --- KPI METRICS ROW ---
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    with m1:
        with st.container(border=True):
            st.metric(label="Impressions", value="49.4M", delta="6.2%")
    with m2:
        with st.container(border=True):
            st.metric(label="Clicks", value="882K", delta="4.8%")
    with m3:
        with st.container(border=True):
            st.metric(label="CPM", value="$6.54", delta="-2.1%")
    with m4:
        with st.container(border=True):
            st.metric(label="CPC", value="$0.37", delta="-3.5%")
    with m5:
        with st.container(border=True):
            st.metric(label="CPA", value="$22.11", delta="-1.8%")
    with m6:
        with st.container(border=True):
            st.metric(label="Pacing", value="82%", delta="1.2%")

    # --- DAILY TRENDS (AREA CHARTS) ---
    days = [f"Mar {i}" for i in range(1, 15)]
    imp_data = pd.DataFrame({'Day': days, 'Impressions': [2.1, 2.3, 2.0, 2.4, 2.6, 2.4, 2.7, 2.3, 2.5, 2.9, 2.6, 2.8, 3.1, 3.0]})
    clicks_data = pd.DataFrame({'Day': days, 'Clicks': [40, 45, 38, 48, 52, 47, 54, 45, 50, 56, 48, 55, 60, 58]})

    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("**Daily Impressions**\n\n<span style='color:gray; font-size: 14px;'>Last 14 days</span>", unsafe_allow_html=True)
            fig_imp = px.area(imp_data, x='Day', y='Impressions')
            fig_imp.update_traces(line_color='#00a8e8', fillcolor='rgba(0, 168, 232, 0.1)')
            fig_imp.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=250, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig_imp, use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Daily Clicks**\n\n<span style='color:gray; font-size: 14px;'>Last 14 days</span>", unsafe_allow_html=True)
            fig_clicks = px.area(clicks_data, x='Day', y='Clicks')
            fig_clicks.update_traces(line_color='#06d6a0', fillcolor='rgba(6, 214, 160, 0.1)')
            fig_clicks.update_layout(margin=dict(l=0, r=0, t=10, b=0), height=250, xaxis_title=None, yaxis_title=None)
            st.plotly_chart(fig_clicks, use_container_width=True)

    # --- COST METRICS BY CHANNEL ---
    cpm_data = pd.DataFrame({'Channel': channels, 'CPM': [7.5, 9.2, 6.8, 4.5, 3.2, 5.8]})
    cpc_data = pd.DataFrame({'Channel': channels, 'CPC': [0.42, 0.28, 0.35, 0.55, 0.58, 0.40]})
    cpa_data = pd.DataFrame({'Channel': channels, 'CPA': [38.0, 42.0, 35.0, 45.0, 52.0, 48.0]})

    col3, col4, col5 = st.columns(3)
    with col3:
        with st.container(border=True):
            st.markdown("**CPM by Channel**\n\n<span style='color:gray; font-size: 14px;'>Cost per 1,000 impressions</span>", unsafe_allow_html=True)
            fig_cpm = px.bar(cpm_data, x='Channel', y='CPM', color='Channel', color_discrete_map=color_map)
            fig_cpm.update_layout(showlegend=False, margin=dict(l=0, r=0, t=10, b=0), height=250, xaxis_title=None, yaxis_title=None)
            fig_cpm.update_yaxes(tickprefix="$")
            st.plotly_chart(fig_cpm, use_container_width=True)

    with col4:
        with st.container(border=True):
            st.markdown("**CPC by Channel**\n\n<span style='color:gray; font-size: 14px;'>Cost per click</span>", unsafe_allow_html=True)
            fig_cpc = px.bar(cpc_data, x='Channel', y='CPC', color='Channel', color_discrete_map=color_map)
            fig_cpc.update_layout(showlegend=False, margin=dict(l=0, r=0, t=10, b=0), height=250, xaxis_title=None, yaxis_title=None)
            fig_cpc.update_yaxes(tickprefix="$")
            st.plotly_chart(fig_cpc, use_container_width=True)

    with col5:
        with st.container(border=True):
            st.markdown("**CPA by Channel**\n\n<span style='color:gray; font-size: 14px;'>Cost per acquisition</span>", unsafe_allow_html=True)
            fig_cpa = px.bar(cpa_data, x='Channel', y='CPA', color='Channel', color_discrete_map=color_map)
            fig_cpa.update_layout(showlegend=False, margin=dict(l=0, r=0, t=10, b=0), height=250, xaxis_title=None, yaxis_title=None)
            fig_cpa.update_yaxes(tickprefix="$")
            st.plotly_chart(fig_cpa, use_container_width=True)

    # --- BUDGET PACING & CTR ---
    with st.container(border=True):
        st.markdown("**Budget Pacing by Channel**\n\n<span style='color:gray; font-size: 14px;'>Budget vs actual spend</span>", unsafe_allow_html=True)
        
        budget_vals = [120, 100, 70, 80, 25, 40]
        actual_vals = [98, 85, 50, 62, 18, 25]
        
        rev_channels = channels[::-1]
        rev_budget = budget_vals[::-1]
        rev_actual = actual_vals[::-1]
        bar_colors = [color_map[c] for c in rev_channels]
        
        fig_pace = go.Figure()
        
        fig_pace.add_trace(go.Bar(
            y=rev_channels, x=rev_budget, orientation='h', 
            name='Budget', marker=dict(color='#e2e8f0'), 
            width=0.6, hoverinfo='skip'
        ))
        fig_pace.add_trace(go.Bar(
            y=rev_channels, x=rev_actual, orientation='h', 
            name='Actual', marker=dict(color=bar_colors), 
            width=0.4
        ))
        
        fig_pace.update_layout(
            barmode='overlay', showlegend=False, 
            margin=dict(l=0, r=0, t=10, b=0), height=300,
            xaxis_title=None, yaxis_title=None
        )
        fig_pace.update_xaxes(tickprefix="$", ticksuffix="K")
        st.plotly_chart(fig_pace, use_container_width=True)

    with st.container(border=True):
        st.markdown("**Click-Through Rate by Channel**\n\n<span style='color:gray; font-size: 14px;'>CTR %</span>", unsafe_allow_html=True)
        ctr_data = pd.DataFrame({'Channel': channels, 'CTR': [1.8, 3.2, 2.4, 0.9, 1.1, 1.5]})
        fig_ctr = px.bar(ctr_data, x='Channel', y='CTR', color='Channel', color_discrete_map=color_map)
        fig_ctr.update_layout(showlegend=False, margin=dict(l=0, r=0, t=10, b=0), height=300, xaxis_title=None, yaxis_title=None)
        fig_ctr.update_yaxes(ticksuffix="%")
        st.plotly_chart(fig_ctr, use_container_width=True)

# --- CAMPAIGN PERFORMANCE PAGE ---
elif st.session_state.active_page == "Campaign Performance":
    
    # --- TOP HEADER & FILTERS ---
    filter_col1, filter_col2, filter_col3, _ = st.columns([2, 2, 3, 5])
    with filter_col1:
        st.selectbox("Organization", ["Acme Corp", "Globex", "Initech"], key="camp_org", label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Products", ["All Products", "Software", "Hardware"], key="camp_prod", label_visibility="collapsed")
    with filter_col3:
        st.date_input("Date Range", [], key="camp_date", label_visibility="collapsed")

    st.title("Campaign Performance")
    st.markdown("Detailed campaign-level analytics across all channels")

    # --- KPI METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric(label="Total Spend", value="$367K", delta="15.2%")
    with m2:
        with st.container(border=True):
            st.metric(label="Avg ROAS", value="4.14x", delta="6.8%")
    with m3:
        with st.container(border=True):
            st.metric(label="Total Conversions", value="11.4K", delta="9.1%")
    with m4:
        with st.container(border=True):
            st.metric(label="Avg CPA", value="$32.19", delta="-7.3%", delta_color="inverse")

    # --- BAR CHART ---
    campaign_data = pd.DataFrame({
        'Campaign': ['Brand Awareness Q4', 'Retargeting - Cart', 'Prospecting - LAL', 'Holiday Push', 'Summer Sale'],
        'Spend': [85, 42, 65, 120, 55],
        'Revenue': [342, 231, 195, 580, 187],
        'ROAS': ['4x', '5.5x', '3x', '4.8x', '3.4x'],
        'Conversions': ['2,800', '1,900', '1,400', '4,200', '1,100']
    })

    with st.container(border=True):
        st.markdown("**Campaign Performance Comparison**\n\n<span style='color:gray; font-size: 14px;'>Revenue & spend by campaign</span>", unsafe_allow_html=True)
        
        melted_df = pd.melt(campaign_data, id_vars=['Campaign'], value_vars=['Spend', 'Revenue'], var_name='Metric', value_name='Amount')
        
        fig_camp = px.bar(
            melted_df, 
            x='Campaign', 
            y='Amount', 
            color='Metric', 
            barmode='group',
            color_discrete_map={'Spend': '#00a8e8', 'Revenue': '#2a9d8f'}
        )
        
        fig_camp.update_layout(
            legend_title_text='',
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
            margin=dict(l=0, r=0, t=20, b=0),
            height=350,
            xaxis_title=None,
            yaxis_title=None
        )
        fig_camp.update_yaxes(tickprefix="$", ticksuffix="K")
        st.plotly_chart(fig_camp, use_container_width=True)

    # --- DATA TABLE ---
    with st.container(border=True):
        st.markdown("**Campaign Details**")
        
        display_df = campaign_data.copy()
        display_df['Spend'] = display_df['Spend'].apply(lambda x: f"${x}K")
        display_df['Revenue'] = display_df['Revenue'].apply(lambda x: f"${x}K")
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)

# --- ATTRIBUTION & MMM PAGE ---
elif st.session_state.active_page == "Attribution & MMM":
    
    # --- TOP HEADER & FILTERS ---
    filter_col1, filter_col2, filter_col3, _ = st.columns([2, 2, 3, 5])
    with filter_col1:
        st.selectbox("Organization", ["Acme Corp", "Globex", "Initech"], key="attr_org", label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Products", ["All Products", "Software", "Hardware"], key="attr_prod", label_visibility="collapsed")
    with filter_col3:
        st.date_input("Date Range", [], key="attr_date", label_visibility="collapsed")

    st.title("Attribution & MMM")
    st.markdown("Multi-touch attribution and marketing mix modeling")

    # --- KPI METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric(label="Data-Driven ROAS", value="4.5x", delta="+12.1%")
    with m2:
        with st.container(border=True):
            st.metric(label="Incrementality", value="68%", delta="+3.2%")
    with m3:
        with st.container(border=True):
            st.metric(label="Contribution Margin", value="42%", delta="-1.5%")
    with m4:
        with st.container(border=True):
            st.metric(label="Cross-Channel Assists", value="34%", delta="+8.7%")

    # --- CHARTS ROW ---
    col1, col2 = st.columns([1.6, 1])
    
    with col1:
        with st.container(border=True):
            st.markdown("**Attribution Model Comparison**\n\n<span style='color:gray; font-size: 14px;'>% credit by model</span>", unsafe_allow_html=True)
            
            attr_channels = ['Meta', 'Google', 'TikTok', 'Amazon', 'Email', 'Direct']
            attr_data = pd.DataFrame({
                'Channel': attr_channels * 4,
                'Model': ['First Touch']*6 + ['Last Touch']*6 + ['Linear']*6 + ['Data-Driven']*6,
                'Credit': [
                    32, 28, 18, 12, 5, 5,   
                    28, 35, 12, 18, 4, 3,   
                    30, 30, 15, 15, 6, 4,   
                    35, 28, 17, 10, 5, 3    
                ]
            })
            
            attr_color_map = {
                'First Touch': '#2a9d8f', 
                'Last Touch': '#00a8e8',  
                'Linear': '#7209b7',      
                'Data-Driven': '#ffb703'  
            }
            
            fig_attr = px.bar(
                attr_data, 
                x='Channel', 
                y='Credit', 
                color='Model', 
                barmode='group',
                color_discrete_map=attr_color_map
            )
            
            fig_attr.update_layout(
                legend_title_text='',
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
                margin=dict(l=0, r=0, t=10, b=0),
                height=400,
                xaxis_title=None,
                yaxis_title=None,
                yaxis=dict(dtick=9) 
            )
            st.plotly_chart(fig_attr, use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Channel Contribution Radar**\n\n<span style='color:gray; font-size: 14px;'>Data-driven model</span>", unsafe_allow_html=True)
            
            radar_vals = [35, 28, 17, 10, 5, 3] 
            
            radar_vals_closed = radar_vals + [radar_vals[0]]
            radar_channels_closed = attr_channels + [attr_channels[0]]
            
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=radar_vals_closed,
                theta=radar_channels_closed,
                fill='toself',
                line_color='#00a8e8',
                fillcolor='rgba(0, 168, 232, 0.3)',
                hoverinfo="theta+r"
            ))
            
            fig_radar.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, showticklabels=False, range=[0, 40])
                ),
                showlegend=False,
                margin=dict(l=40, r=40, t=30, b=30),
                height=400
            )
            st.plotly_chart(fig_radar, use_container_width=True)

# --- INCREMENTALITY TESTS PAGE ---
elif st.session_state.active_page == "Incrementality Tests":
    
    # --- TOP HEADER & FILTERS ---
    filter_col1, filter_col2, filter_col3, _ = st.columns([2, 2, 3, 5])
    with filter_col1:
        st.selectbox("Organization", ["Acme Corp", "Globex", "Initech"], key="inc_org", label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Products", ["All Products", "Software", "Hardware"], key="inc_prod", label_visibility="collapsed")
    with filter_col3:
        st.date_input("Date Range", [], key="inc_date", label_visibility="collapsed")

    st.title("Incrementality Tests")
    st.markdown("Geo-lift and holdout experiment results")

    # --- KPI METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric(label="Avg iROAS", value="3.5x", delta="+9.4%")
    with m2:
        with st.container(border=True):
            st.metric(label="Avg Lift", value="11%", delta="+4.2%")
    with m3:
        with st.container(border=True):
            st.metric(label="Active Tests", value="4", delta="0%")
    with m4:
        with st.container(border=True):
            st.metric(label="Avg Confidence", value="91%", delta="+2.1%")

    # --- CHARTS ROW ---
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("**Test Results – iROAS**\n\n<span style='color:gray; font-size: 14px;'>By experiment</span>", unsafe_allow_html=True)
            
            iroas_data = pd.DataFrame({
                'Experiment': ['Meta Geo-Lift Q3', 'TikTok Holdout', 'Google Brand Lift', 'Amazon ASIN Test'],
                'iROAS': [3.8, 5.2, 2.9, 2.1]
            })
            
            fig_iroas = px.bar(iroas_data, x='Experiment', y='iROAS')
            fig_iroas.update_traces(marker_color='#2a9d8f')
            fig_iroas.update_layout(
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
                xaxis_title=None,
                yaxis_title=None
            )
            st.plotly_chart(fig_iroas, use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("**Geo Test vs Control**\n\n<span style='color:gray; font-size: 14px;'>Revenue comparison</span>", unsafe_allow_html=True)
            
            geo_data = pd.DataFrame({
                'Group': ['Test – Northeast', 'Control – Southeast', 'Test – West', 'Control – Midwest'],
                'Revenue': [420, 380, 500, 390]
            })
            
            fig_geo = px.bar(geo_data, x='Group', y='Revenue')
            fig_geo.update_traces(marker_color='#00a8e8')
            fig_geo.update_layout(
                margin=dict(l=0, r=0, t=10, b=0),
                height=300,
                xaxis_title=None,
                yaxis_title=None
            )
            fig_geo.update_yaxes(tickprefix="$", ticksuffix="K")
            st.plotly_chart(fig_geo, use_container_width=True)

    # --- DATA TABLE ---
    with st.container(border=True):
        st.markdown("**Test Library**")
        
        test_library_data = pd.DataFrame({
            'Test Name': ['Meta Geo-Lift Q3', 'TikTok Holdout', 'Google Brand Lift', 'Amazon ASIN Test'],
            'iROAS': ['3.8x', '5.2x', '2.9x', '2.1x'],
            'Lift %': ['+12%', '+18%', '+8%', '+6%'],
            'Confidence': ['95%', '92%', '88%', '90%']
        })
        
        st.dataframe(test_library_data, use_container_width=True, hide_index=True)

# --- MARKETING FUNNEL PAGE ---
elif st.session_state.active_page == "Marketing Funnel":
    
    # --- TOP HEADER & FILTERS ---
    filter_col1, filter_col2, filter_col3, _ = st.columns([2, 2, 3, 5])
    with filter_col1:
        st.selectbox("Organization", ["Acme Corp", "Globex", "Initech"], key="funnel_org", label_visibility="collapsed")
    with filter_col2:
        st.selectbox("Products", ["All Products", "Software", "Hardware"], key="funnel_prod", label_visibility="collapsed")
    with filter_col3:
        st.date_input("Date Range", [], key="funnel_date", label_visibility="collapsed")

    st.title("Marketing Funnel")
    st.markdown("Awareness → Conversion funnel analytics")

    # --- KPI METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric(label="Funnel Conversion", value="0.15%", delta="+2.1%")
    with m2:
        with st.container(border=True):
            # Dropping is good for Drop-off Rate, so inverse colors
            st.metric(label="Drop-off Rate", value="62%", delta="-4.3%", delta_color="inverse")
    with m3:
        with st.container(border=True):
            # Less time is better, so inverse colors
            st.metric(label="Avg Time to Convert", value="4.2d", delta="-8.1%", delta_color="inverse")
    with m4:
        with st.container(border=True):
            st.metric(label="Touch Points", value="5.3", delta="+1.2%")

    # --- FUNNEL CHART ---
    with st.container(border=True):
        st.markdown("**Conversion Funnel**\n\n<span style='color:gray; font-size: 14px;'>Volume by stage</span>", unsafe_allow_html=True)
        
        funnel_stages = ['Impressions', 'Clicks', 'Site Visits', 'Add to Cart', 'Checkout', 'Purchase']
        funnel_volumes = [13500000, 800000, 400000, 80000, 30000, 18500]
        
        # Colors to match the provided screenshot
        funnel_colors = ['#2a9d8f', '#06d6a0', '#00a8e8', '#7209b7', '#ffb703', '#e63946']
        
        df_funnel = pd.DataFrame({
            'Stage': funnel_stages,
            'Volume': funnel_volumes,
            'Color': funnel_colors
        })
        
        fig_funnel = px.bar(
            df_funnel, 
            x='Volume', 
            y='Stage', 
            orientation='h',
            color='Stage',
            color_discrete_map={k: v for k, v in zip(funnel_stages, funnel_colors)}
        )
        
        fig_funnel.update_layout(
            showlegend=False,
            margin=dict(l=0, r=0, t=10, b=0),
            height=400,
            xaxis_title=None,
            yaxis_title=None,
            yaxis={'categoryorder':'array', 'categoryarray': funnel_stages[::-1]} # Display top-down
        )
        
        # Format X axis to match the image precisely (Millions)
        fig_funnel.update_xaxes(
            tickvals=[0, 3500000, 7000000, 10500000, 14000000],
            ticktext=['0', '3.5M', '7.0M', '10.5M', '14.0M']
        )
        
        st.plotly_chart(fig_funnel, use_container_width=True)

# --- PLACEHOLDER FOR OTHER PAGES ---
else:
    st.title(st.session_state.active_page)
    st.info(f"The {st.session_state.active_page} module is currently under construction.")