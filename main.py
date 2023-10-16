import os
from flask import Flask, render_template, send_from_directory
from Image_analyzer import ImageAnalyzer
from Instagram_scraper import InstagramImageScraper

app = Flask(__name)

# Function to create ImageAnalyzer instance and save plots as images
def create_analyzer_and_save_plots(image_folder_path):
    analyzer = ImageAnalyzer(image_folder_path)
    analyzer.analyze_images()

    # Save the plots as images
    analyzer.save_average_color_plot("static/average_color_plot.png")
    analyzer.save_average_brightness_plot("static/average_brightness_plot.png")
    analyzer.save_histogram_red_channel_plot("static/red_channel_histogram.png")
    analyzer.save_pie_chart("static/color_composition_pie_chart.png")
    analyzer.save_scatter_red_vs_green_plot("static/red_vs_green_scatter.png")

# Instagram scraping and saving data to a folder
def scrape_and_save_data(username, password, keyword):
    chromedriver_path = "chromedriver.exe"
    scraper = InstagramImageScraper(chromedriver_path, username, password)
    scraper.login_to_instagram()
    scraper.search_and_download_images(keyword)
    scraper.close_driver()

    image_folder = keyword[1:] + "s"
    return image_folder

# Route for displaying the charts
@app.route('/')
def display_charts():
    image_folder_path = "C:/Users/hp/Desktop/Chayma/Data_Insights_From_Images/Keyword"

    # Create the ImageAnalyzer instance and save the plots as images
    create_analyzer_and_save_plots(image_folder_path)

    return render_template('charts.html')

if __name__ == '__main__':
    # Replace with your Instagram username, password, and keyword
    username = "Your_Username"
    password = "Your_Password"
    keyword = "Your_Keyword"

    # Scraping and saving data to a folder
    image_folder = scrape_and_save_data(username, password, keyword)

    # Analyzing the data and saving plots
    create_analyzer_and_save_plots(image_folder)

    app.run(debug=True)
