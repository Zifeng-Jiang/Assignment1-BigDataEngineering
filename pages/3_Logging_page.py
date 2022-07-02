import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Airbus Ship Detection')
data = pd.read_excel('log.xlsx')

st.subheader('Successed call vs Failed call')
success = data['Success'][0]
fail = data['Fail'][0]
labels = ['success', 'fail']
sizes = [success, fail]
fig, ax = plt.subplots()
ax.pie(x = sizes, labels = labels, shadow = True, autopct='%1.1f%%')
plt.title("Successed percentage vs Failed percentage")
st.pyplot(fig)

st.subheader('Number of Calls for each of the 5 APIs')
run_length_decode = data['run_length_decode'][0]
image_number_of_ships = data['image_number_of_ships'][0]
ship_nonship_image = data['ship_nonship_image'][0]
image_and_masks = data['image_and_masks'][0]
num_ship_in_image = data['num_ship_in_image'][0]
apis = [run_length_decode, image_number_of_ships, ship_nonship_image, image_and_masks, num_ship_in_image]
st.write('API-1: run_length_decode')
st.write('API-2: image_number_of_ships')
st.write('API-3: ship_nonship_image')
st.write('API-4: image_and_masks')
st.write('API-5: num_ship_in_image')
fig, ax = plt.subplots()
ax.grid(color = 'gray', linestyle = 'dashed')
ax.bar(['API-1', 'API-2', 'API-3', 'API-4', 'API-5'], 
            apis, color = sns.color_palette())
for a,b in zip(['API-1', 'API-2', 'API-3', 'API-4', 'API-5'],
            apis):
    plt.text(a, b + 0.5, '%.0f' % b, ha = 'center', va = 'bottom',fontsize = 8)
plt.title("Number of Calls of the 5 APIs")
plt.ylabel('Number of Calls')
st.pyplot(fig)