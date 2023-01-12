# Rocket_Elevators_Django_API

This is a facial recognition api that allows you to interact and get data from the rocket elevators employee table

Postman Collection: https://api.postman.com/collections/24446629-3a004605-a944-4682-bfdf-d77f3ff62496?access_key=PMAT-01GPKG1B7TT1P71GHEEANQVZBW

# First Endpoint 

http://127.0.0.1:8000/list
-this endpoint gets a list of every entry in the employee database

# Second Endpoint

 http://127.0.0.1:8000/employee/12/photo
 -this endpoints allows you to add a photo that gets its facial keypoints encoded and stored in the facialKeyPoints column in the database
 -to choose the employee you want just change the number in the url to the employees id number

# Third Endpoint

http://127.0.0.1:8000/recognize
-this endpoint takes the image file you attached, encodes it then compares that to the encoded information in the facialKeyPoints column of the database, finds a match then returns that matches information

# Fourth Endpoint

http://127.0.0.1:8000/employee
-this endpoint allows you to add a new employee with a photo, that photo will then be encoded and stored in the facialKeyPoints column
