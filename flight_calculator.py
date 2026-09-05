#Calculates the active flight time of the drone based on payload weight using the equation T(w) = 180 - 0.1*w
def calculate_flight_time(weight_grams):
    """
    Calculates the flight time of the drone based on the weight of its payload using the equation T(w) = 180 - 0.1*w
    The parameter `weight_grams` is the weight of the payload in grams.
    It returns the flight time in minutes or raises and error if the weight is negative.
    """
    #Copilot suggested return 180 - 0.1 * weight_grams here
    #This was rejected - had to add raise for negative weight value and if the flight time goes below zero
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative")
    flight_time = 180 - 0.1 * weight_grams
    if flight_time < 0:
        return 0
    return flight_time
    #The first if statement was accepted as is
    #The second if statement was edited to return 0 instead of raising an error

#Returns a list of (weight, flight_time) pairs for payload weights from 0 to max_weight_grams in steps of step_grams, calling
#calculate_flight_time for each weight
def flight_time_table(max_weight_grams, step_grams):
    """
    Creates a table of flight times for payloads with weights starting at 0 and ending at the max_weight_grams. 
    The increase between each payload weight and flight time pair is step_grams.
    The parameter 'max_weight_grams' is the maximum weight of the payload in grams.
    The parameter 'step_grams' is the increment between each payload weight.
    A list of (weight, flight_time) pairs is returned.
    """
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table
#This function was accepted as is
