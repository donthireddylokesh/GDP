## Intelligent Traffic Signaling System

**Short Description**

This project implements an intelligent traffic signaling system that dynamically adjusts signal timing based on real-time traffic data and prioritizes emergency vehicles. This system aims to reduce traffic congestion, improve traffic flow efficiency, minimize emissions, and ensure faster response times for emergency services.

**Built With**

* Python
* NumPy
* OpenCV (for vehicle detection and registration plate recognition)
* PyMongo (for accessing emergency vehicle data)

**Dependencies**

The required dependencies are listed in a separate file named `dependencies.txt`. You can install them using the following command:

```bash
pip install -r dependencies.txt
```

**Getting Started**

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Configure the connection details to your MongoDB instance containing emergency vehicle data.
4. Run the following commands to start the simulation and visualization:

```bash
python main.py
python simulation.py
```

**Features**

* Dynamic signal timing adjustment based on real-time traffic data.
* Prioritization of emergency vehicles based on registration plate recognition and comparison with emergency vehicle data from MongoDB.
* Visualization of traffic flow, signal timing changes, and emergency vehicle movement.
* Performance evaluation metrics including average waiting time, travel time, queue length, and emergency response time improvement.


**Deployment**

This project is currently designed for research and development purposes. For deployment on real-world traffic systems, additional hardware and software infrastructure would be required, including cameras for vehicle detection and communication interfaces with traffic lights.


