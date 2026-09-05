- GitHub Copilot inline suggested were used to create the functions calculate_flight_time and flight_time_table. 
- Rewrote the function calculate_flight_time to add if statements to check if the weight was below 0 and if the flight time went below 0, Copilot inline suggestions used to create if statements
- Second if statement (if flight_time < 0) was rewritten to return 0 instead of raising and error
- Function flight_time_table was accepted as it

- Used GitHub Copilot Chat (/tests) to generate the initial unit test skeletons for calculate_flight_time(). Rewrote the last test as after testing I realized flight time being less than 0
raised an error and rewrote the if statement in calculate_flight_time to return 0 instead, then rewrote the test case to check that 0 was being returned
- After edits once again verified all test passed with pytest