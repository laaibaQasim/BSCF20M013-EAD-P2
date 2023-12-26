import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import LoginPage from './pages/LoginPage/login';
import StudentList from './pages/StudentsPage/studentList';
import StudentForm from './pages/StudentsPage/studentForm';
import DashboardPage from './pages/DashboardPage/dashboardPage';
import ViewStudent from './pages/StudentsPage/studentView';


const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage/>}/>
        <Route path="/studentList" element={<StudentList />} />
        <Route path="/studentList/add" element={<StudentForm />} />
        <Route path="/studentList/view/:id" element={<ViewStudent />} />
        <Route path="/studentList/update/:id" element={<StudentForm />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
