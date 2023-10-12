// import React, { useEffect ,useState } from 'react';
// import CameraApp from './CameraApp';

// function App() {

//   const [data,setData] = useState([{}])

//   useEffect(() => {
//     fetch("/members").then(
//       res => res.json()
//     ).then(
//       data => {
//         setData(data)
//         console.log(data)
//       }
//     )
//   },[])

//   return (
//     <div className="App">
//       {/* <CameraApp /> */}
//     </div>
//   );
// }

// export default App;
import React, { useState, useEffect } from "react";

function App() {
  const [members, setMembers] = useState([]);

  useEffect(() => {
    fetch("/api/members") // Make sure the URL matches your Flask route
      .then((response) => response.json())
      .then((data) => {
        setMembers(data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Members:</h1>
      <ul>
        {members.map((member, index) => (
          <li key={index}>{member}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

