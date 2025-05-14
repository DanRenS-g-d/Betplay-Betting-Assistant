from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
import sqlite3
import os
from dotenv import load_dotenv

app = Flask(__name__)
socketio = SocketIO(app)
load_dotenv()

API_KEY = os.getenv('ODDS_API_KEY')
ODDS_API_URL = 'https://api.the-odds-api.com/v4/sports/soccer_colombia_liga_aguila/odds'

def get_odds():
    response = requests.get(ODDS_API_URL, params={
        'apiKey': API_KEY,
        'regions': 'us',
        'markets': 'h2h,totals',
        'oddsFormat': 'american'
    })
    return response.json()

def calculate_implied_probability(odds):
    if odds > 0:
        return 100 / (odds + 100)
    return abs(odds) / (abs(odds) + 100)

def calculate_ev(true_prob, odds, stake=100):
    payout = stake * (odds / 100) if odds > 0 else stake * (100 / abs(odds))
    return (true_prob * payout) - stake

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/odds', methods=['GET'])
def api_odds():
    odds_data = get_odds()
    recommendations = []
    for event in odds_data:
        home_team = event['home_team']
        away_team = event['away_team']
        h2h = event['bookmakers'][0]['markets'][0]['outcomes']
        home_odds = h2h[0]['price']
        away_odds = h2h[1]['price']
        
        # Modelo simple: Probabilidad real basada en promedio histórico
        true_prob_home = 0.5  # Placeholder, usar regresión
        imp_prob_home = calculate_implied_probability(home_odds)
        ev_home = calculate_ev(true_prob_home, home_odds)
        
        if ev_home > 0:
            recommendations.append({
                'match': f"{home_team} vs {away_team}",
                'bet': f"{home_team} (+{home_odds})",
                'ev': round(ev_home, 2)
            })
    
    return jsonify(recommendations)

@socketio.on('connect')
def handle_connect():
    socketio.emit('update', {'message': 'Connected to real-time odds'})

if __name__ == '__main__':
    socketio.run(app, debug=True)