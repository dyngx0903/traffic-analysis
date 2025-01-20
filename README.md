# Vehicle Counting with YOLOv5

This project provides an automated solution for vehicle counting using YOLOv5 object detection, applied to traffic monitoring scenarios. By detecting and counting various vehicle classes, such as cars, motorbikes, trucks, and buses, this system supports data-driven decision-making for traffic management and urban planning.

## Project Overview

Our solution leverages CCTV feeds from public traffic cameras in Ho Chi Minh City, accessible through [Ho Chi Minh City Traffic Map](http://giaothong.hochiminhcity.gov.vn/Map.aspx). By analyzing these CCTV, the system identifies and counts vehicles passing through different locations, delivering valuable traffic insights to aid congestion management and enhance urban mobility strategies.
The report can be accessed with this link: [Traffic Analysis report](https://www.overleaf.com/read/jmkfbwvnzgpv#ecf74f)

### Key Features

- **Develop a real-time traffic monitoring system using YOLOv5 for detecting and categorizing vehicles.**
- **Analyze traffic patterns to identify insights such as peak hours and vehicle distributions.**
- **Visualize results through an interactive dashboard.**
- **Demonstrate cost-effective, resource-efficient deployment on edge devices.**

---

## **Manual**

### **1. Data Collection**
- Traffic images are sourced from public CCTV feeds and stored locally for processing.
- To collect data:
  1. Run the `trafficdetection.py` script:
     ```bash
     python trafficdetection.py
     ```
  2. This script captures and stores images from specified CCTV feeds every 20 seconds.

### **2. Preprocessing**
- The captured images are preprocessed to ensure they are structured and suitable for analysis. This includes resizing and formatting steps.

### **3. Vehicle Detection**
- A fine-tuned YOLOv5 Nano model is used to detect and categorize vehicles in the images.
- Detection covers the following categories:
  - Cars
  - Motorcycles
  - Heavy vehicles (e.g., buses, trucks).
- Detection is integrated within `trafficdetection.py`.

### **4. Traffic Analysis and Visualization**
- The detection results are analyzed to extract insights, including:
  - Traffic volume trends.
  - Rush hour identification.
  - Vehicle category distributions.
- Analysis results are visualized through an app that generates:
  - Graphs and charts.
  - Textual summaries for deeper insights.
- To perform analysis and view visualizations, run:
  ```bash
  python main.py
  ```

---

## **Additional Notes**
- Ensure all dependencies are installed before running the scripts:
  ```bash
  pip install -r requirements.txt
  ```
- Refer to the `config.yaml` file (if available) to adjust parameters like input sources and model settings.

---
