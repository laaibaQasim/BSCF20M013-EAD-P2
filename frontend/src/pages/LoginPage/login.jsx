import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './login.css'

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const handleLogin = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/login', {
        email: email,
        password: password,
      });

      // Assuming the API returns a success status code (e.g., 200)
      if (response.status === 200) {
          await axios.post('http://127.0.0.1:5000/log', {
            action: "login",
            details: "User logged into the system",
          });
        navigate('/studentList');
      } else {
        setError('Invalid Credentials');
      }
    } catch (error) {
      setError('Invalid Credentials');
    }
  };

  return (
    <div className="container">
      <div className="row justify-content-center">
        <div className="col-md-4 form-container">
          <h2 className="mb-6 form-heading">LOGIN</h2>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">
              EMAIL
            </label>
            <input
              type="email"
              className="form-control"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">
              PASSWORD
            </label>
            <input
              type="password"
              className="form-control"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button className="btn-login" onClick={handleLogin}>
            Login
          </button>
          {error && <p className="text-danger mt-3">{error}</p>}
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
