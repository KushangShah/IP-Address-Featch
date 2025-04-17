import streamlit as st
import requests


# Copy past this in terminal:

# python3 -m venv venv

# source venv/bin/activate

# streamlit run "manin.py" 


# Function to fetch IP information
def get_ip_info(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            return {
                "IP Address": ip_address,
                "Country": data.get('country', 'N/A'),
                "Region": data.get('regionName', 'N/A'),
                "City": data.get('city', 'N/A'),
                "ZIP Code": data.get('zip', 'N/A'),
                "Timezone": data.get('timezone', 'N/A'),
                "ISP": data.get('isp', 'N/A'),
                "Organization": data.get('org', 'N/A'),
                "Latitude": data.get('lat', 'N/A'),
                "Longitude": data.get('lon', 'N/A'),
            }
        else:
            return {"Error": "Unable to fetch data for the given IP address"}
    except Exception as e:
        return {"Error": str(e)}

# Streamlit App
st.title("IP Address Information Finder")
st.write("Enter an IP address to get details about its geolocation, ISP, and more.")

# Input field for IP address
ip_address = st.text_input("Enter IP Address:", "")

if st.button("Get Info"):
    if ip_address:
        with st.spinner("Fetching data..."):
            ip_info = get_ip_info(ip_address)
        if "Error" in ip_info:
            st.error(ip_info["Error"])
        else:
            st.success("IP Information Retrieved Successfully!")
            # Display the information as a table
            st.table(ip_info)
    else:
        st.warning("Please enter a valid IP address.")
