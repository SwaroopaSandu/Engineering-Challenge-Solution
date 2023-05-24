# Engineering-Challenge-Solution

# Food Truck API

This project implements a web API that provides information about food trucks in a city. It also includes a CLI tool to retrieve the names of all the taco trucks specifically. Additionally, a containerized system is provided that generates a placeholder webpage featuring the name of each food truck, which can be used for marketing purposes.
Here is the link to the complete problem statement: https://github.com/peck/engineering-assessment/blob/main/README.md

## Problem Statement
The goal of this project is to create a web API that allows users to retrieve information about food trucks in a city. Specifically, we need to implement the following:

1. Create an API endpoint that returns a list of all food trucks.
2. Create a CLI tool that retrieves the names of all the taco trucks in the city.

## Solution Overview
To address the problem statement, we have implemented the solution using the following technologies:

- Angular: A popular front-end framework for building web applications.
- Flask: A lightweight web framework for building APIs with Python.

The solution consists of the following components:

1. **Food Truck API**: This is a RESTful API built with Flask. It provides two endpoints:
   - `/allfoodtrucks`: Returns information about all food trucks in the city.
   - `/foodtrucks`: Returns the names of all taco trucks in the city.
   
2. **CLI Tool**: The CLI tool allows users to retrieve the names of all the taco trucks in the city. It utilizes the `/foodtrucks` endpoint of the Food Truck API to obtain list of taco food trucks and `/allfoodtrucks` endpoint of the Food Truck API to obtain list of all available food trucks..

## Installation and Usage

To use this project, follow the steps below:

1. Clone the repository: `git clone <repository-url>`
2. Install the required dependencies for the Python API:
   ```
   cd food-truck-api
   pip install -r requirements.txt
   ```
3. Start the Python API server:
   ```
   python AllFoodTrucks.py
   python tacoTrucks.py
   ```
   The API endpoints will be available at `http://localhost:5000/allfoodtrucks` and `http://localhost:5000/tacoTrucks`.

4. Install Node.js and npm on your system (if not already installed).
5. Install the required dependencies for the Angular application:
   ```
   cd angular-app
   npm install
   ```
6. Build the Angular application:
   ```
   ng build --prod
   ```
   The production-ready build files will be generated in the `dist` directory.

7. Install a web server, such as `http-server`, globally on your system:
   ```
   npm install -g http-server
   ```

8. Start the web server and serve the Angular application:
   ```
   http-server dist/angular-app
   ```
   The Angular application will be accessible at `http://localhost:8080` in your browser.


## Conclusion
In conclusion, this project successfully addresses the problem statement by providing a comprehensive solution for managing and showcasing food trucks in a city. The implemented solution includes a web API, CLI tool, and containerized system, leveraging Flask, and Angular.

The web API offers two endpoints to fulfill different requirements. 
The /allfoodtrucks endpoint returns a complete list of all food trucks in the city, providing detailed information about each truck, such as name, cuisine type, and location. On the other hand, the /foodtrucks endpoint specifically caters to taco enthusiasts, returning only the names of taco trucks.
By combining Flask, and Angular, this project offers a robust, scalable, and visually appealing solution for food truck management. It caters to API consumers, CLI users, and marketing teams, empowering them with valuable information and tools to explore, retrieve, and promote food trucks in the city.
