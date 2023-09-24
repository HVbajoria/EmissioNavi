import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def calculate_motorcycle_emissions(distance, num_days):
    CO2_PER_KM = 0.129
    total_distance = distance * num_days
    carbon_emissions = total_distance * CO2_PER_KM
    return carbon_emissions

def calculate_car_emissions(distance, num_days):
    CO2_PER_KM = 0.1808
    AVG_DISTANCE_PER_DAY = 40.0
    total_distance = distance * num_days
    carbon_emissions = (total_distance / AVG_DISTANCE_PER_DAY) * CO2_PER_KM
    return carbon_emissions

def calculate_public_trans_emissions(distance, num_days):
    CO2_PER_KM = 0.09
    total_distance = distance * num_days
    carbon_emissions = total_distance * CO2_PER_KM
    return carbon_emissions


def gradient_text(text, color1, color2):
    gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 42px;
    """
    return f'<span style="{gradient_css}">{text}</span>'

color1 = "#0d3270"
color2 = "#0fab7b"
text = "Commute Insight"

styled_text = gradient_text(text, color1, color2)
st.write(f"<div>{styled_text}</div>", unsafe_allow_html=True)

st.write('Calculate and reduce your carbon footprint for your daily commute using simple machine learning algorithms.')

st.header(':green[Enter your commute details:]')
data = []
transportation_modes = ['Public transportation', 'Car', 'Motorcycle']
total_emissions = 0

distance_unit = st.selectbox('Distance Unit', ['Kilometers', 'Miles'])

for mode in transportation_modes:
    st.subheader(f'{mode} Commute Details:')
    distance_label = f'Distance ({distance_unit.lower()}) for {mode}:'
    distance_conversion = 1.0

    if distance_unit == 'Miles':
        distance_conversion = 0.621371
        distance_label = f'Distance ({distance_unit.lower()}) for {mode}:'

    distance = st.number_input(distance_label, min_value=0.0, max_value=1000.0, step=0.1, key=f'{mode}_distance')
    num_days = st.number_input(f'Number of days per week for {mode}:', min_value=0, max_value=7, step=1, key=f'{mode}_days')
    distance *= distance_conversion
    if distance < 0 or num_days < 0:
        st.error('Invalid input. Distance and number of days should be non-negative.')
        continue

    if mode == 'Car':
        carbon_emissions = calculate_car_emissions(distance, num_days)
    elif mode == 'Motorcycle':
        carbon_emissions = calculate_motorcycle_emissions(distance, num_days)
    elif mode == 'Public transportation':
        carbon_emissions = calculate_public_trans_emissions(distance, num_days)

    total_emissions += carbon_emissions
    data.append({'Transportation Mode': mode, 'CO2 Emissions (kg)': carbon_emissions})

df = pd.DataFrame(data)
if st.button("Calculate: "):
    st.header('Results:')

    if total_emissions > 10:
        st.subheader(f'Net :red[carbon] :red[emissions]: :red[{format(total_emissions, ".2f")} kg of CO2]')
    else:
        st.subheader(f'Net :green[carbon] :green[emissions]: :green[{format(total_emissions, ".2f")} kg of CO2]')

    max_emissions = max(data, key=lambda x: x['CO2 Emissions (kg)'])['CO2 Emissions (kg)']

    fig, ax = plt.subplots()
    ax.bar(df['Transportation Mode'], df['CO2 Emissions (kg)'])
    ax.set_xlabel('Transportation Mode')
    ax.set_ylabel('CO2 Emissions (kg)')
    ax.set_title('CO2 Emissions by Transportation Mode')

    for i, value in enumerate(df['CO2 Emissions (kg)']):
        ax.text(i, value + max_emissions * 0.02, f'{value:.2f}', ha='center')

    ax.set_ylim(0, max_emissions * 1.4)
    st.pyplot(fig)

    st.subheader('\n\nSustainable transportation recommendations:')
    if total_emissions > 0:
        st.write(':red[Consider the following more sustainable transportation options::]')
        if any(mode in ['Car', 'Motorcycle'] for mode in transportation_modes):
            st.write(':red[- Use public transportation or carpooling when possible:]')
            st.write(':red[- Switch to an electric vehicle:]')
        else:
            st.write(':green[- Keep up the good work!:]')
    else:
        st.write(':green[Your carbon emissions are negligible. Keep up the good work!:]')

footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/harshavardhan-bajoria/" target="_blank">Harshavardhan Bajoria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
