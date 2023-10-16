import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageAnalyzer:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.image_stats = []

    def analyze_images(self):
        if not os.path.exists(self.image_folder):
            print(f"Directory '{self.image_folder}' does not exist.")
            return
        image_files = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            image = cv2.imread(image_path)

            if image is not None:
                avg_color = np.mean(image, axis=(0, 1))
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                avg_brightness = np.mean(gray_image)

                self.image_stats.append({
                    "ImageName": image_file,
                    "AverageColor": avg_color.tolist() if avg_color is not None else [0, 0, 0],
                    "AverageBrightness": avg_brightness
                })

    def save_average_color_plot(self, output_path):
        if not self.image_stats:
            return
        colors = [np.array(stat["AverageColor"]) for stat in self.image_stats]
        colors = np.array(colors)
        plt.figure(figsize=(10, 6))
        plt.scatter(range(len(colors)), colors[:, 0], label="Blue", c='skyblue', edgecolors='darkblue', s=50)
        plt.scatter(range(len(colors)), colors[:, 1], label="Green", c='lightgreen', edgecolors='darkgreen', s=50)
        plt.scatter(range(len(colors)), colors[:, 2], label="Red", c='lightcoral', edgecolors='darkred', s=50)
        plt.xlabel("Image Index")
        plt.ylabel("Average Color Value")
        plt.title("Average Color Analysis")
        plt.savefig(output_path)
        plt.close()

    def save_average_brightness_plot(self, output_path):
        if not self.image_stats:
            return
        brightness = [stat["AverageBrightness"] for stat in self.image_stats]
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(brightness)), brightness, label="Brightness", c='b')
        plt.xlabel("Image Index")
        plt.ylabel("Average Brightness Value")
        plt.title("Average Brightness Analysis")
        plt.savefig(output_path)
        plt.close()

    def save_histogram_red_channel_plot(self, output_path):
        if not self.image_stats:
            return
        red_values = [stat["AverageColor"][2] for stat in self.image_stats]
        plt.hist(red_values, bins=30, color='lightcoral', edgecolor='darkred', alpha=0.7)
        plt.xlabel('Red Channel Value')
        plt.ylabel('Frequency')
        plt.title('Red Channel Histogram')
        plt.savefig(output_path)
        plt.close()

    def save_pie_chart(self, output_path):
        if not self.image_stats:
            return
        total_images = len(self.image_stats)
        total_red = max(0, sum(1 for stat in self.image_stats if stat["AverageColor"][2] > 100))
        total_green = max(0, sum(1 for stat in self.image_stats if stat["AverageColor"][1] > 100))
        total_blue = max(0, sum(1 for stat in self.image_stats if stat["AverageColor"][0] > 100))
        other_colors = max(0, total_images - (total_red + total_green + total_blue))

        labels = ['Red', 'Green', 'Blue', 'Other']
        sizes = [total_red, total_green, total_blue, other_colors]
        colors = ['lightcoral', 'lightgreen', 'skyblue', 'lightgray']

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
        plt.title('Color Composition in Images')
        plt.axis('equal')
        plt.savefig(output_path)
        plt.close()

    def save_scatter_red_vs_green_plot(self, output_path):
        if not self.image_stats:
            return
        red_values = [stat["AverageColor"][0] for stat in self.image_stats]
        green_values = [stat["AverageColor"][1] for stat in self.image_stats]
        plt.scatter(red_values, green_values, c='b', marker='o', alpha=0.5)
        plt.xlabel('Red Channel Value')
        plt.ylabel('Green Channel Value')
        plt.title('Red vs. Green Color Channel')
        plt.savefig(output_path)
        plt.close()

