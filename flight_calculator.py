#Calculates the active flight time of the drone based on payload weight using the equation T(w) = 180 - 0.1*w
def calculate_flight_time(weight_grams):
    #Copilot suggested return 180 - 0.1 * weight_grams here
    #This was rejected - had to add raise for negative weight value and if the flight time goes below zero
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative")
    flight_time = 180 - 0.1 * weight_grams
    if flight_time < 0:
        raise ValueError("Flight time cannot be negative")
    return flight_time
    #These 2 if statements were accepted
