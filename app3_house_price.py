import streamlit as st
import joblib

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------------
# LOAD MODEL
# -----------------------------------

model = joblib.load("house_price_model.pkl")


# -----------------------------------
# TITLE
# -----------------------------------

st.title("🏠 House Price Predictor")

st.write(
    "Enter the details of your house and our Machine Learning model "
    "will estimate its price."
)

st.divider()


# -----------------------------------
# HOUSE INFORMATION
# -----------------------------------

st.header("🏡 Property Information")

col1, col2, col3 = st.columns(3)

with col1:
    area = st.slider(
        "📐 Area (sq ft)",
        500,
        15000,
        2000,
        step=100
    )

with col2:
    bedrooms = st.number_input(
        "🛏️ Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

with col3:
    bathrooms = st.number_input(
        "🚿 Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )


col1, col2, col3 = st.columns(3)

with col1:
    stories = st.number_input(
        "🏢 Stories",
        min_value=1,
        max_value=10,
        value=2
    )

with col2:
    parking = st.number_input(
        "🚗 Parking Spaces",
        min_value=0,
        max_value=10,
        value=1
    )

with col3:
    furnishingstatus = st.selectbox(
        "🛋️ Furnishing Status",
        [
            "furnished",
            "semi-furnished",
            "unfurnished"
        ]
    )


# -----------------------------------
# HOUSE FEATURES
# -----------------------------------

st.header("✨ House Features")

col1, col2, col3 = st.columns(3)

with col1:

    mainroad = st.selectbox(
        "🛣️ Main Road",
        ["yes", "no"]
    )

    guestroom = st.selectbox(
        "🛏️ Guest Room",
        ["yes", "no"]
    )


with col2:

    basement = st.selectbox(
        "🏚️ Basement",
        ["yes", "no"]
    )

    hotwaterheating = st.selectbox(
        "🔥 Hot Water Heating",
        ["yes", "no"]
    )


with col3:

    airconditioning = st.selectbox(
        "❄️ Air Conditioning",
        ["yes", "no"]
    )

    prefarea = st.selectbox(
        "📍 Preferred Area",
        ["yes", "no"]
    )


st.divider()


# -----------------------------------
# CONVERT YES / NO
# -----------------------------------

mainroad = 1 if mainroad == "yes" else 0
guestroom = 1 if guestroom == "yes" else 0
basement = 1 if basement == "yes" else 0
hotwaterheating = 1 if hotwaterheating == "yes" else 0
airconditioning = 1 if airconditioning == "yes" else 0
prefarea = 1 if prefarea == "yes" else 0


# -----------------------------------
# FURNISHING ENCODING
# -----------------------------------

furnished = 1 if furnishingstatus == "furnished" else 0

semi_furnished = (
    1 if furnishingstatus == "semi-furnished" else 0
)

unfurnished = (
    1 if furnishingstatus == "unfurnished" else 0
)


# -----------------------------------
# PREDICTION
# -----------------------------------

st.header("🔮 Get Your House Price")

if st.button(
    "🚀 Predict House Price",
    type="primary",
    use_container_width=True
):

    input_data = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnished,
        semi_furnished,
        unfurnished
    ]]

    prediction = model.predict(input_data)

    predicted_price = prediction[0]

    st.success("Prediction completed successfully! 🎉")

    st.metric(
        "🏠 Estimated House Price",
        f"₹ {predicted_price:,.0f}"
    )


# -----------------------------------
# ABOUT MODEL
# -----------------------------------

st.divider()

with st.expander("ℹ️ About this project"):

    st.write("""
    This application uses Machine Learning to predict house prices.

    Model:
    Linear Regression

    Technology:
    Python + Scikit-learn + Streamlit

    The model was trained using house features such as:

    • Area
    • Bedrooms
    • Bathrooms
    • Stories
    • Parking
    • Main Road
    • Guest Room
    • Basement
    • Air Conditioning
    • Furnishing Status
    """)