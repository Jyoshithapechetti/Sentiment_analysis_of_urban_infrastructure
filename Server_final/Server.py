from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Path to the CSV file
DATA_PATH = "userdata_Dataset.csv"

# Define feature columns
columns = [
    "anxiety_level", "self_esteem", "mental_health_history", "depression", "headache", 
    "blood_pressure", "sleep_quality", "breathing_problem", "noise_level", "living_conditions", 
    "safety", "basic_needs", "work_performance", "work_load", "manager_employee_relationship", 
    "future_career_concerns", "social_support", "peer_pressure", "physical_activities", 
    "Workplace_Aggression", "stress_level"
]

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit_form():
    try:
        # Extract user input from the form
        user_data = {col: float(request.form.get(col, 0)) for col in columns}

        # Load existing data from the CSV file
        try:
            data = pd.read_csv(DATA_PATH)
        except FileNotFoundError:
            # Create an empty DataFrame if the file doesn't exist
            data = pd.DataFrame(columns=columns)

        # Convert user input into a DataFrame row
        new_row = pd.DataFrame([user_data])

        # Append the new row to the existing data
        data = pd.concat([data, new_row], ignore_index=True)

        # Save the updated data back to the CSV file
        data.to_csv(DATA_PATH, index=False)

        # Return a success message to render in result.html
        return render_template("results.html", message="New data added successfully.")
    
    except Exception as e:
        # Log the error and provide a meaningful message
        return f"Error saving the dataset: {e}"

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/submit", methods=["POST"])
def submit_form():
    # Extract user input from the form
    place = request.form.get("Place")
    label = request.form.get("Label")
    review = request.form.get("Review")

    try:
        # Load existing data from the CSV file
        data = pd.read_csv(DATA_PATH)

        # Create a new row with the user inputs
        new_row = pd.DataFrame({"Place": [place], "Label": [label], "Review": [review]})

        # Append the new row to the existing data
        data = pd.concat([data, new_row], ignore_index=True)

        # Save the updated data back to the CSV file
        data.to_csv(DATA_PATH, index=False)

        # Return a success message to render in result.html
        return render_template("results.html", message="New data added successfully.")
    
    except Exception as e:
        # Log the error and provide a meaningful message
        return f"Error saving the dataset: {e}"

if __name__ == "__main__":
    app.run(debug=True)
