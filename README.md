# 🚗 Car Price Predictor

An intelligent machine learning web application that estimates used car prices with high accuracy. Built with LightGBM and deployed as a Flask web app with an intuitive user interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![LightGBM](https://img.shields.io/badge/ML-LightGBM-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Overview

This project predicts used car prices using a machine learning model trained on over 143,000 vehicles. The application analyzes multiple features including vehicle specifications, location data, and usage patterns to provide accurate price predictions.

**Key Highlights:**
- 📊 Trained on 143K+ vehicle records (1997-2018 models)
- 🎯 LightGBM regression model with engineered features
- 🌐 Interactive web interface with dynamic form controls
- 📈 Complete EDA pipeline included

## 📁 Project Structure

```
car-price-predictor/
├── app/
│   ├── static/              # Frontend assets (CSS, JS, fonts, images)
│   ├── templates/           # HTML templates
│   ├── app.py              # Main Flask application
│   ├── transformation_functions.py  # Feature engineering utilities
│   └── config.py           # Application configuration
├── data/
│   ├── feature-transformation-data.json  # Encoding mappings
│   ├── models_to_makes.json             # Vehicle relationships
│   └── cities_to_states.json            # Geographic mappings
├── models/
│   └── lgb                 # Trained LightGBM model (pickle)
├── notebooks/
│   └── EDA_Technolabs.ipynb  # Exploratory Data Analysis
├── requirements.txt
├── Procfile               # Heroku deployment config
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/waddah12alhajar/car-price-predictor.git
cd car-price-predictor
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
cd app
python app.py
```

5. **Access the web interface**
   - Open your browser and navigate to: `http://localhost:5000`

## 📊 Dataset & Features

**Dataset Statistics:**
- Total Records: 143,115 vehicles
- Price Range: $1,500 - $279,990
- Model Years: 1997 - 2018
- Average Price: $24,352
- Average Mileage: 53,803 miles

**Input Features:**
- **Vehicle Info**: Make, Model, Manufacturing Year
- **Usage Data**: Mileage, Car Age
- **Location**: City, State
- **Derived Features**:
  - Car usage level (Highly/Moderately/Less Driven)
  - Age classification (New/Old)
  - City/State importance scores

## 🧠 Machine Learning Model

**Algorithm**: LightGBM (Light Gradient Boosting Machine)

**Feature Engineering Pipeline:**
1. **Temporal Features**: Car age, manufacturing year
2. **Usage Metrics**: Miles driven per year, usage classification
3. **Geographic Encoding**: City and state importance levels
4. **Target Encoding**: Log-transformed average prices by categorical features
5. **Statistical Features**: Value counts for location-based features

**Key Correlations:**
- Year ↔ Price: +0.553 (newer = higher price)
- Mileage ↔ Price: -0.537 (less mileage = higher price)
- Year ↔ Mileage: -0.774 (newer = less mileage)

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | Flask 2.3+, Python 3.8+ |
| **ML/Data** | LightGBM, NumPy, Pandas, scikit-learn |
| **Frontend** | HTML5, CSS3, JavaScript, jQuery |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Gunicorn, Heroku-ready |

## 📈 Exploratory Data Analysis

The EDA notebook (`notebooks/EDA_Technolabs.ipynb`) reveals:
- **Price Distribution**: Right-skewed with median at $22,428
- **Mileage Impact**: Strong negative correlation with price
- **Year Trend**: Linear positive relationship with price
- **Brand Analysis**: Luxury brands command premium prices

See full analysis in the [EDA Notebook](notebooks/EDA_Technolabs.ipynb).

## 🌐 Deployment

**Heroku Deployment:**
The app includes a `Procfile` for one-command Heroku deployment:
```bash
heroku create your-app-name
git push heroku main
```

## 📝 License

MIT License with Attribution Requirement

Copyright (c) 2025 Waddah Alhajar

This project requires attribution when used in derivative works. See [LICENSE](LICENSE) for full details.

## 👨‍💻 Author

**Waddah Alhajar**
- GitHub: [@waddah12alhajar](https://github.com/waddah12alhajar)

*Developed as part of the Technocolabs internship program*

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📧 Contact

For questions or feedback, please open an issue on GitHub.
