# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 17:10:00 2025

@author: groja
"""

import streamlit as st
import time
import random

choices_loading = ['Analizando tus gustos, espera un poquito chanchi 🐖', 'Aquí vienen tus resultados chanchi, aguarda 🐖',
                   'Mmmm, interesante... 🐖','QUEEEEEE... veamos que se viene... 🐖']
# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Page navigation handler
def navigate_to(page_name):
    st.session_state.page = page_name

# Define pages
def home():
    st.title("🎉🎉🎉 Hoy es tu cumpleaños!!!")
    st.write("El cumpleaños de la niña operada más linda de todo el universo🌌✨")
    st.image("operada.jpg",width=350)
    if st.button("Vamos a ver que hay de regalo...🤔",key=1):
        navigate_to("regalo")
    # if st.button("Go to Contact Page"):
    #     navigate_to("contact")

def regalo():
    st.title("ℹ️ Veo que te gusta ir de compras...")
    st.write("¿Tienes una o más de una multitienda favorita?")
    col1, col2,col3 = st.columns([1, 2, 1])

    with col1:
        st.image("ripley.png", width=100)
    
    with col2:
        if st.button("Ripley!",key=3):
            navigate_to("ripley")
            # st.success("Button clicked!")
    col1, col2,col3= st.columns([1, 2, 1])

    with col1:
        st.image("falabella.png", width=100)
    
    with col2:
        if st.button("Fallabella!",key=5):
            navigate_to("falabella")
    col1, col2,col3= st.columns([1, 2, 1])

    with col1:
        st.image("paris.png", width=100)
    
    with col2:
        if st.button("Paris!",key=6):
            navigate_to("paris")
            # st.success("Button clicked!")
            
    
    if st.button("Tengo más de una...🤔🤔🤔🤔"):
        navigate_to("distribution")

    if st.button("Volver a inicio"):
        navigate_to("home")

def contact():
    st.title("📞 Contact Page")
    st.write("This is the contact page.")
    if st.button("Back to Home"):
        navigate_to("home")
    if st.button("Go to regalo Page"):
        navigate_to("regalo")


def ripley():
    st.title("Te ganaste una gift card de $100.000 en RIPLEY!!🥳🥳🥳")
    st.write("FELICIDADES!! Te amo infinito!")
    st.balloons()
    st.image("giftcard_ripley.jpg", width=500)
    if st.button("Volver a inicio"):
        navigate_to("home")
        
def falabella():
    st.title("Te ganaste una gift card de $100.000 en FALABELLA!!🥳🥳🥳")
    st.write("FELICIDADES!! Te amo infinito!")
    st.balloons()
    st.image("giftcard_falabella.jpeg", width=500)
    if st.button("Volver a inicio"):
        navigate_to("home")
        
def paris():
    st.title("Te ganaste una gift card de $100.000 en PARIS!!🥳🥳🥳")
    st.write("FELICIDADES!! Te amo infinito!")
    st.balloons()
    st.image("giftcard_cencosud.png", width=500)
    if st.button("Volver a inicio"):
        navigate_to("home")

def distribution():
    st.title("Calcula tus gustos chanchi!!❤️❤️")

    st.markdown("Ajusta tus gustos de cada multitienda entre 0 y 100, ¿Cuál te gusta más?🤔")

    ripley = st.slider("Ripley", 0, 100, 33)
    falabella = st.slider("Falabella", 0, 100, 33)
    paris = st.slider("Paris", 0, 100, 34)
    
    if st.button("Submit Distribution"):
        with st.spinner(random.choice(choices_loading)):
            time.sleep(3)  # simulate processing delay
            scores = {"Ripley": ripley, "Falabella": falabella, "Paris": paris}
            total_score = sum(scores.values())
    
            if total_score == 0:
                st.warning("All scores are zero. Splitting equally.")
                final_blocks = {k: 1 for k in scores}  # 4 blocks total
            else:
                # Step 1: Compute raw shares
                raw_shares = {k: (v / total_score) * 4 for k, v in scores.items()}  # 4 chunks = 100k/25k
    
                # Step 2: Round down to floor
                floored_blocks = {k: int(v) for k, v in raw_shares.items()}
    
                # Step 3: Distribute remaining blocks
                blocks_assigned = sum(floored_blocks.values())
                blocks_remaining = 4 - blocks_assigned
    
                # Compute residuals
                residuals = {k: raw_shares[k] - floored_blocks[k] for k in scores}
                sorted_residuals = sorted(residuals.items(), key=lambda x: x[1], reverse=True)
    
                for i in range(blocks_remaining):
                    floored_blocks[sorted_residuals[i][0]] += 1
    
                final_blocks = floored_blocks
    
            # Final display
            st.subheader("📊 GIFTCARD(s) DE REGALO!! Asociado a tus gustos:")
            st.balloons()
            for k, b in final_blocks.items():
                st.write(f"**{k}**: ${b * 25000:,.0f}")
            st.subheader("Te amo infinito! ❤️❤️")


    if st.button("Volver a inicio"):
        navigate_to("home")

# Page router
if st.session_state.page == "home":
    home()
elif st.session_state.page == "regalo":
    regalo()
elif st.session_state.page == "distribution":
    distribution()
elif st.session_state.page == "ripley":
    ripley()
elif st.session_state.page == "falabella":
    falabella()
elif st.session_state.page == "paris":
    paris()
