#Project 01: unit convertor
#Build a google unit convertor using python and streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #lele2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc.#cfe2f3)
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
        text-align: center;
        front-size: 36px;
        color: white;
    }
    .stButton>button{
        background: liner-gardient(45deg, #0b5394, #351c75)
        color: black;
        font-size: 18px;
        paddingL 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.4);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px
        font-weight: bold;
        text-align: center;
        background: rgba(255,255,255,0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.3);
        }
        .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black
        }
        </style>
        """,
        unsafe_allow_html=True
)

#title and description (title and description)
st.markdown("<h1> unit convertor using python and streamlit </h1>", unsafe_allow_html=True)
st.write("easily covert between different units of lenght , weight, and temprature.")

#sidebar menu (conversion type select karna ka option)
conversion_type = st.sidebar.selectbox("choose conversion type", ["Length", "Weight", "Temperature"])

#input value (user se value lane ke liye)
value =st.number_input("Enter the value", value=0.0,min_value=0.0, step=0.1)

#layout for unit selection (from aur to unist select karna ka setup)
col1, col2 = st.columns(2)



if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("from", ["meters", "kilograms", "centimeters","milimeters","miles","yards","inches","feet"])
    with col2:
        to_unit = st.selectbox("to", ["meters", "kilograms", "centimeters","milimeters","miles","yards","inches","feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("from", ["kilograms", "Grams", "Milligrams","Pounds","Ounces"])
    with col2:
        to_unit = st.selectbox("to", ["kilograms", "Grams", "Milligrams","Pounds","Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("from", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("to", ["Celsius", "Fahrenheit", "Kelvin"])



#converted functions (alag alag conversion functions)
def convertor_length(value, from_unit, to_unit):
    # length units ko conversion factor ke zariye convert karna
    conversion_factors = {
        'meters':1,
        'kilometers': 0.001, 
        'centermeters': 100, 
        'milimeters': 1000,
        'miles': 0.000621371, 
        'yards': 1.09361, 
        'feet': 3.28084, 
        'inches': 39.3701
    }

    # convert the value to meters first
    value_in_meters = value * conversion_factors[from_unit]
 
    # convert the value from meters to the desired unit
    converted_value = value_in_meters / conversion_factors[to_unit]

    return converted_value


# convert the value to grams first
def value_in_grams(value, from_unit,to_unit):
    # weight units ko conversion factor ke zariye convert karna
    weight_units = {
        'kilograms': 1000, 'grams': 1, 'milligrams': 1000000, 'pounds': 2.20462, 'ounces': 35.274
    }
    # convert the value in grams to the desired unit
    value_in_grams = value * weight_units[from_unit]
    converted_value = value_in_grams / weight_units [to_unit]

    return converted_value

def temp_convertor(value, from_unit, to_unit):
    # Temperature conversion logic
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value



# convert button (conversion krne ka button)
if st.button("🧑‍💻convert"):
    if conversion_type == "Length":
        result = convertor_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = value_in_grams(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_convertor(value, from_unit, to_unit)

    # Result ko dikhana (conversion ka result show karna)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer (neeche footer message)
st.markdown("<div class'footer'>created with ❤️ by mariya munawar /div>", unsafe_allow_html=True)











    

    








