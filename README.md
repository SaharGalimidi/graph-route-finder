# Graph-Based Route Finder

This is a Flask application for finding routes in a graph.
It uses the Dijkstra algorithm to find the shortest path between two nodes in a graph.
Edges are weighted and the weight is the distance between the nodes using Euclidean distance .

## How to Run

### Using Docker

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/SaharGalimidi/graph-route-finder.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd graph-route-finder/graph_route_finder
    ```

3. **Build the Docker Image:**

    ```bash
    docker build -t graph-route-finder .
    ```

4. **Run the Docker Container:**

    ```bash
    docker run --rm -p 5000:5000 graph-route-finder
    ```

5. **Access the Application:**

    Open your web browser and go to `http://localhost:5000`.

### Without Docker

1. **Ensure Python 3.9 is Installed:**

    Make sure you have Python 3.9 installed on your system.

2. **Clone the Repository:**

    ```bash
    git clone https://github.com/SaharGalimidi/graph-route-finder.git

3. **Navigate to the Project Directory:**

    ```bash
    cd graph-route-finder/graph_route_finder
    ```

4. **Create a Virtual Environment:**

    Create a new virtual environment using the following command:

    ```bash
    python -m venv venv
    ```

5. **Activate the Virtual Environment:**
    
        Activate the virtual environment using the following command:
    
        - On Windows:
    
            ```bash
            venv\Scripts\activate
            ```
    
        - On macOS and Linux:
    
            ```bash
            source venv/bin/activate
            ```


6. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    Run the Flask application using the following command:

    ```bash
    python run.py
    ```

4. **Access the Application:**

    Open your web browser and go to `http://localhost:5000`.

## Requirements

- Python 3.9
- Flask
- matplotlib
- Docker
