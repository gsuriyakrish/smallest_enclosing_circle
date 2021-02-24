# Smallest Circle around cluster of points #
This module is for finding the
smallest circle around a cluster of points in 2D
and plotting them against on a Graph

## How do you get set up? ##

### Using Docker ###
1. Download this project or clone the repository.
2. Go to the project folder in command prompt
3. Run the following command

        * docker-compose build minimum-enclosing-circle
        * docker-compose up
        
4. After the docker spun up, the code will be ready to run on the Docker environment.
5. To run the unit testcases

        * docker-compose run --rm minimum-enclosing-circle python -m unittest
        
6. To stop the service

        * docker-compose stop

### Without using Docker ###

1. Download this project or clone the repository.
2. Go to the project folder.
3. Install virtualenv

        pip install virtualenv
 
4. Create a virtual environment in project root folder

        virtualenv venv
        
5. Go to the project folder and activate virtual environment
 
        \venv\Scripts\activate.bat            
        
6. Install dependencies

       pip install -r requirements.txt
       
6. Run the unittests

       python -m unittest
       
7. Run the program
        
       python start.py
 
8. The number of input points can be changed from start.py like below and run the program
   
     `print(smallest_circle.pilot(input_points=2))`
     
     `print(smallest_circle.pilot(input_points=6))`
     
     `print(smallest_circle.pilot(input_points=20))`
     
## Libraries Used ##

- Check `requirements.txt`

## Contribution guidelines ##
- Forks are always appreciated




 
         
      
 
