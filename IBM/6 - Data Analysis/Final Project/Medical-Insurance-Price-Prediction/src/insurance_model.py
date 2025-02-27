import joblib
import numpy as np

class InsuranceModel:
    def __init__(self, model_path="../outputs/final_model.pkl", transformer_path="../outputs/polynomial_transformer.pkl"):
        """
        Load the trained model and transformer.
        """
        try:
            self.model = joblib.load(model_path)
            self.poly_transformer = joblib.load(transformer_path)
        except Exception as e:
            raise RuntimeError(f"Error loading model or transformer: {e}")

    def input_validation(self, age, bmi, no_of_children, smoker, region, male, female):
        """
        Validate input data types and values.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Invalid input: 'age' must be a positive integer.")
        if not isinstance(bmi, (float, int)) or bmi <= 0:
            raise ValueError("Invalid input: 'bmi' must be a positive float or integer.")
        if not isinstance(no_of_children, int) or no_of_children < 0:
            raise ValueError("Invalid input: 'no_of_children' must be a non-negative integer.")
        if smoker not in {0, 1}:
            raise ValueError("Invalid input: 'smoker' must be 0 (non-smoker) or 1 (smoker).")
        if region not in {0, 1, 2, 3, 4}:
            raise ValueError("Invalid input: 'region' must be 0, 1, 2, or 3.")
        if male not in {0, 1} or female not in {0, 1} or (male + female) != 1:
            raise ValueError("Invalid input: Exactly one of 'male' or 'female' must be 1, the other must be 0.")
        
        return True

    def predict(self, age, bmi, no_of_children, smoker, region, male, female):
        """
        Predict the insurance cost based on input features.
        """
        self.input_validation(age, bmi, no_of_children, smoker, region, male, female)
        
        # Ensure correct feature order
        input_data = np.array([[age, no_of_children, smoker, bmi, region, female, male]])
        
        # Apply polynomial transformation
        input_data_poly = self.poly_transformer.transform(input_data)
        
        # Predict using the trained Ridge model
        price = self.model.predict(input_data_poly)[0]
        
        return round(price, 2)

# Initialize model when imported
insurance_model = InsuranceModel()

