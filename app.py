import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("MateoA")
client1.on_message = on_message



st.title("HAZ BAILAR A BMO!")
   
if st.button('BAILAR'):
    st.audio(audio_bytes, format="audio/mp3")
    act1="¡A BAILAR!"
    client1= paho.Client("MateoA")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("BMO", message)
    
 
else:
    st.write('')




