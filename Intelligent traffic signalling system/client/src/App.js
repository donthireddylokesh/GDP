import "./App.css";
import { useState } from "react";
import axios from "axios";
function App() {
  const [vehicleNumber, setVehicleNumber] = useState("");
  const [vehicleData, setVehicleData] = useState([]);
  const [isUserLogged, setIsUserLogged] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const BASE_URL = "http://localhost:8000";

  const USER_INFO = [
    {
      username: "admin",
      password: "strong-password",
    },
  ];

  const handleAxios = async (event) => {
    event.preventDefault();
    try {
      setVehicleData({});
      const res = await axios.get(`${BASE_URL}/single/${vehicleNumber}`);
      const vehicle = res.data;
      setVehicleData(vehicle);
      if (vehicle.length === 0) {
        alert("no Vehicle found for the given vehicle numbers");
      }
    } catch (e) {
      console.error(e);
    }
  };
  const handleClear = () => {
    setVehicleNumber("");
    setVehicleData([]);
  };

  const renderSearchVehicle = () => {
    return (
      <>
        <form onSubmit={(event) => handleAxios(event)} className="form">
          <label htmlFor={"vehicle_number"}>Enter the Vehicle Number</label>
          <input
            type="text"
            onChange={(event) => setVehicleNumber(event.target.value)}
            value={vehicleNumber}
            id={"vehicle_number"}
          />
          <button disabled={!vehicleNumber?.length} className="search-button">
            Search
          </button>
          <button onClick={handleClear} className="search-button">
            Clear
          </button>
        </form>
        {vehicleData.length ? (
          <table className="result-table">
            <thead>
              <tr>
                <th>Vehicle Number</th>
                <th>Time</th>
                <th>Location</th>
              </tr>
            </thead>
            {vehicleData.map((vehicle) => (
              <tbody key={vehicle.vehicle_number}>
                <tr>
                  <td>{vehicle.vehicle_number}</td>
                  <td>{vehicle.time}</td>
                  <td>{vehicle.location}</td>
                </tr>
              </tbody>
            ))}
          </table>
        ) : (
          ""
        )}
        )
      </>
    );
  };

  const handleLogin = () => {
    const user = USER_INFO.find((val) => val.username === username);
    if (user && user.password === password) {
      setIsUserLogged(true);
    } else {
      alert("login failed");
    }
  };

  const renderLoginPage = () => {
    return (
      <form className="form">
        <label>Username</label>
        <input
          type="text"
          onChange={(event) => setUsername(event.target.value)}
        />
        <label>Password</label>
        <input
          type="password"
          onChange={(event) => setPassword(event.target.value)}
        />
        <button onClick={handleLogin} className="search-button">
          Login
        </button>
      </form>
    );
  };
  console.log({ vehicleNumber, vehicleData });

  return (
    <div className="App">
      <header className="header">
        <h1>Intelligent Traffic Signaling System</h1>
      </header>
      <main className="container">
        {isUserLogged ? renderSearchVehicle() : renderLoginPage()}
      </main>
    </div>
  );
}

export default App;
