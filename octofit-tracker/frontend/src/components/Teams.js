import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', results);
      });
  }, [endpoint]);

  return (
    <div className="card mb-4 shadow-sm">
      <div className="card-body">
        <h2 className="card-title text-info mb-3">Teams</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>Name</th>
                <th>Members</th>
              </tr>
            </thead>
            <tbody>
              {teams.map((team, idx) => (
                <tr key={team.id || idx}>
                  <td>{team.name || '-'}</td>
                  <td>{Array.isArray(team.members) ? team.members.join(', ') : '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Teams;
