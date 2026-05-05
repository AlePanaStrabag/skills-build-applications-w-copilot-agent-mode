// -8000.app.github.dev/api/activities
import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${baseUrl}/api/activities/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
      });
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Activities</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-light">
              <tr>
                <th>#</th>
                <th>User Email</th>
                <th>Activity</th>
                <th>Distance (km)</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((a, i) => (
                <tr key={i}>
                  <td>{i + 1}</td>
                  <td>{a.user_email}</td>
                  <td>{a.activity}</td>
                  <td>{a.distance}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Activities;
