import React, { useEffect, useState } from "react"
import './App.css';

function App() {
  const [users, setUsers] = useState([])

  const fetchUserData = () => {
    fetch("/api/todos", {method: "GET"})
      .then(response => {
        console.log(response)
        return response.json()
      })
      .then(data => {
        console.log(data)
        setUsers(data.todos)
      })
  }

  useEffect(() => {
    fetchUserData()
  }, [])

  return (
    <div>
      {users.length > 0 && (
        <ul>
          {users.map(user => (
            <li key={user['id']}>{user['goal']}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
