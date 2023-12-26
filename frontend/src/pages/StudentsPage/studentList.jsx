import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './studentList.css'

const StudentList = () => {
  const [students, setStudents] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [pageSize, setPageSize] = useState(10);
  const [totalRows, setTotalRows] = useState(0);
  const [sortColumn, setSortColumn] = useState('id');
  const [sortDirection, setSortDirection] = useState('asc');
  const [userRole, setUserRole] = useState('');

  useEffect(()=>
  {
    logActivity("navigate", "User nagiated to /studentList");
  },[]);

  const logActivity = async (action, details) => {
    await axios.post('http://127.0.0.1:5000/log', {
      action,
      details,
    });
  };

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
      logActivity("naviagte","User navigated to /studentList/update");
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
  }, [currentPage, pageSize, sortColumn, sortDirection]);

  const fetchStudentList = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:5000/student?page=${currentPage}&page_size=${pageSize}&sort=${sortColumn}&direction=${sortDirection}`
        );
      console.log('API Response:', response.data);

      const studentsData = response.data.object || [];
      setStudents(studentsData);
      setTotalRows(response.data.total_rows);
    } catch (error) {
      console.error('Error fetching student list:', error);
    }
  };

  const handlePageChange = (newPage, bname) => {
    logActivity("Button click", "user clicked on " + bname + " button on page navigator");
    setCurrentPage(newPage);
  };

  const handlePageSizeChange = (e) => {
    // Ensure the entered value is a positive integer
    const enteredPageSize = parseInt(e.target.value, 10);
    if (!isNaN(enteredPageSize) && enteredPageSize > 0) {
      logActivity("enter", "User changed page size");
      setPageSize(enteredPageSize);
    }
  };

  const handleSort = (column) => {
    if (column === sortColumn) {
      // Toggle the sort direction if the same column is clicked again
      setSortDirection((prevDirection) => (prevDirection === 'asc' ? 'desc' : 'asc'));
      logActivity("Sort direction", "user changed sort direction");
    } else {
      // Set a new column for sorting with the default ascending direction
      logActivity("Sort", "user set " + column + " for sorting");
      setSortColumn(column);
      setSortDirection('asc');
    }
  };

  const handleLogout = async () => {
    try {
      logActivity("logout", "User logged out of the system")
      await axios.post('http://127.0.0.1:5000/logout');
      console.log('Logout successful');
      setUserRole(NaN);
      navigate('/');
    } catch (error) {
      console.error('Error during logout:', error);
    }
  };
  const handleAdd = async () => {
    if (userRole === "admin"){
      navigate('/studentList/add');
    }
  else {
    alert('You are not authorized to perform this action.');
  }
  };

  return (
    <div className="container mt-5">
      <div className="topbar-div">
        <Link to="/dashboard" className="topbar">
          Dashboard
        </Link>
        |
        <span className="topbar" onClick={handleAdd}>
          Add Student
        </span>
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
          <th onClick={() => handleSort('id')}>
            ID {sortColumn === 'id' && (sortDirection === 'asc' ? '↑' : '↓')}
          </th>
          <th onClick={() => handleSort('user.name')}>
            Name {sortColumn === 'user.name' && (sortDirection === 'asc' ? '↑' : '↓')}
          </th>
          <th onClick={() => handleSort('roll_number')}>
            Roll Number {sortColumn === 'roll_number' && (sortDirection === 'asc' ? '↑' : '↓')}
          </th>
          <th onClick={() => handleSort('department.name')}>
            Department {sortColumn === 'department.name' && (sortDirection === 'asc' ? '↑' : '↓')}
          </th>
          <th onClick={() => handleSort('interest.name')}>
            Interest {sortColumn === 'interest.name' && (sortDirection === 'asc' ? '↑' : '↓')}
          </th>
          <th onClick={() => handleSort('degree')}>
            Degree {sortColumn === 'degree' && (sortDirection === 'asc' ? '↑' : '↓')}
          </th>
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
            onClick={() => handlePageChange(1, "first")}
            disabled={currentPage === 1}
          >
            First
          </button>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => handlePageChange(currentPage - 1, "prev")}
            disabled={currentPage === 1}
          >
            Prev
          </button>
          <span>Page {currentPage}</span>
          <button
            className="btn btn-secondary ml-2"
            onClick={() => handlePageChange(currentPage + 1, "next")}
            disabled={currentPage * pageSize >= totalRows}
          >
            Next
          </button>
          <button
            className="btn btn-secondary mr-2 ml-2"
            onClick={() => handlePageChange(Math.ceil(totalRows / pageSize), "last")}
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
