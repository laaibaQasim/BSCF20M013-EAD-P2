import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ViewStudent = () => {
  const [student, setStudent] = useState({});
  const { id } = useParams();

  useEffect(() => {
    const fetchStudentData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/student/${id}`);
        setStudent(response.data.object);
      } catch (error) {
        console.error('Error fetching student data:', error);
      }
    };

    fetchStudentData();
  }, [id]);

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Student Details</h2>
      {student && student.user && (
        <div className="card">
          <div className="card-body">
            <p className="card-text border-bottom"><b>ID: </b> {student.id}</p>
            <p className="card-text border-bottom"><b>NAME: </b> {student.user.name}</p>
            <p className="card-text border-bottom"><b>EMAIL: </b> {student.user.email}</p>
            <p className="card-text border-bottom"><b>ROLL NUMBER: </b> {student.roll_number}</p>
            <p className="card-text border-bottom"><b>CITY: </b> {student.city}</p>
            <p className="card-text border-bottom"><b>DOB: </b> {student.dob}</p>
            <p className="card-text border-bottom"><b>DEPARTMENT: </b> {student.department && student.department.name}</p>
            <p className="card-text border-bottom"><b>INTEREST: </b> {student.interest && student.interest.name}</p>
            <p className="card-text border-bottom"><b>DEGREE: </b> {student.degree}</p>
            <p className="card-text border-bottom"><b>START DATE: </b> {student.start_date}</p>
            <p className="card-text border-bottom"><b>END DATE: </b> {student.end_date}</p>
          </div>
        </div>
      )}

      {/* Back button with Bootstrap styling */}
      <button className="btn btn-secondary mt-3" onClick={() => window.history.back()}>
        Back
      </button>
    </div>
  );
};

export default ViewStudent;
