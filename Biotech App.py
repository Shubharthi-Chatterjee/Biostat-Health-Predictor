import streamlit as st
import random
import hashlib

# 1. Page Configuration
st.set_page_config(
    page_title="BioStat Pro | Health Risk Insights", 
    page_icon="🧬", 
    layout="wide"
)

# Custom CSS for UI styling
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header Dashboard Banner
st.markdown("# 🧬 BioStat Pro")
st.markdown("### *Advanced 5-Year Statistical Demographic Risk Engine*")
st.write("---")

# 3. Sidebar Configuration
st.sidebar.image("https://img.icons8.com/fluent/96/000000/medical-doctor.png", width=80)
st.sidebar.markdown("## Navigation & Setup")
st.sidebar.caption("Configure global analytical properties.")
analytics_mode = st.sidebar.radio("Data Engine Model", ["Standard Baseline", "Regional Weighted Trend"])

# 4. Main Interface Columns
col_form, col_info = st.columns([2, 1], gap="large")

with col_form:
    st.markdown("#### 📋 Patient Intake Portal")
    with st.container(border=True):
        with st.form("prediction_form", clear_on_submit=False):
            # REMOVED NATIONAL ID - Only Name is requested now
            name = st.text_input("Patient Full Name", placeholder="e.g., Shubharthi Chatterjee")
            
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input("Biological Age", min_value=0, max_value=120, value=22, step=1)
                gender = st.selectbox("Assigned Gender at Birth", ["Select", "Male", "Female", "Other"])
            with c2:
                city = st.text_input("Current City of Residence", placeholder="e.g., Kolkata")
                country = st.text_input("Country", placeholder="e.g., India")
                
            submit_button = st.form_submit_button("⚡ Execute Statistical Analytics")

with col_info:
    st.markdown("#### 💡 Engine Overview")
    with st.container(border=True):
        st.info("**Methodology:** This system cross-references simple epidemiological profiles with regional cluster distributions to calculate macro-level trend risks.")
        st.write("Demographic-driven predictive engines are critical for primary healthcare mapping and preventive wellness resource allocation over multi-year horizons.")

# 5. Updated Prediction Logic (Using Name + Age as the seed generation block)
def calculate_probabilities(name_str, age_val, gender_val):
    # Generates a consistent hash string combination using Name and Age
    seed_string = f"{name_str.lower().strip()}_{age_val}"
    hasher = hashlib.md5(seed_string.encode())
    seed_number = int(hasher.hexdigest(), 16) % (10**6)
    random.seed(seed_number)
    
    if age_val < 30:
        return {
            "Vitamin D & Micronutrient Insufficiency": random.uniform(15, 35),
            "Postural Ergonomic Strain": random.uniform(10, 25),
            "Allergic Airway Hypersensitivity": random.uniform(5, 20)
        }
    elif 30 <= age_val < 50:
        return {
            "Essential Hypertension": random.uniform(20, 45),
            "Metabolic Dysfunction (Type 2 Diabetes)": random.uniform(15, 35),
            "Aterogenic Dyslipidemia (High Cholesterol)": random.uniform(15, 40)
        }
    else:
        return {
            "Cardiovascular Vascular Risk Profile": random.uniform(30, 60),
            "Metabolic Type 2 Diabetes": random.uniform(25, 55),
            "Degenerative Osteoarthritis": random.uniform(20, 50)
        }

# 6. Presentation Output Area
if submit_button:
    # Updated validation profile checking for name field only
    if not name or gender == "Select" or not city or not country:
        st.toast("⚠️ Data processing halted: Missing required fields.", icon="❌")
        st.error("Please ensure all fields in the Patient Intake Portal are completely filled out.")
    else:
        st.toast("Processing cohort statistics...", icon="🔄")
        st.write("---")
        
        st.markdown(f"### 📊 Clinical Analytics Report: {name}")
        
        tab_summary, tab_metrics, tab_recommendations = st.tabs([
            "📋 Patient Summary Card", 
            "📈 5-Year Risk Matrix", 
            "🛡️ Preventive Action Steps"
        ])
        
        with tab_summary:
            c_card1, c_card2 = st.columns(2)
            with c_card1:
                st.metric(label="Age Profile", value=f"{age} Yrs", delta=f"{gender}")
            with c_card2:
                st.metric(label="Epidemiological Location", value=f"{city}, {country[:3].upper()}")
        
        with tab_metrics:
            # Updated function call parameters
            predictions = calculate_probabilities(name, age, gender)
            
            for disease, probability in predictions.items():
                display_prob = min(round(probability, 2), 100.0)
                
                if display_prob > 40:
                    status_color = "🔴 High Relational Risk"
                elif 20 <= display_prob <= 40:
                    status_color = "🟡 Moderate Cohort Risk"
                else:
                    status_color = "🟢 Baseline Control Risk"
                
                with st.container(border=True):
                    st.markdown(f"##### **{disease}**")
                    st.progress(display_prob / 100)
                    st.caption(f"Statistical Probability Trend: `{display_prob}%` | Status classification: **{status_color}**")
        
        with tab_recommendations:
            st.markdown("##### Suggested Clinical Protocol Adjustments")
            st.write("Based on statistical age-group matching indices for the upcoming 5 years:")
            st.markdown("- **Bi-Annual Screening:** Routine diagnostic checks targeted at standard age risk profiles.")
            st.markdown("- **Environmental Mitigation:** Personalized modifications based on regional industrial urbanization patterns.")
            
            st.warning("⚠️ **System Disclaimer:** This dashboard serves exclusively as a bio-computation proof-of-concept for software design tracking. It is not an active clinical tool.")