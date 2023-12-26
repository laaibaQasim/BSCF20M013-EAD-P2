import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import axios from 'axios';
import './studentForm.css'

const StudentForm = () => {
  const [name, setName] = useState('');
  const [roll_number, setRollNumber] = useState('');
  const [email, setEmail] = useState('');
  const [gender, setGender] = useState('Male');
  const [dob, setDob] = useState(null);
  const [city, setCity] = useState('');
  const [interest, setInterest] = useState('');
  const [department, setDepartment] = useState('');
  const [degree, setDegree] = useState('');
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);

  const [cities, setCities] = useState([]);
  const [interests, setInterests] = useState([]);
  const [departments, setDepartments] = useState([]);
  const [degrees, setDegrees] = useState([]);
  const [customInterest, setCustomInterest] = useState('');

  const { id } = useParams();
  const isUpdateMode = id !== undefined;
  const navigate = useNavigate();

  useEffect(()=>
  {
    logActivity("navigate", "User nagiated to /studentList/view");
  },[]);

  const logActivity = async (action, details) => {
    await axios.post('http://127.0.0.1:5000/log', {
      action,
      details,
    });
  };

  useEffect(() => {
    // Fetch cities, interests, departments, and degrees from the backend API
    const fetchData = async () => {
      try {
        const citiesResponse = await axios.get('http://127.0.0.1:5000/student/cities');
        const interestsResponse = await axios.get('http://127.0.0.1:5000/interest');
        const departmentsResponse = await axios.get('http://127.0.0.1:5000/department');
        const degreesResponse = await axios.get('http://127.0.0.1:5000/student/degrees');

        const deptnames = departmentsResponse.data.object.map(department => department.name);
        setInterests(interestsResponse.data.object.map(interest => interest.name));
        setCities(citiesResponse.data.object);
        setDepartments(deptnames);
        setDegrees(degreesResponse.data.object);

        if (isUpdateMode) {
          const studentResponse = await axios.get(`http://127.0.0.1:5000/student/${id}`);
          const studentData = studentResponse.data.object;

          setName(studentData.user.name);
          setRollNumber(studentData.roll_number);
          setEmail(studentData.user.email);
          setGender(studentData.gender);
          setDob(new Date(studentData.dob));
          setCity(studentData.city);
          setInterest(studentData.interest.name);
          setDepartment(studentData.department.name);
          setDegree(studentData.degree);
          setStartDate(studentData.start_date ? new Date(studentData.start_date) : null);
      setEndDate(studentData.end_date ? new Date(studentData.end_date) : null);
        }

      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, [id, isUpdateMode]);

  const handleConfirm = async () => {
    if (id){
      var intId = parseInt(id)
    }
    else {
      var intId = 0
    }
    const studentData = {
      id:intId,
      user: {
        name,
        email,
      },
      roll_number,
      department: {
        name: department
      },
      degree,
      dob: dob.toISOString().split('T')[0],
      city,
      interest: {
        name: interest,
      },
      gender,
      start_date: startDate.toISOString().split('T')[0],
      end_date: endDate.toISOString().split('T')[0],
    };
    console.log('Request Payload:', studentData);
    try {
      if (id) {
        // Update existing student
        await axios.patch(`http://127.0.0.1:5000/student/${id}`, studentData);
      } else {
        // Insert new student
        await axios.post('http://127.0.0.1:5000/student', studentData);
      }
    } catch (error) {
      console.error('Error updating/inserting student:', error);
    }
    navigate('/studentList')
  };

  return (
    <div className='form-container'>
      <div className='form-row'>
        <div className='form-field'>
          <label htmlFor="name">FULL NAME</label>
          <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} />
        </div>
        <div className='form-field'>
          <label htmlFor="roll_number">ROLL NUMBER</label>
          <input type="text" id="roll_Number" value={roll_number} onChange={(e) => setRollNumber(e.target.value)} />
        </div>
      </div>

      <div className='form-row'>
        <div className='form-field'>
          <label htmlFor="email">EMAIL</label>
          <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </div>
        <div className='form-field'>
          <label htmlFor="gender">GENDER</label>
          <select id="gender" value={gender} onChange={(e) => setGender(e.target.value)}>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
      </div>

      <div className='form-row'>
        <div className='form-field'>
          <label htmlFor="dob">DATE OF BIRTH</label>
          <DatePicker id="dob" selected={dob} onChange={(date) => setDob(date)} />
        </div>
        <div className='form-field'>
          <label htmlFor="city">CITY</label>
          <select id="city" value={city} onChange={(e) => setCity(e.target.value)}>
            {cities.map((city,index) => (
              <option key={index} value={city}>{city}</option>
            ))}
          </select>
        </div>
      </div>

      <div className='form-row'>
        <div className='form-field'>
          <label htmlFor="interest">INTEREST</label>
          <select id="interest" value={interest} onChange={(e) => setInterest(e.target.value)}>
            {interests.map((interest, index) => (
              <option key={index} value={interest}>{interest}</option>
            ))}
            <option value="other">Other</option>
          </select>
          {interest === 'other' && (
            <div className='other-field'>
              <label htmlFor="customInterest">ENTER YOUR OWN INTEREST</label>
              <input
                type="text"
                id="customInterest"
                value={customInterest}
                onChange={(e) => setCustomInterest(e.target.value)}
              />
            </div>
          )}
        </div>
      </div>

      <div className='form-row'>
        <div className='form-field'>
          <label htmlFor="department">DEPARTMENT</label>
          <select id="department" value={department} onChange={(e) => setDepartment(e.target.value)}>
            {departments.map((dept, index) => (
              <option key={index} value={dept}>{dept}</option>
            ))}
          </select>
        </div>
        <div className='form-field'>
          <label htmlFor="degree">DEGREE</label>
          <select id="degree" value={degree} onChange={(e) => setDegree(e.target.value)}>
            {degrees.map((degree, index) => (
              <option key={index} value={degree}>{degree}</option>
            ))}
          </select>
        </div>
      </div>

      <div className='form-row'>
        <div className='form-field'>
          <label htmlFor="startDate">START DATE</label>
          <DatePicker id="startDate" selected={startDate} onChange={(date) => setStartDate(date)} />
        </div>
        <div className='form-field'>
          <label htmlFor="endDate">END DATE</label>
          <DatePicker id="endDate" selected={endDate} onChange={(date) => setEndDate(date)} />
        </div>
      </div>

      <button className = 'confirm-button' onClick={handleConfirm}>Confirm</button>
    </div>
  );
};

export default StudentForm;
