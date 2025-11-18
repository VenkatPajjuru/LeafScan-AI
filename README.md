# LeafScan AI: Intelligent Crop Disease Detection & Management

![LeafScan AI Banner](static/images/banner_placeholder.png) 
## 📋 Abstract

*LeafScan AI* is an intelligent web application designed to empower farmers and gardeners with a complete "detect, cure, and manage" solution for crop health. 

Traditional disease identification is often reactive and slow. LeafScan AI changes this by integrating deep learning for instant *disease detection* (using a VGG16 model) with generative AI (Google Gemini) for *dynamic remedy recommendations* and proactive *crop timeline management. The system supports critical crops including **Tomato, Potato, Pepper, Paddy, and Wheat*, providing an accessible, all-in-one platform for sustainable agriculture.

---

## 🚀 Key Features

### 1. 🍂 AI Disease Detection
* *Instant Diagnosis:* Upload a leaf image to instantly identify diseases using a pre-trained VGG16 Convolutional Neural Network (CNN).
* *Supported Crops:* Tomato, Potato, Bell Pepper, Paddy (Rice), and Wheat.
* *Confidence Scores:* Provides a probability score for the prediction to ensure transparency.

### 2. 💊 AI-Powered Remedies
* *Dynamic Solutions:* Beyond static advice, the system integrates *Google's Gemini AI* to generate specific, context-aware recommendations for pesticides and fertilizers tailored to the detected disease.
* *Actionable Advice:* Get step-by-step treatment plans on demand.

### 3. 📅 Crop Timeline Manager
* *Proactive Management:* Shift from reactive to proactive farming. Register your crop and sowing date to generate a full cultivation schedule.
* *AI-Generated Schedules:* Gemini AI creates a day-by-day timeline covering soil preparation, irrigation, fertilization, and harvesting.
* *Persistent Tracking:* Save and view your crop timelines via the "My Crops" dashboard (powered by SQLite).

### 4. 📚 Disease Library
* *Educational Resource:* A dedicated section providing detailed information, identification tips, and standard remedies for common diseases across all supported crops.

---

## 🛠 Tech Stack

* *Backend:* Python, Flask
* *Deep Learning:* TensorFlow, Keras (VGG16 Model)
* *Generative AI:* Google Gemini API (google-generativeai)
* *Database:* SQLite, Flask-SQLAlchemy
* *Frontend:* HTML5, CSS3, JavaScript
* *Image Processing:* NumPy, Pillow (PIL)

---

## 📂 Project Structure

```bash
LEAFSCAN-AI/
├── model/
│   └── vgg16_model.h5        # Pre-trained CNN model
├── static/
│   ├── css/                  # Stylesheets (base, index, result, library)
│   └── images/
│       └── uploads/          # Folder for user-uploaded images
├── templates/
│   ├── base.html             # Base layout template
│   ├── index.html            # Homepage (Upload)
│   ├── result.html           # Prediction results & AI remedies
│   ├── my_crops.html         # Crop management dashboard
│   ├── register_crop.html    # Crop registration form
│   ├── timeline.html         # Generated timeline view
│   ├── disease_library.html  # Disease information library
│   └── error.html            # Error handling page
├── app.py                    # Main Flask application controller
├── data.py                   # Static dictionaries (class_names, remedies, library)
├── crops.db                  # SQLite database (generated on run)
├── .env                      # Environment variables (API Key)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
