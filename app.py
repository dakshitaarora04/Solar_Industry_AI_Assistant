import streamlit as st
from processor import load_image, extract_rooftop_area
from analysis import calculate_area, estimate_solar_output, estimate_roi
from llm_agent import get_llm_response
import numpy as np

st.set_page_config(page_title="Solar Rooftop Analysis", layout="centered")
st.title("🔆 AI-Powered Rooftop Solar Analysis")

uploaded_file = st.file_uploader("Upload a Satellite Image of Your Rooftop", type=['jpg', 'png'])

if uploaded_file:
    image = load_image(uploaded_file)
    mask = extract_rooftop_area(image)

    area = calculate_area(mask)
    output_kw = estimate_solar_output(area) / 1000
    roi = estimate_roi(output_kw)

    st.image(image, caption="Original Image", use_container_width=True)
    st.image(mask, caption="Detected Rooftop Area (Grayscale)", use_container_width=True, clamp=True)


    st.markdown("### 📊 Solar Analysis")
    st.success(f"**Rooftop Area:** {area:.2f} m²")
    st.success(f"**Estimated Output:** {output_kw:.2f} kW")
    st.success(f"**Estimated ROI:** {roi} years")

    prompt = f"""Analyze this rooftop:
- Area: {area:.2f} m²
- Output: {output_kw:.2f} kW
- ROI: {roi} years

Give installation tips for homeowners and professionals, including panel type, direction, and optimization advice.
"""
    response = get_llm_response(prompt)

    st.markdown("### 🧠 LLM Recommendations")
    st.info(response)
