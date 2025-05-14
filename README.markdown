# Betplay Betting Assistant

A web application that uses statistics, probability, and mathematics to identify the best betting opportunities on Betplay, leveraging data from `the-odds-api.com`. Designed for users like Aymen to maximize winning chances through data-driven recommendations.

## Features

- **Real-time Odds**: Fetches sports events and odds from `the-odds-api.com`.
- **Statistical Analysis**: Uses regression and expected value to find bets with positive value.
- **Recommendations**: Displays bets with the highest winning probability (e.g., moneyline, over/under).
- **Simulated Betting**: Allows users to place virtual bets and track performance.
- **Responsive UI**: Built with Tailwind CSS, inspired by Betplay's green and orange design.

## Technologies

- **Backend**: Python, Flask, Flask-SocketIO, SQLite, pandas, scikit-learn
- **Frontend**: HTML, Tailwind CSS, JavaScript, Chart.js
- **API**: `the-odds-api.com` for sports data
- **Environment**: python-dotenv for secure API key management

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/betplay_betting_assistant
   cd betplay_betting_assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` with your `the-odds-api.com` API key:
     ```
     ODDS_API_KEY=your_api_key
     ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## Usage

- **View Recommendations**: Browse suggested bets with positive expected value.
- **Place Bets**: Use the "Apostar" button to simulate bets with virtual currency.
- **Track Performance**: Check your betting history and statistics (hit rate, ROI) in the dashboard.

## Screenshots

![Dashboard](screenshots/dashboard.png)
![Statistics](screenshots/stats.png)

## Project Structure

```
betplay_betting_assistant/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   ├── css/                # Tailwind CSS
│   └── js/                 # JavaScript
├── screenshots/            # UI screenshots
├── data/
│   └── db.sqlite           # SQLite database
├── requirements.txt        # Dependencies
├── .gitignore             # Excluded files
├── .env.example           # API key template
├── README.md              # Documentation
```

## License

MIT License

## Contact

For issues or inquiries, open an issue on GitHub.