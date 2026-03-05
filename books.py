import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
# Note: Keep your API Key secure!
API_KEY = "AIzaSyBXe_0wgBTYF7dDZu-YeLTs_lEitckdXkY" 
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Hidden Gems of Santa Cruz", layout="wide", page_icon="☀️")

# --- CUSTOM STYLING (The "Happy Palette") ---
st.markdown("""
    <style>
    /* Main Background: Pastel Sunny Yellow */
    .stApp {
        background-color: #FFF9E3;
    }
    
    /* Headers */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2D5A27 !important; 
        font-family: 'Trebuchet MS', sans-serif;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.5);
    }

    /* Cards: Baby Pink and Baby Green accents */
    .gem-card {
        padding: 0px; 
        border-radius: 20px; 
        background-color: white; 
        box-sizing: border-box;
        border: 4px solid #FADADD; /* Baby Pink Border */
        margin-bottom: 30px;
        overflow: hidden; /* Keeps image corners rounded */
        transition: transform 0.3s;
    }
    .gem-card:hover {
        transform: scale(1.02);
        border-color: #C1E1C1; /* Change to Baby Green on hover */
    }
    
    .card-text {
        padding: 20px;
    }

    /* Button: Sunshine Yellow/Orange */
    .stButton>button {
        background-color: #FFD700;
        color: #444;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        padding: 10px 24px;
        border: 2px solid #FFCC00;
    }
    .stButton>button:hover {
        background-color: #FFEA00;
        color: #000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP HEADER ---
st.title("☀️ Hidden Gems of Santa Cruz")
st.markdown("#### Discover the happiest local secrets of the Central Coast!")

# --- DISPLAY FUNCTION ---
def display_gem(name, description, why_special, image_url):
    with st.container():
        st.markdown(f"""
        <div class="gem-card">
            <img src="{image_url}" style="width:100%; height:250px; object-fit:cover;">
            <div class="card-text">
                <h3 style="margin-top:0;">{name}</h3>
                <p><b>The Vibe:</b> {description}</p>
                <p style="color: #666;"><i>✨ {why_special}</i></p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- CONTENT ---
col1, col2 = st.columns(2)

with col1:
    st.header("💗 Beach Bliss")
    display_gem(
        "Panther Beach", 
        "A secluded beach north of Davenport with a dramatic rock arch.", 
        "It feels like a private island and features a hidden 'Hole in the Wall' passage.",
        "https://images.unsplash.com/photo-1505118380757-91f5f5832de0?auto=format&fit=crop&w=800&q=80"
    )
    
    st.header("🍵 Cozy Sips")
    display_gem(
        "11th Hour Coffee", 
        "A lush, plant-filled roastery in downtown Santa Cruz.", 
        "The interior feels like a greenhouse—perfect for a sunny afternoon chat.",
        "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=800&q=80"
    )

with col2:
    st.header("🌿 Nature Escapes")
    display_gem(
        "Pogonip Koi Pond", 
        "A hidden pond tucked deep within the Pogonip redwood forest.", 
        "Finding it feels like a scavenger hunt, and the mossy atmosphere is pure magic.",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=800&q=80"
    )

    st.header("🥪 Happy Eats")
    display_gem(
        "Steamer Lane Supply", 
        "A small window-serve shack right at the lighthouse point.", 
        "Grab a taco and watch world-class surfers while the sun hits the water.",
        "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80"
    )

# --- AI GENERATOR SECTION ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.header("✨ Need a New Adventure?")
st.write("Let the sunshine santa cruz AI find a fresh spot for you!")

if st.button("Generate Happy Suggestion"):
    try:
        # Note: 'gemini-1.5-flash' is the current stable name
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = (
            "Suggest one unique, specific hidden gem location in Santa Cruz, California. "
            "Focus on places that are upbeat, beautiful, or peaceful. "
            "Output: Name: [Name]\nDescription: [Short description]\nReason: [Why it's special]"
        )
        
        with st.spinner("Searching for sunbeams..."):
            response = model.generate_content(prompt)
            st.balloons()
            st.info(response.text)
            
    except Exception as e:
        st.error(f"Oops! Check your API key. Error: {e}")

# --- FOOTER ---
st.markdown("<div style='text-align: center; color: #999; padding: 50px;'>Made with 💛 for Santa Cruz explorers.</div>", unsafe_allow_html=True)