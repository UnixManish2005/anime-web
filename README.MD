# 🎌 Anime Hub - Streamlit Anime Discovery Platform

A beautiful and interactive web application for discovering, searching, and exploring anime content built with Streamlit and powered by the Jikan API (unofficial MyAnimeList API).

## Features
# Anime WebSite 
### 🏠 Home Page
- Browse trending and popular anime titles
- View detailed information about each anime
- Beautiful card-based layout with images
 
### 🔍 Search Functionality
- Search for any anime by name
- Real-time search results
- Comprehensive anime information display

### 📅 Seasonal Anime
- Browse anime by season and year
- Filter by Winter, Spring, Summer, or Fall
- Discover new seasonal releases

### ⭐ Top Rated
- View the highest-rated anime of all time
- Pagination support for browsing through rankings
- Sort by MyAnimeList scores

### ❤️ Favorites System
- Add anime to your personal favorites list
- Manage and view your saved anime
- Quick access to your favorite titles

## Anime Information Displayed

For each anime, the app shows:
- **Cover Image**: High-quality anime poster
- **Title**: Both Japanese and English titles
- **Score**: MyAnimeList rating
- **Episodes**: Total episode count
- **Year**: Release year
- **Status**: Airing status (Finished, Airing, Upcoming)
- **Genres**: Anime genres and categories
- **Synopsis**: Full plot description
- **Links**: Direct links to MyAnimeList and trailers

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd anime_streaming_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and navigate to `http://localhost:8501`
   - The app should automatically open in your default browser

## Project Structure

```
anime_streaming_app/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Dependencies

- **streamlit**: Web application framework
- **requests**: HTTP library for API calls
- **pandas**: Data manipulation (for future enhancements)

## API Information

This application uses the **Jikan API** (https://jikan.moe/), which is an unofficial MyAnimeList API. The API is free to use and doesn't require authentication for basic features.

### API Features Used:
- Top anime rankings
- Anime search
- Seasonal anime listings
- Detailed anime information
- Character and staff information

### API Rate Limits:
- The Jikan API has rate limiting in place
- Requests are cached for 1 hour to minimize API calls
- Please be respectful of the API's resources

## Usage Tips

1. **Browsing**: Start on the Home page to see trending anime
2. **Searching**: Use the Search page to find specific titles
3. **Exploring**: Check out Seasonal anime to discover new releases
4. **Saving**: Click "Add to Favorites" to save anime you like
5. **Learning**: Read synopses and check ratings before watching

## Customization

### Modify Styling
Edit the CSS in the `st.markdown()` section of `app.py` to change:
- Colors and themes
- Card layouts
- Button styles
- Typography

### Add Features
Potential enhancements:
- User authentication
- Persistent storage (database)
- Anime recommendations
- Character information pages
- Watch history tracking
- Community ratings and reviews

## Troubleshooting

### Common Issues:

1. **API Connection Errors**
   - Check your internet connection
   - The Jikan API may be temporarily unavailable
   - Wait a moment and try again

2. **Slow Loading**
   - The API has rate limits
   - Cache is implemented to speed up repeated requests
   - Consider reducing the number of items loaded per page

3. **Missing Images**
   - Some anime may not have high-quality images
   - This is a data limitation from MyAnimeList

## Screenshots

The app includes:
- Responsive design that works on desktop and mobile
- Dark theme optimized for viewing
- Intuitive navigation sidebar
- Rich anime cards with images and metadata
- Interactive buttons and links

## Contributing

Feel free to fork this project and add your own features! Some ideas:
- Add more filtering options
- Implement user reviews
- Create anime comparison features
- Add streaming service links
- Include manga information

## License

This project is open source and available for educational purposes.

## Credits

- **API**: Jikan API (https://jikan.moe/)
- **Data Source**: MyAnimeList (https://myanimelist.net/)
- **Framework**: Streamlit (https://streamlit.io/)

## Disclaimer

This application is for educational and personal use only. All anime data and images are property of their respective owners and MyAnimeList. This is not an official MyAnimeList application.

---

**Enjoy discovering amazing anime! 🎌✨**