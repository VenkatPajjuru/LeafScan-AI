# Import redirect and url_for
from flask import Flask, render_template, request, jsonify, redirect, url_for # <-- FIX 1
from keras.utils import load_img, img_to_array
from keras.models import load_model
import numpy as np
import os
import json 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime 
import time
from data import class_names, remedies, library_data                             
from werkzeug.utils import secure_filename 
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables (your API key)
load_dotenv()
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Error: GEMINI_API_KEY not found. Please set it in your .env file.")
    exit()
    
#print("--- Listing Available Models ---")
#for m in genai.list_models():
 #   if 'generateContent' in m.supported_generation_methods:
  #      print(f"Model name: {m.name}")
#print("---------------------------------")
# --- END OF NEW CODE ---


# Initialize the Generative Model
# --- CHECK YOUR TERMINAL TO CONFIRM THIS MODEL NAME IS IN THE LIST ---
gemini_model = genai.GenerativeModel('models/gemini-2.5-flash') # <-- RECOMMENDATION 1 (Changed to a safer default)
# --- END OF NEW GEMINI SETUP ----

class_names = {
    # This was a syntax error. The string was broken into two lines.
    0: "Pepper bell Bacterial spot (alt)", # <-- FIX 2
    1: "Pepper bell healthy",
    2: "Potato Early blight",
    3: "Potato Late blight",
    4: "Potato healthy",
    5: "Tomato Bacterial spot",
    6: "Tomato Early blight",
    7: "Tomato Late blight",
    8: "Tomato Leaf Mold",
    9: "Tomato Septoria leaf spot",
    10: "Tomato Spider mites Two spotted spider mite",
    11: "Tomato Target_Spot",
    12: "Tomato YellowLeaf Curl Virus",
    13: "Tomato mosaic virus",
    14: "Tomato healthy",
}


# --- END OF NEW LIBRARY DATA ---

model = load_model("model/vgg16_model.h5")
# ... (rest of your code)

model = load_model("model/vgg16_model.h5")

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crops.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UserCrop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    # This will store the generated plan as a simple text file (JSON)
    timeline_json = db.Column(db.Text, nullable=True) 

    def __repr__(self):
        return f'<UserCrop {self.crop_name}>'

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")

    file = request.files["file"]
    
    # --- Using your previous secure filename logic ---
    base_filename = secure_filename(file.filename) 
    file_extension = os.path.splitext(base_filename)[1]
    unique_name = str(int(time.time())) + "_" + base_filename
    img_path = "static/images/uploads/" + unique_name
    file.save(img_path)
    # --- End of secure filename logic ---

    img = load_img(img_path, target_size=(224, 224))
    x = img_to_array(img)
    x /= 255.0
    x = np.expand_dims(x, axis=0)

    predictions = model.predict(x)
    class_idx = np.argmax(predictions[0])
    confidence_score = predictions[0][class_idx] * 100
    confidence = "{:.2f}".format(confidence_score)

    if class_idx == 14 or class_idx == 4 or class_idx == 1:
        predicted_disease = "No disease detected (Healthy Leaf)"
        treatment = []
    else:
        predicted_disease = class_names.get(class_idx, "Unknown Disease")
        treatment = remedies.get(class_idx, ["No specific remedy found."])

    return render_template(
        "result.html",
        confidence=confidence,
        filename=unique_name,
        predicted_disease=predicted_disease,
        treatment=treatment,
    )
@app.route('/my_crops')
def my_crops():
    # Query the database for all crops
    all_crops = UserCrop.query.all()
    return render_template('my_crops.html', all_crops=all_crops)
# ... (after your my_crops route) ...

@app.route('/disease_library')
def disease_library():
    # Pass the existing library_data dictionary to the new page
    return render_template('disease_library.html', library=library_data)

@app.route('/register_crop', methods=['GET', 'POST'])
def register_crop():
    if request.method == 'POST':
        # 1. Get data from the form
        crop_name = request.form['crop_name']
        sowing_date_str = request.form['sowing_date']
        sowing_date = datetime.strptime(sowing_date_str, '%Y-%m-%d').date()

        # 2. Create the prompt for Gemini
        # We will ask for a JSON response to make it easy to parse
        prompt = f"""
        You are an expert agronomist. A user is planting '{crop_name}' on '{sowing_date_str}'.
        Generate a comprehensive, day-wise schedule for this crop.
        Include all key stages: Soil Preparation, Sowing, Fertilization, Irrigation, Weed Control, Pest Protection, Harvesting, and Storage.

        Respond ONLY with a JSON object. The root object must have a key "schedule".
        The "schedule" key should be an array of objects.
        Each object in the array must have three keys:
        1. "task_name": The name of the task (e.g., "First Fertilization").
        2. "days_after_sowing": The approximate number of days after sowing to perform the task.
        3. "details": A brief description of what to do.

        Do not include any text before or after the JSON object.
        """

        # 3. Call Gemini API (use your model name)
        try:
            response = gemini_model.generate_content(prompt)
            # Clean up the response to get pure JSON
            json_response = response.text.strip().replace('```json', '').replace('```', '')
            
            # 4. Save to database
            new_crop = UserCrop(
                crop_name=crop_name,
                sowing_date=sowing_date,
                timeline_json=json_response # Save the raw JSON
            )
            db.session.add(new_crop)
            db.session.commit()

            # 5. Redirect to the new timeline page
            return redirect(url_for('crop_timeline', crop_id=new_crop.id))

        except Exception as e:
            print(f"Error during crop registration: {e}")
            return render_template("error.html", error=str(e))

    # GET request: Just show the form
    return render_template('register_crop.html')

@app.route('/crop_timeline/<int:crop_id>')
def crop_timeline(crop_id):    # Get the crop from the database by its ID
    crop = UserCrop.query.get_or_404(crop_id)
    
    # Parse the saved JSON string into a Python object
    try:
        # Use json.loads() to parse the string
        timeline_data = json.loads(crop.timeline_json)
        schedule = timeline_data['schedule']
    except Exception as e:
        print(f"Error parsing timeline JSON: {e}")
        schedule = [] # Show an empty schedule on error

    return render_template('timeline.html', crop=crop, schedule=schedule)
# --- NEW ROUTE FOR GEMINI RECOMMENDATIONS ---
@app.route("/get_recommendation", methods=["POST"])
def get_recommendation():
    try:
        # Get the disease name from the frontend
        data = request.get_json()
        disease_name = data['disease']

        # A good prompt is key!
        prompt = f"""
        I have a plant with the disease: '{disease_name}'.
        Please recommend specific pesticides and fertilizers to treat this.
        
        Provide your answer in two sections:
        1.  **Recommended Pesticides:** (List 3-5 specific products or chemical names)
        2.  **Recommended Fertilizers:** (List 3-5 products or types that help recovery)

        Keep the response concise and easy for a home gardener to understand.
        Format the response in HTML that I can directly display.
        **Do not include the markdown triple backticks (```html or ```) in your response.**
        """

        # Call the Gemini API
        response = gemini_model.generate_content(prompt)
        
        # Send the response back to the frontend
        return jsonify({'recommendation': response.text})

    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Send a generic error message
        error_message = f"<p>Error: Could not get recommendations at this time. Error: {str(e)}</p>"
        return jsonify({'recommendation': error_message}), 500
# --- END OF NEW ROUTE ---

@app.errorhandler(Exception)
def handle_exception(error):
    print(error)
    return render_template("error.html", error=error), 500

# --- RECOMMENDATION 2: Add this block to create the database ---
# This code will create the 'crops.db' file if it doesn't exist
with app.app_context():
    db.create_all()
# --- END OF NEW BLOCK ---

if __name__ == "__main__":
    app.run(debug=True) # Run in debug mode for development