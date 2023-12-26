import React, { useEffect, useRef, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Chart from 'chart.js/auto';
import axios from 'axios';
import './dashboardPage.css'

const Dashboard = () => {
  const navigate = useNavigate();
  const [topInterests, setTopInterests] = useState([]);
  const [bottomInterests, setBottomInterests] = useState([]);
  const [provincialDistribution, setProvincialDistribution] = useState([]);
  const [interestCounts, setInterestCounts] = useState(0);

  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  const submissionChartRef = useRef(null);
  const submissionChartInstance = useRef(null);

  const tactivityDataRef = useRef(null);
  const tactivityDataInstance = useRef(null);

  const tfactivityDataRef = useRef(null);
  const tfactivityDataInstance = useRef(null);

  const ageDistributionDataRef = useRef(null);
  const ageDistributionDataInstance = useRef(null);

  const deptDataRef = useRef(null);
  const deptDataInstance = useRef(null);

  const degreeDataRef = useRef(null);
  const degreeDataInstance = useRef(null);

  const genderDataRef = useRef(null);
  const genderDataInstance = useRef(null);

  useEffect(() => {
    const fetchTopInterests = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/top-interests');
        const bottomInterestsResponse = await axios.get('http://127.0.0.1:5000/dashboard/bottom-interests');
        const interestCountsResponse = await axios.get('http://127.0.0.1:5000/interest');

        setTopInterests(response.data.object);
        setBottomInterests(bottomInterestsResponse.data.object);
        setInterestCounts(interestCountsResponse.data.total_rows);
        console.log(response.data.object)
      } catch (error) {
        console.error('Error fetching top interests:', error);
      }
    };

    fetchTopInterests();
  }, []);


  useEffect(() => {
    const fetchData = async () => {
      try {
        const distributionResponse = await axios.get('http://127.0.0.1:5000/dashboard/provincial-distribution');
        setProvincialDistribution(distributionResponse.data.object);
      } catch (error) {
        console.error('Error fetching provincial distribution:', error);
      }
    };

    fetchData();
  }, []);
  const distributionData = provincialDistribution;
  const labels = Object.keys(distributionData);
  const data = Object.values(distributionData);
  console.log(labels,data);
  useEffect (()=>{
    if (chartInstance.current){
      chartInstance.current.destroy()
    }
    const mychartRef = chartRef.current.getContext('2d');
    chartInstance.current = new Chart(mychartRef, {
      type:"pie",
      data:{
        labels,
        datasets: [
          {
            data,
            backgroundColor: [
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(153, 102, 255, 0.6)',
              'rgba(255, 159, 64, 0.6)',
            ],
          },
        ],
      }

    })
    return () => {
      if (chartInstance.current){
        chartInstance.current.destroy()
      }
    }
  },[labels, data]);


  const [submissionData, setSubmissionData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/submission-chart');
        setSubmissionData(response.data.object);
      } catch (error) {
        console.error('Error fetching submission data:', error);
      }
    };

    fetchData();
  }, []);
  const submissionLabels = submissionData.map((entry) => entry.date);
  const submissiondata = submissionData.map((entry) => entry.count);
  console.log(submissionLabels)
  console.log(submissiondata)
  useEffect (()=>{
    if (submissionChartInstance.current){
      submissionChartInstance.current.destroy()
    }
    const mychartRef = submissionChartRef.current.getContext('2d');
    submissionChartInstance.current = new Chart(mychartRef, {
      type:"line",
      data:{
        labels: submissionLabels,
        datasets: [
          {
            label:"Line Chart",
            data: submissiondata,
            fill:false,
            borderColor: 'rgb(75,192,192)',
            borderWidth:2,
          },
        ],
      }

    })
    return () => {
      if (submissionChartInstance.current){
        submissionChartInstance.current.destroy()
      }
    }
  },[submissionLabels, submissiondata]);


  const [tactivityData, setTActivityData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/last_30_days_activity');
        setTActivityData(response.data.object);
      } catch (error) {
        console.error('Error fetching activity data:', error);
      }
    };

    fetchData();
  }, []);
  const tactivityDataLabels = tactivityData.map((entry) => entry.date.split(' ')[0]);
  const tactivitydata = tactivityData.map((entry) => entry.count);
  console.log(tactivityDataLabels);
  console.log(tactivitydata);
  useEffect (()=>{
    if (tactivityDataInstance.current){
      tactivityDataInstance.current.destroy()
    }
    const mychartRef = tactivityDataRef.current.getContext('2d');
    tactivityDataInstance.current = new Chart(mychartRef, {
      type:"line",
      data:{
        labels: tactivityDataLabels,
        datasets: [
          {
            label:"Line Chart",
            data: tactivitydata,
            fill:false,
            borderColor: 'rgb(75,192,192)',
            borderWidth:2,
          },
        ],
      }
    })
    return () => {
      if (tactivityDataInstance.current){
        tactivityDataInstance.current.destroy()
      }
    }
  },[tactivityDataLabels, tactivitydata]);


  const [tfactivityData, setTfactivityData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/last_24_hours_activity');
        setTfactivityData(response.data.object);
      } catch (error) {
        console.error('Error fetching activity data:', error);
      }
    };

    fetchData();
  }, []);
  const tfactivityDataLabels = tfactivityData.map(entry => {
    const time = new Date(entry.time);
    const minutes = time.getMinutes();
    return minutes;
  });
  const tfactivitydata = tfactivityData.map((entry) => entry.count);
  console.log(tfactivityDataLabels);
  console.log(tfactivitydata);
  useEffect (()=>{
    if (tfactivityDataInstance.current){
      tfactivityDataInstance.current.destroy()
    }
    const mychartRef = tfactivityDataRef.current.getContext('2d');
    tfactivityDataInstance.current = new Chart(mychartRef, {
      type:"line",
      data:{
        labels: tfactivityDataLabels,
        datasets: [
          {
            label:"Line Chart",
            data: tfactivitydata,
            fill:false,
            borderColor: 'rgb(75,192,192)',
            borderWidth:2,
          },
        ],
      }
    })
    return () => {
      if (tfactivityDataInstance.current){
        tfactivityDataInstance.current.destroy()
      }
    }
  },[tfactivityDataLabels, tfactivitydata]);


  const [ageData, setAgeData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/age-distribution');
        setAgeData(response.data.object);
      } catch (error) {
        console.error('Error fetching submission data:', error);
      }
    };

    fetchData();
  }, []);
  const ageLabels = ageData.map((entry) => entry.age);
  const agedata = ageData.map((entry) => entry.count);
  console.log("age labels",ageLabels)
  console.log(agedata)
  useEffect (()=>{
    if (ageDistributionDataInstance.current){
      ageDistributionDataInstance.current.destroy()
    }
    const mychartRef = ageDistributionDataRef.current.getContext('2d');
    ageDistributionDataInstance.current = new Chart(mychartRef, {
      type:"bar",
      data:{
        labels: ageLabels,
        datasets: [
          {
            label:"Data",
            data: agedata,
            backgroundColor: [
            'rgba(255, 99, 132, 0.6)',
            'rgba(54, 162, 235, 0.6)',
            'rgba(255, 206, 86, 0.6)',
            'rgba(75, 192, 192, 0.6)',
            'rgba(153, 102, 255, 0.6)',
            'rgba(255, 159, 64, 0.6)',
            ],
          },
        ],
      }

    })
    return () => {
      if (ageDistributionDataInstance.current){
        ageDistributionDataInstance.current.destroy()
      }
    }
  },[ageLabels, agedata]);


  const [deptData, setDeptData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/department-distribution');
        setDeptData(response.data.object);
      } catch (error) {
        console.error('Error fetching provincial distribution:', error);
      }
    };
    fetchData();
  }, []);
  const deptLabels = deptData.map((entry) => entry.department);
  const deptdata = deptData.map((entry) => entry.count);
  console.log("department: ",deptLabels,deptdata);
  useEffect (()=>{
    if (deptDataInstance.current){
      deptDataInstance.current.destroy()
    }
    const mychartRef = deptDataRef.current.getContext('2d');
    deptDataInstance.current = new Chart(mychartRef, {
      type:"pie",
      data:{
        labels : deptLabels,
        datasets: [
          {
            data:deptdata,
            backgroundColor: [
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(153, 102, 255, 0.6)',
              'rgba(255, 159, 64, 0.6)',
            ],
          },
        ],
      }

    })
    return () => {
      if (deptDataInstance.current){
        deptDataInstance.current.destroy()
      }
    }
  },[deptLabels, deptdata]);


  const [degreeData, setDegreeData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/degree-distribution');
        setDegreeData(response.data.object);
      } catch (error) {
        console.error('Error fetching provincial distribution:', error);
      }
    };
    fetchData();
  }, []);
  const degreeLabels = degreeData.map((entry) => entry.degree);
  const degreedata = degreeData.map((entry) => entry.count);
  console.log("degree: ",degreeLabels,degreedata);
  useEffect (()=>{
    if (degreeDataInstance.current){
      degreeDataInstance.current.destroy()
    }
    const mychartRef = degreeDataRef.current.getContext('2d');
    degreeDataInstance.current = new Chart(mychartRef, {
      type:"pie",
      data:{
        labels : degreeLabels,
        datasets: [
          {
            data:degreedata,
            backgroundColor: [
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(153, 102, 255, 0.6)',
              'rgba(255, 159, 64, 0.6)',
            ],
          },
        ],
      }

    })
    return () => {
      if (degreeDataInstance.current){
        degreeDataInstance.current.destroy()
      }
    }
  },[degreeLabels, degreedata]);



  const [genderData, setGenderData] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/gender-distribution');
        setGenderData(response.data.object);
      } catch (error) {
        console.error('Error fetching provincial distribution:', error);
      }
    };
    fetchData();
  }, []);
  const genderLabels = genderData.map((entry) => entry.gender);
  const genderdata = genderData.map((entry) => entry.count);
  console.log("gender: ",degreeLabels,genderdata);
  useEffect (()=>{
    if (genderDataInstance.current){
      genderDataInstance.current.destroy()
    }
    const mychartRef = genderDataRef.current.getContext('2d');
    genderDataInstance.current = new Chart(mychartRef, {
      type:"pie",
      data:{
        labels : genderLabels,
        datasets: [
          {
            data:genderdata,
            backgroundColor: [
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(153, 102, 255, 0.6)',
              'rgba(255, 159, 64, 0.6)',
            ],
          },
        ],
      }

    })
    return () => {
      if (genderDataInstance.current){
        genderDataInstance.current.destroy()
      }
    }
  },[genderLabels, genderdata]);

  const [studentStatus, setStudentStatus] = useState({});
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/student/status');
        setStudentStatus(response.data.object);
      } catch (error) {
        console.error('Error fetching student status data:', error);
      }
    };

    fetchData();
  }, []);


  const [activityData, setActivityData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/dashboard/active-hours');
        setActivityData(response.data.object);
      } catch (error) {
        console.error('Error fetching activity data:', error);
      }
    };

    fetchData();
  }, []);


  const handleLogout = async () => {
    try {
      await axios.post('http://127.0.0.1:5000/logout');
      console.log('Logout successful');

      navigate('/');
    } catch (error) {
      console.error('Error during logout:', error);
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Student Interest System</h2>
      <div className="topbar-div">
        <Link to="/studentList" className="topbar">
          Student List
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
      {/* Dashboard Rows */}
      {/* row 1 */}
      <div className="row mb-4">
        {/* Col 1 */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Top 5 Interests</h5>
              <div className="boundary">
                <div className="interest-container">
                  {topInterests.map((interest, index) => (
                    <div key={index} className="interest-card">
                      <p className="card-text">
                        {interest.interest}
                      </p>
                    </div>
                  ))}
                </div>
                <br></br>
                <br></br>
                <h5>Bottom 5 Interests</h5>
                <div className="interest-container">
                  {bottomInterests.map((interest, index) => (
                    <div key={index} className="interest-card">
                      <p className="card-text">{interest.interest}</p>
                    </div>
                  ))}
                </div>
                <br></br>
                <br></br>
                <h5 className="card-title">Distinct Interests</h5>
                <p className="card-text big-font">{interestCounts}</p>
              </div>
            </div>
          </div>
        </div>

        {/* Col 2 */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Age Distribution</h5>
              <canvas ref={ageDistributionDataRef} style={{width:"100px", height:"200px"}}></canvas>
            </div>
          </div>
        </div>
      </div>

      {/* row 2 */}
      {/* Dashboard Rows */}
      <div className="row mb-4">
        {/* Col 1 */}
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Last 24 Hours Activity</h5>
              <canvas ref={tfactivityDataRef} style={{width:"100px", height:"100px"}}></canvas>
            </div>
          </div>
        </div>

        {/* Col 2 */}
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Students Created Daily in last 30 days</h5>
              <canvas ref={submissionChartRef} style={{width:"100px", height:"100px"}}></canvas>
            </div>
          </div>
        </div>

        {/* Col 3 */}
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title">Last 30 Days Activity</h5>
              <canvas ref={tactivityDataRef} style={{width:"100px", height:"100px"}}></canvas>
            </div>
          </div>
        </div>
      </div>

      {/* row 3 */}
      <div className="row mb-4">
              {/* Col 1 */}
              <div className="col-md-3">
                <div className="card">
                  <div className="card-body">
                      <h5 className="card-title">Provincial Distribution</h5>
                      <canvas ref={chartRef} style={{width:"100px", height:"100px"}}></canvas>
                  </div>
                </div>
              </div>

              {/* Col 2 */}
              <div className="col-md-3">
                <div className="card">
                  <div className="card-body">
                    <h5 className="card-title">Degree Distribution</h5>
                    <canvas ref={degreeDataRef} style={{width:"100px", height:"100px"}}></canvas>
                  </div>
                </div>
              </div>

              {/* Col 3 */}
              <div className="col-md-3">
                <div className="card">
                  <div className="card-body">
                      <h5 className="card-title">Department Distribution</h5>
                      <canvas ref={deptDataRef} style={{width:"100px", height:"100px"}}></canvas>
                  </div>
                </div>
              </div>

              {/* Col 4 - Add more cols as needed */}
              <div className="col-md-3">
                <div className="card">
                  <div className="card-body">
                      <h5 className="card-title">Gender Distribution</h5>
                      <canvas ref={genderDataRef} style={{width:"100px", height:"100px"}}></canvas>
                  </div>
                </div>
              </div>
      </div>

      {/* row 4 */}
      <div className="row mb-4">

        {/* Col 1 */}
        <div className="col-md-6">
          <div className="card">
            <div className="card-body">
              <h5 className="card-title"><u>Students Status</u></h5><br></br><br></br>
              <div className="grid-container">
                {Object.entries(studentStatus).map(([status, count]) => (
                  <div key={status} className="grid-item">
                    <h5>{status.replace(/_/g, ' ')}</h5>
                    <p>{count}</p>
                  </div>
                ))}
              </div>
            </div>
            </div>
        </div>

        {/* Col 2 */}
        <div className="col-md-4">
          <div className="card">
            <div className="card-body">
            <h5 className="card-title">Active Hours In Last 30 Days</h5>
            <div style={{ display: 'flex', flexDirection: 'row' }}>
              <div style={{ marginRight: '40px' }}>
                <p><b>MOST</b></p>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Hour</th>
                      <th>Count</th>
                    </tr>
                  </thead>
                  <tbody>
                    {activityData['Most Active Hours'] &&
                      activityData['Most Active Hours'].map((entry, index) => (
                        <tr key={index}>
                          <td>{entry.hour}</td>
                          <td>{entry.count}</td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              </div>

              <div style={{ marginRight: '40px' }}>
                <p><b>LEAST</b></p>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Hour</th>
                      <th>Count</th>
                    </tr>
                  </thead>
                  <tbody>
                    {activityData['Least Active Hours'] &&
                      activityData['Least Active Hours'].map((entry, index) => (
                        <tr key={index}>
                          <td>{entry.hour}</td>
                          <td>{entry.count}</td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              </div>

              <div style={{ marginRight: '40px' }}>
                <p><b>DEAD</b></p>
                <table border="1">
                  <thead>
                    <tr>
                      <th>Hour</th>
                      <th>Count</th>
                    </tr>
                  </thead>
                  <tbody>
                    {activityData['Dead Hours'] &&
                      activityData['Dead Hours'].map((hour, index) => (
                        <tr key={index}>
                          <td>{index}</td>
                          <td>{hour}</td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              </div>
            </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  );
};

export default Dashboard;
