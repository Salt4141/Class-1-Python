def conversion (unit: str, val: int):
    
    #converting centimeters to feet
    
    if unit == "centimeters":
        new_val = val
        new_val *= 0.0328
        print (val + " centimeters = " + new_val + " feet")
        
        #converting centimeters to inches
        new_val = val
        new_val *= 0.393701
        print (val + " centimeters = " + new_val + " inches")
        
        return 0;
        
    if unit == "inches":
        #converting inches to centimeters
        new_val = val / 0.393701
        print (val + " inches = " + new_val + " centimeters")
        
        return 0;
        
    if unit == "feet":
        #converting feet to centimeters
        new_val = val / 0.0328
        print (val + " feet = " + new_val + " centimeters")
        
        return 0;