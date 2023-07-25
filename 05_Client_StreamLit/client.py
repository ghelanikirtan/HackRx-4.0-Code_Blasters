import streamlit as st
import requests
import time

st.title('URL Submission')

url = st.text_input('Enter your URL here:')
url = '"'+url+'"'
submit_button = st.button('Submit')

if submit_button:
    response = requests.post('https://massive-imp-on.ngrok-free.app/test-it-up', url)
    if response.status_code == 200:
        data = response.json()
        value = data['Rating'][0][0]
        # st.write(f'{value}')
        value_0_to_10 = round(value * 10,2)
        st.write('URL successfully submitted! Server response:')
        st.write(f'Value (0-10): {value_0_to_10}')
        # Create a progress bar
        progress_bar = st.progress(0)
        for i in range(101):
            # Update the progress bar with each iteration.
            progress_bar.progress(i)
            if i > value_0_to_10 * 10:
                break
            time.sleep(0.01)        
        # fig, ax = plt.subplots()
        # ax.pie([value_0_to_10, 10 - value_0_to_10], colors=['blue', 'white'], startangle=90, counterclock=False)
        # ax.add_artist(plt.Circle((0,0),0.70,fc='white'))
        # st.pyplot(fig)        
    else:
        st.write('Submission failed. Please try again.')
