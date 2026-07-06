import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Global Page Layout & Theme Configuration
st.set_page_config(page_title="Executive Creator Panel", layout="centered")

# Configure a premium aesthetic theme preset for all Matplotlib operations
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.family': 'sans-serif',
    'axes.edgecolor': '#EAEAEA',
    'axes.linewidth': 0.8,
    'grid.color': '#F3F3F3'
})

# Premium CSS Injection for clean, enterprise-level typography
st.markdown("""
    <style>
    .main-title { font-size: 34px; font-weight: 700; color: #1E1E1E; text-align: center; margin-bottom: 5px; letter-spacing: -0.5px; }
    .sub-title { text-align: center; font-size: 14px; color: #666666; margin-bottom: 30px; font-weight: 400; }
    .executive-card { background-color: #1E1E2F; padding: 25px; border-radius: 6px; border-left: 6px solid #FF0000; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; margin-top: 15px; margin-bottom: 30px; }
    .metric-header { margin: 0 0 8px 0; color: #AEAEB2; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
    .prediction-value { margin: 0; color: #FFFFFF; font-size: 44px; font-weight: 700; letter-spacing: -1px; }
    .engine-tag { margin: 10px 0 0 0; font-size: 11px; color: #8E8E93; font-weight: 500; }
    </style>
""", unsafe_allow_html=True)

# 2. Production Binary Loading Layer
try:
    with open("champion_model.pkl", "rb") as f:
        deployed_model = pickle.load(f)
    with open("model_metadata.pkl", "rb") as f:
        _, model_winner, feature_columns = pickle.load(f)
except FileNotFoundError:
    st.error("🚨 Compiled model artifacts not found. Please complete all execution blocks inside your Jupyter Notebook first.")
    st.stop()

# Header Presentation Block
st.markdown("<div class='main-title'>🎬 Creator Engagement & Watch-Time Predictive Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'><b>Predictive Analytics Platform</b> | Course Evaluation Framework | Developed by: Apoorva I U</div>", unsafe_allow_html=True)
st.markdown("---")

# 3. Parameter Inputs Collection Workspace Form
st.header("⚙️ Video Production Parameters")
st.write("Configure your target quantitative video metrics below:")

# Clean linear slider elements
duration_mins = st.slider("Video Duration (Minutes)", 1.0, 60.0, 15.0, 0.5)
view_duration_sec = st.slider("Average View Duration (Seconds)", 10, 1200, 240, 10)
impressions = st.slider("System Impressions (Algorithmic Reach)", 1000, 2000000, 150000, 10000)
ctr = st.slider("Thumbnail Click-Through Rate (CTR %)", 0.5, 30.0, 8.5, 0.1)

# Secondary metric inputs organized cleanly into twin columns
col_in1, col_in2 = st.columns(2)
with col_in1:
    likes = st.number_input("Target Total Likes", min_value=0, value=5200, step=100)
    comments = st.number_input("Target Total Comments", min_value=0, value=380, step=10)
with col_in2:
    shares = st.number_input("Target Total Shares", min_value=0, value=120, step=10)
    subscribers = st.number_input("Subscribers Gained From Video", min_value=0, value=45)

# Execute real-time data engineering mappings
computed_engagement = (likes + comments) / (impressions + 1e-5)
avg_view_pct = ((view_duration_sec) / (duration_mins * 60)) * 100

st.markdown("###")

# 4. Inference Trigger and Execution Block
if st.button("Execute Production Inference Evaluation", type="primary", use_container_width=True):
    # Form input data row conforming precisely to your training pipeline attributes
    query_data = {
        'video_duration_min': duration_mins, 'avg_view_duration_sec': view_duration_sec,
        'avg_view_percentage': avg_view_pct, 'subscribers_gained': subscribers,
        'ctr_percentage': ctr, 'impressions': impressions, 'likes': likes,
        'comments': comments, 'shares': shares, 'engagement_rate': computed_engagement
    }
    
    ordered_input = [query_data.get(col, 0.0) for col in feature_columns]
    target_prediction = deployed_model.predict(np.array([ordered_input]))[0]
    
    # Render the Premium High-Contrast Slate Evaluation Card
    st.markdown(f"""
        <div class='executive-card'>
            <p class='metric-header'>📈 Algorithmic Watch-Time Valuation Forecast</p>
            <p class='prediction-value'>{max(0.0, target_prediction):,.1f} Hours</p>
            <p class='engine-tag'>Verified Generalization Engine Core: {model_winner}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("📊 Analytical Distribution Simulations")
    st.write("Dynamic charts computed live from your specified query parameters:")
    
    # ----------------------------------------------------
    # GRAPH 1: HIGH-RES DYNAMIC AUDIENCE RETENTION PATHWAY
    # ----------------------------------------------------
    st.subheader("1. Retention Decay Pathway Analysis")
    
    video_length_seconds = duration_mins * 60
    time_axis = np.linspace(0, video_length_seconds, 120)
    
    decay_constant = np.log(2) / max(10, view_duration_sec)
    retention_curve = 100 * np.exp(-decay_constant * time_axis)
    retention_curve = np.clip(retention_curve, 0, 100)
    
    # Create the figure with higher DPI for maximum clarity
    fig1, ax1 = plt.subplots(figsize=(11, 4), dpi=300)
    ax1.plot(time_axis / 60, retention_curve, color='#FF0000', linewidth=2.5, label="Audience Retention Trail")
    ax1.axvline(view_duration_sec / 60, color='#008080', linestyle='--', alpha=0.8, linewidth=1.5, label=f"Average Retention Drop Point: {view_duration_sec}s")
    ax1.fill_between(time_axis / 60, retention_curve, color='#FF0000', alpha=0.06)
    
    ax1.set_title("Predicted Interactive View-Time Drop-Off Distribution", fontsize=11, fontweight='bold', color='#1E1E1E', pad=12)
    ax1.set_xlabel("Video Timeline (Minutes)", fontsize=9, color='#555555')
    ax1.set_ylabel("Viewers Remaining (%)", fontsize=9, color='#555555')
    ax1.set_ylim(-5, 105)
    ax1.tick_params(axis='both', labelsize=8)
    ax1.legend(loc="upper right", fontsize=8, framealpha=0.9)
    
    st.pyplot(fig1)
    plt.close(fig1)
    
    st.markdown("###")
    
    # ----------------------------------------------------
    # GRAPH 2: PREMIUM HORIZONTAL PROGRESSION BAR MATRIX (UPDATED)
    # ----------------------------------------------------
    st.subheader("2. Proportional Engagement Density Distribution")
    total_interactions = likes + comments + shares
    
    if total_interactions > 0:
        p_likes = (likes / total_interactions) * 100
        p_comments = (comments / total_interactions) * 100
        p_shares = (shares / total_interactions) * 100
        
        # Build layout with a tighter height to look sleek and modern
        fig2, ax2 = plt.subplots(figsize=(11, 1.2), dpi=300)
        
        # Premium color palette definitions
        c_likes, c_comments, c_shares = '#008080', '#D9534F', '#F0AD4E'
        
        # Draw horizontal stacked progression blocks with clear borders
        ax2.barh([0], [p_likes], color=c_likes, edgecolor='white', height=0.5)
        ax2.barh([0], [p_comments], left=[p_likes], color=c_comments, edgecolor='white', height=0.5)
        ax2.barh([0], [p_shares], left=[p_likes + p_comments], color=c_shares, edgecolor='white', height=0.5)
        
        # Remove all borders and axes to keep it minimalist
        ax2.set_xlim(0, 100)
        ax2.set_axis_off()
        
        st.pyplot(fig2)
        plt.close(fig2)
        
        # EXECUTIVE LEGEND LAYOUT: Using clean columns below the graph instead of cramped text inside
        st.markdown(f"""
            <div style="display: flex; justify-content: space-around; background-color: #F8F9FA; padding: 12px; border-radius: 6px; border: 1px solid #EAEAEA; margin-top: -10px;">
                <div style="font-size: 13px; font-weight: 500; color: #333;"><span style="color: {c_likes}; font-size: 16px; margin-right: 5px;">●</span> <b>Likes:</b> {likes:,} ({p_likes:.1f}%)</div>
                <div style="font-size: 13px; font-weight: 500; color: #333;"><span style="color: {c_comments}; font-size: 16px; margin-right: 5px;">●</span> <b>Comments:</b> {comments:,} ({p_comments:.1f}%)</div>
                <div style="font-size: 13px; font-weight: 500; color: #333;"><span style="color: {c_shares}; font-size: 16px; margin-right: 5px;">●</span> <b>Shares:</b> {shares:,} ({p_shares:.1f}%)</div>
            </div>
            <p style="font-size: 11px; color: #8E8E93; font-style: italic; margin-top: 10px; text-align: center;">
                ℹ️ Analysis Note: Visual metrics reflect weight ratios mapped over an aggregate interaction volume pool of {total_interactions:,} instances.
            </p>
        """, unsafe_allow_html=True)
    else:
        st.info("Provide parameter values above 0 to generate engagement density distributions.")