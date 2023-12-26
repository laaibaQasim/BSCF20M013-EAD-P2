import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './studentList.css'

const StudentList = () => {
  const [students, setStudents] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [totalRows, setTotalRows] = useState(0);

  const [userRole, setUserRole] = useState('');

  useEffect(() => {
    const fetchUserRole = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/login');
        setUserRole(response.data.object);
      } catch (error) {
        console.error('Error fetching user role:', error);
      }
    };

    const fetchStudents = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/student?page=${currentPage}&page_size=${pageSize}`);
        setStudents(response.data.object);
      } catch (error) {
        console.error('Error fetching students:', error);
      }
    };

    fetchUserRole();
    fetchStudents();
  }, []);

  const navigate = useNavigate();

  const handleViewClick = (id) => {
    navigate(`/studentList/view/${id}`);
  };

  const handleUpdateClick = (id) => {
    if (userRole === 'student') {
      alert('You are not authorized to perform the update action.');
    }
    else if (userRole === 'admin'){
      navigate(`/studentList/update/${id}`);
    }
    else{
      navigate(`/`);
    }
  };
  const handleDeleteClick = async (id) => {
      if (userRole === 'student') {
        alert('You are not authorized to perform the delete action.');
      }
      else if (userRole === 'admin'){
        const isConfirmed = window.confirm('Are you sure you want to delete this student?');
        if (isConfirmed)
        {
          try {
            await axios.delete(`http://127.0.0.1:5000/student/${id}`);
            const response = await axios.get(`http://127.0.0.1:5000/student?page=${currentPage}&page_size=${pageSize}`);
            setStudents(response.data.object);
          } catch (error) {
            console.error('Error deleting student:', error);
          }
      }
      }
      else {
        navigate(`/`);
      }
  };

  useEffect(() => {
    fetchStudentList();
  }, [currentPage, pageSize]);

  const fetchStudentList = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/student?page=${currentPage}&page_size=${pageSize}`);
      console.log('API Response:', response.data);

      const studentsData = response.data.object || [];
      setStudents(studentsData);
      setTotalRows(response.data.total_rows);
    } catch (error) {
      console.error('Error fetching student list:', error);
    }
  };

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  const handlePageSizeChange = (e) => {
    // Ensure the entered value is a positive integer
    const enteredPageSize = parseInt(e.target.value, 10);
    if (!isNaN(enteredPageSize) && enteredPageSize > 0) {
      setPageSize(enteredPageSize);
    }
  };

  const handleLogout = async () => {
    try {
      await axios.post('http://127.0.0.1:5000/logout');
      console.log('Logout successful');
      setUserRole(NaN);
      navigate('/');
    } catch (error) {
      console.error('Error during logout:', error);
    }
  };

  return (
    <div className="container mt-5">
      <div className="topbar-div">
        <Link to="/dashboard" className="topbar">
          Dashboard
        </Link>
        |
        <Link to="/studentList/add" className="topbar">
          Add Student
        </Link>
        |
        <span className="topbar" onClick={handleLogout}>
          Logout
        </span>
      </div>
      {/* Pagination controls */}
      <div className="page-container">
        <div className="page-div">
          <label htmlFor="pageSize">Page Size</label>
          <input
            type="number"
            id="pageSize"
            className="form-control"
            value={pageSize}
            onChange={handlePageSizeChange}
            min="1"
          />
        </div>
      </div>
      <h2 className="mb-4">Student List</h2>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Roll Number</th>
            <th>Department</th>
            <th>Interest</th>
            <th>Degree</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student) => (
            <tr key={student.id}>
              <td>{student.id}</td>
              <td>{student.user.name}</td>
              <td>{student.roll_number}</td>
              <td>{student.department.name}</td>
              <td>{student.interest.name}</td>
              <td>{student.degree}</td>
              <td>
                <button className="btn-view" onClick={() => handleViewClick(student.id)}>
                  View
                </button>
                <button className="btn-update" onClick={() => handleUpdateClick(student.id)}>
                  Update
                </button>
                <button className="btn-delete" onClick={() => handleDeleteClick(student.id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="row justify-content-center mt-4">
        <div className="col-md-8 text-center btn-pages">
          <button
            className="btn btn-secondary mr-2"
            onClick={() => handlePageChange(1)}
            disabled={currentPage === 1}
          >
            First
          </button>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => handlePageChange(currentPage - 1)}
            disabled={currentPage === 1}
          >
            Prev
          </button>
          <span>Page {currentPage}</span>
          <button
            className="btn btn-secondary ml-2"
            onClick={() => handlePageChange(currentPage + 1)}
            disabled={currentPage * pageSize >= totalRows}
          >
            Next
          </button>
          <button
            className="btn btn-secondary mr-2 ml-2"
            onClick={() => handlePageChange(Math.ceil(totalRows / pageSize))}
            disabled={currentPage * pageSize >= totalRows}
          >
            Last
          </button>
        </div>
      </div>
    </div>
  );
};

export default StudentList;
