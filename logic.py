import pandas as pd

def determine_vehicle(df, num_persons):
    """
    Engine for determining the correct vehicle based on the uploaded Excel structure.
    """
    
    # CASE 1: The user typed 0.
    if num_persons == 0:
        return {
            "found": True,             
            "input_a": 0,              
            "match_b": 0,              
            # We will read exactly what is in row 2 of your Assigned_Vehicle column
            "output_c": df.iloc[0]['Assigned_Vehicle'] 
        }
        
    # CASE 2: The user typed 1 or more.
    # Searching using the EXACT column name from your image: 'Max_Capacity'
    suitable_rows = df[df['Max_Capacity'] >= num_persons]
    
    if not suitable_rows.empty:
        # Extract using the exact column names
        match_b = suitable_rows.iloc[0]['Max_Capacity']
        output_c = suitable_rows.iloc[0]['Assigned_Vehicle']
        
        return {
            "found": True,
            "input_a": num_persons,
            "match_b": match_b,
            "output_c": output_c
        }
        
    # CASE 3: The user typed a number larger than 720 (Train capacity).
    else:
        return {
            "found": False,
            "input_a": num_persons,
            "error_msg": "Number of persons exceeds our maximum database capacity (720)."
        }