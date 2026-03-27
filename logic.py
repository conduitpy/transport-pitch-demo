import pandas as pd

def determine_vehicle(df, num_persons):

    if num_persons == 0:
        return {
            "found": True,             
            "input_a": 0,              
            "match_b": 0,                
            "output_c": df.iloc[0]['Assigned_Vehicle'] 
        }
        
    suitable_rows = df[df['Max_Capacity'] >= num_persons]
    
    if not suitable_rows.empty:
        match_b = suitable_rows.iloc[0]['Max_Capacity']
        output_c = suitable_rows.iloc[0]['Assigned_Vehicle']
 
        return {
            "found": True,
            "input_a": num_persons,
            "match_b": match_b,
            "output_c": output_c
        }
        
    else:
        return {
            "found": False,
            "input_a": num_persons,
            "error_msg": "Number of persons exceeds our maximum database capacity (720)."
        }
