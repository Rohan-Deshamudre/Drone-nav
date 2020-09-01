# Hospital of the Future - Drone navigation

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installing Unreal Engine](#installing-unreal-engine)
  * [Installing Visual Studio and Cloning repository](#installing-visual-studio-and-cloning-repository)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project
Leveraging the services offered by Microsoft Azure, a drone will be able to act as an assistant to the hospital staff as well as patients and other individuals inside the facility. The two main objectives of the drone can be classified as autonomous navigation through the facility and surveillance of the premises. The solutions to these is as follows: 
1.	A map of the hospital building will be created including data about physical assets such as furniture, elevators, stairs and more for each floor. Using this map, given the current location of the drone and a destination point, a route (set of coordinates for the drone to follow) is calculated. 
2.	Computer vision models for mask compliance, people counting, and proximity sensing will be deployed onto the drone. Using its autonomous flight, the drone will be able to maneuver around the hospital and monitor people across different areas of the building to ensure that rules such as social distancing and mask compliance are being adhered to. 
A web app created to showcase the digital twin of the hospital will have a feature allowing users to enter a destination point on the map that the drone needs to travel to. The moving drone can then be used as a guide to take people from room to room in the building or for surveillance purposes. 


### Built with: 
1.	**Azure maps:** A map of each floor of the building is created using the azure indoor maps creator module. A CAD drawing of the floor plan is converted into map data further allowing querying of this dataset to extract coordinates of the drone’s current location, coordinates of its destination point and create a route between the two points.
2.	**AirSim:** The traversal of this route will be simulated in a 3D model of the inside of the hospital created on Unreal Engine and deployed on the AirSim simulator. This provides a visual on how the drone would move in a real hospital environment. 
3.	**Azure digital twin:** Using sensor data available through the Azure digital twin, further additions such as finding the closest unoccupied room, closest wheelchair and more can be determined and fed as a destination point for the drone.

<!-- GETTING STARTED -->
## Getting Started
### Installing Unreal Engine

You will need to install Unreal Engine to work with this demo code using the following steps:

1. [Download](https://www.unrealengine.com/en-US/download) the Epic Games Launcher. While the Unreal Engine is open source and free to download, registration is still required.
2. Run the Epic Games Launcher, open the `Unreal Engine` tab on the left pane and then click on the `Library` tab on the top navigation bar.
3. Click on the `+` next to engine versions which should show the option to download Unreal 4.25. If you have multiple versions of Unreal installed then **make sure 4.25 is set to `current`** by clicking down arrow next to the Launch button for the version.

 **Note**: AirSim also works with UE >= 4.22, however, we recommend you update to 4.25.


### Installing Visual Studio and Cloning repository
* Install Visual Studio 2019.
**Make sure** to select **Desktop Development with C++** and **Windows 10 SDK 10.0.18362** (should be selected by default) while installing VS 2019.
* [Download](https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net48-developer-pack-offline-installer) and install .NET Framework Developer pack >= 4.6.
* Start `Command Prompt` and change the current working directory to the location where you want the cloned directory to be made.
* Clone the repo: `INSERT URL HERE`, and go the Hospital directory by `cd Hospital`.
### Installing python & dependencies
* [Download](https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64-webinstall.exe) and install the latest version of python.
* Check the box that says `Add Python to PATH`
![python.png](images/python.png)
* Run `Command Prompt` as Administrator and change the current working directory to `Hospital\PythonClient\multirotor`
* This package depends on `msgpack` and `airsim`. To install, copy paste this into the `Command Prompt`:
```
pip install airsim msgpack-rpc-python
```

# Running Airsim

Once the project is set up by following above steps, you can:

1. Double click on Hospital.sln file to load the Contoso Healthcare environment onto Unreal Engine. 
2. Make sure Build config is set to "Development Editor" and Win64.
![config.png](images/config.png) 
3. Press F5 to run. This will start the Unreal Editor. 
4. In `Window/World Settings` as shown below, set the `GameMode Override` to `AirSimGameMode`:
![sim_game_mode.png](images/sim_game_mode.png)


# Running python script
* To start simulation, press Play button on Unreal editor and select `no` on the choose vehicle popup to use quadcoptor.
![play.png](images/play.png) 
* Run `Command Prompt` as Administrator and change the current working directory to `Hospital\PythonClient\multirotor`
* Run the navigation script using:
```
python pathFinder.py
```
* Enter the current location of drone and the destination of drone based on the Azure map below:
![azureMap.png](images/azureMap.png)

**Watch the drone navigate its way through the environment...**

**Note**: The drone spawns at the Reception which is Room 27 on the Azure Map. This should be the start location you enter when the simulation starts.

# Videos

Room to Room Navigation

[![Room to Room](http://img.youtube.com/vi/h912Fh80jnQ/0.jpg)](http://www.youtube.com/watch?v=h912Fh80jnQ "Room to Room Navigation") 


Reception to Waiting Room navigation:

[![Reception to Waiting Room](http://img.youtube.com/vi/uBwP-rYIqmI/0.jpg)](http://www.youtube.com/watch?v=uBwP-rYIqmI "Reception to Waiting Area")



