# Instagram Image Analysis Tool

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Insights](#analysis-insights)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Instagram Image Analysis Tool is a Python application designed for data scientists and enthusiasts who want to scrape and analyze images from Instagram. This tool allows you to gain insights into the average color and brightness of the images you collect. Whether you're using it for research, analysis, or just for fun, this README provides a comprehensive guide on how to use the tool effectively.

## Features

- **Instagram Image Scraping:** Easily download images from Instagram based on specific keywords.
- **Image Analysis:** Calculate the average color (RGB) and brightness of the downloaded images.
- **Visualization:** Generate compelling visualizations, including color histograms and scatter plots.
- **User-Friendly Interface:** Utilize a web-based interface for seamless interaction with the tool.

## Prerequisites

Before you get started with the Instagram Image Analysis Tool, make sure you have the following prerequisites installed on your machine:

- Python 3.x
- Required Python libraries (see the list in `requirements.txt`)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/instagram-image-analysis.git
   ```
2. **Install Dependencies:**

To set up the required Python libraries and dependencies, create a virtual environment and install the packages listed in the requirements.txt file. Use the following commands:
# Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
# Install the required packages
```bash
pip install -r requirements.txt
```
3. **Download ChromeDriver:**

If you're using the Instagram scraper functionality, you'll need ChromeDriver. Download it from the official website and specify the path to it in your application.

4. **Configure Your Instagram Credentials:**

To scrape images from Instagram, you'll need your Instagram username and password. Add them to the `main.py` script.

Usage:

To run the Instagram Image Analysis Tool, execute the following command: 
```bash
python main.py
```
## Access the Web Interface

After starting the tool, you can access the web interface by opening a web browser and navigating to [http://localhost:5000/](http://localhost:5000/) (or the address provided in the terminal).

## Analysis Insights

The Instagram Image Analysis Tool provides the following insights:

- **Average Color Analysis:** Understand the predominant colors in your collected images.
- **Average Brightness Analysis:** Get insights into the brightness levels of your images.
- **Red Channel Histogram:** Visualize the distribution of the red color channel.
- **Color Composition Pie Chart:** Discover the composition of colors in your images.
- **Red vs. Green Color Channel Scatter Plot:** Analyze the relationship between the red and green color channels.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it for your needs.

