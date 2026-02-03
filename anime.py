import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Anime Hub",
    page_icon="🎌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .anime-card {
        background-color: #1e2127;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px solid #ff6b6b;
    }
    .anime-title {
        color: #ff6b6b;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .genre-tag {
        background-color: #ff6b6b;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        margin: 5px;
        display: inline-block;
        font-size: 12px;
    }
    .stButton>button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff5252;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# API Functions (using Jikan API - unofficial MyAnimeList API)
@st.cache_data(ttl=3600)
def fetch_top_anime(page=1, limit=20):
    """Fetch top anime from Jikan API"""
    try:
        url = f"https://api.jikan.moe/v4/top/anime?page={page}&limit={limit}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching anime data: {e}")
        return None

@st.cache_data(ttl=3600)
def search_anime(query):
    """Search for anime by name"""
    try:
        url = f"https://api.jikan.moe/v4/anime?q={query}&limit=20"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error searching anime: {e}")
        return None

@st.cache_data(ttl=3600)
def fetch_anime_details(anime_id):
    """Fetch detailed information about a specific anime"""
    try:
        url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching anime details: {e}")
        return None

@st.cache_data(ttl=3600)
def fetch_seasonal_anime(year, season):
    """Fetch seasonal anime"""
    try:
        url = f"https://api.jikan.moe/v4/seasons/{year}/{season}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error fetching seasonal anime: {e}")
        return None

def display_anime_card(anime):
    """Display an anime card with information"""
    with st.container():
        col1, col2 = st.columns([1, 3])
        
        with col1:
            # Display anime image
            if anime.get('images', {}).get('jpg', {}).get('large_image_url'):
                st.image(anime['images']['jpg']['large_image_url'], use_container_width=True)
        
        with col2:
            # Title
            title = anime.get('title', 'Unknown Title')
            st.markdown(f"### 🎌 {title}")
            
            # English title
            if anime.get('title_english'):
                st.markdown(f"*{anime['title_english']}*")
            
            # Metadata row
            meta_col1, meta_col2, meta_col3, meta_col4 = st.columns(4)
            
            with meta_col1:
                score = anime.get('score', 'N/A')
                st.metric("⭐ Score", score)
            
            with meta_col2:
                episodes = anime.get('episodes', 'N/A')
                st.metric("📺 Episodes", episodes)
            
            with meta_col3:
                year = anime.get('year', 'N/A')
                st.metric("📅 Year", year)
            
            with meta_col4:
                status = anime.get('status', 'N/A')
                st.metric("📊 Status", status)
            
            # Genres
            if anime.get('genres'):
                st.markdown("**Genres:**")
                genre_text = " • ".join([g['name'] for g in anime['genres'][:5]])
                st.markdown(f"🏷️ {genre_text}")
            
            # Synopsis
            if anime.get('synopsis'):
                with st.expander("📖 Synopsis"):
                    st.write(anime['synopsis'])
            
            # Action buttons
            btn_col1, btn_col2, btn_col3 = st.columns(3)
            
            with btn_col1:
                anime_id = anime.get('mal_id')
                if st.button(f"❤️ Add to Favorites", key=f"fav_{anime_id}"):
                    if anime_id not in st.session_state.favorites:
                        st.session_state.favorites.append(anime_id)
                        st.success(f"Added {title} to favorites!")
                    else:
                        st.info("Already in favorites!")
            
            with btn_col2:
                if anime.get('url'):
                    st.link_button("🔗 View on MyAnimeList", anime['url'])
            
            with btn_col3:
                if anime.get('trailer', {}).get('url'):
                    st.link_button("🎬 Watch Trailer", anime['trailer']['url'])
        
        st.divider()

# Sidebar
with st.sidebar:
    st.title("🎌 Anime Hub")
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🔍 Search", "📅 Seasonal", "⭐ Top Rated", "❤️ Favorites"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Filters (for applicable pages)
    if page in ["⭐ Top Rated", "📅 Seasonal"]:
        st.subheader("Filters")
        
        if page == "📅 Seasonal":
            current_year = datetime.now().year
            year = st.selectbox("Year", range(current_year, 1989, -1), index=0)
            season = st.selectbox("Season", ["winter", "spring", "summer", "fall"])
    
    st.markdown("---")
    st.markdown("### About")
    st.info("Discover and explore anime from MyAnimeList database. Data provided by Jikan API.")

# Main content area
st.title("🎌 Anime Hub - Your Anime Discovery Platform")

# Home Page
if page == "🏠 Home":
    st.header("🔥 Trending Anime")
    st.markdown("Explore the most popular anime titles right now!")
    
    data = fetch_top_anime(page=1, limit=10)
    
    if data and data.get('data'):
        for anime in data['data']:
            display_anime_card(anime)
    else:
        st.warning("Unable to load anime data. Please try again later.")

# Search Page
elif page == "🔍 Search":
    st.header("🔍 Search Anime")
    
    search_query = st.text_input("Enter anime name:", placeholder="e.g., Naruto, One Piece, Death Note...")
    
    if search_query:
        with st.spinner("Searching..."):
            data = search_anime(search_query)
        
        if data and data.get('data'):
            st.success(f"Found {len(data['data'])} results for '{search_query}'")
            
            for anime in data['data']:
                display_anime_card(anime)
        else:
            st.warning("No results found. Try a different search term.")
    else:
        st.info("👆 Enter an anime name to start searching!")

# Seasonal Page
elif page == "📅 Seasonal":
    st.header(f"📅 Seasonal Anime - {season.capitalize()} {year}")
    
    data = fetch_seasonal_anime(year, season)
    
    if data and data.get('data'):
        st.success(f"Found {len(data['data'])} anime for {season.capitalize()} {year}")
        
        for anime in data['data']:
            display_anime_card(anime)
    else:
        st.warning("Unable to load seasonal anime data.")

# Top Rated Page
elif page == "⭐ Top Rated":
    st.header("⭐ Top Rated Anime of All Time")
    
    # Pagination
    page_num = st.number_input("Page", min_value=1, max_value=100, value=1, step=1)
    
    data = fetch_top_anime(page=page_num, limit=25)
    
    if data and data.get('data'):
        st.success(f"Showing top anime - Page {page_num}")
        
        for anime in data['data']:
            display_anime_card(anime)
        
        # Pagination controls
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if page_num > 1:
                if st.button("⬅️ Previous Page"):
                    st.rerun()
        with col3:
            if st.button("Next Page ➡️"):
                st.rerun()
    else:
        st.warning("Unable to load top anime data.")

# Favorites Page
elif page == "❤️ Favorites":
    st.header("❤️ Your Favorite Anime")
    
    if st.session_state.favorites:
        st.success(f"You have {len(st.session_state.favorites)} favorites")
        
        if st.button("🗑️ Clear All Favorites"):
            st.session_state.favorites = []
            st.rerun()
        
        for anime_id in st.session_state.favorites:
            with st.spinner(f"Loading anime {anime_id}..."):
                details = fetch_anime_details(anime_id)
            
            if details and details.get('data'):
                anime = details['data']
                display_anime_card(anime)
                
                if st.button(f"Remove from Favorites", key=f"remove_{anime_id}"):
                    st.session_state.favorites.remove(anime_id)
                    st.rerun()
    else:
        st.info("You haven't added any favorites yet! Browse anime and click '❤️ Add to Favorites' to save them here.")
        
        if st.button("🏠 Go to Home"):
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Powered by <a href='https://jikan.moe/' target='_blank'>Jikan API</a> (Unofficial MyAnimeList API)</p>
        <p>Made with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)

