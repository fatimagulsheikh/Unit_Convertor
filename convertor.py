import streamlit as st 

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #141e30, #243b55);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
        color: white;
    }
    h1 {
        text-align: center;
        font-size: 40px;
        color: #ffcc00;
        font-weight: bold;
        text-shadow: 2px 2px 5px rgba(255, 204, 0, 0.5);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff5733, #ffcc00);
        color: white;
        font-size: 20px;
        padding: 12px 24px;
        border-radius: 15px;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 5px 15px rgba(255, 87, 51, 0.5);
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        transform: scale(1.1);
        background: linear-gradient(45deg, #00c9ff, #92fe9d);
        color: black;
    }
    .result-box {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.3);
        color: white;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #ffcc00;
        font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1> ✨ Unit Converter with a Fresh Look ✨ </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature with style!")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# Conversion options
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# Button for conversion
if st.button("🔥 Convert Now 🔥"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)        

# Footer
st.markdown("<div class='footer'>🚀 Created with 💖 by Fatima Sheikh 🚀</div>", unsafe_allow_html=True)                 






