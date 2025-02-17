import { useNavigate } from "react-router-dom";
import React, { useEffect, useState } from "react";

export default function LoginSelection() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Select Your Role</h1>
      <div className="space-x-4">
        <button onClick={() => navigate("/login/admin")} className="px-6 py-3 text-lg bg-blue-500 text-white rounded">
          Login as Admin
        </button>
        <button onClick={() => navigate("/login/employee")} className="px-6 py-3 text-lg bg-blue-500 text-white rounded">
          Login as Employee
        </button>
      </div>
    </div>
  );
}

export function AdminLogin() {
  const navigate = useNavigate();
  const handleLogin = (e) => {
    e.preventDefault();
    navigate("/menu");
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Admin Login</h1>
      <form className="flex flex-col space-y-4" onSubmit={handleLogin}>
        <input type="text" placeholder="Username" className="border p-2" />
        <input type="password" placeholder="Password" className="border p-2" />
        <button type="submit" className="px-6 py-3 text-lg bg-blue-500 text-white rounded">Login</button>
      </form>
    </div>
  );
}

export function EmployeeLogin() {
  const navigate = useNavigate();
  const handleLogin = (e) => {
    e.preventDefault();
    navigate("/menu");
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Employee Login</h1>
      <form className="flex flex-col space-y-4" onSubmit={handleLogin}>
        <input type="text" placeholder="Username" className="border p-2" />
        <input type="password" placeholder="Password" className="border p-2" />
        <button type="submit" className="px-6 py-3 text-lg bg-blue-500 text-white rounded">Login</button>
      </form>
    </div>
  );
}

export function Menu() {

      /*const [ user, setUser ] = useState( null );

    useEffect(() => {
        const fetchUserInfo = async () => {
            const token = localStorage.getItem( "token" )
            if( !token ) {
                window.location.href = "/login";
                return;
            }
        
        const response = await fetch( "http://127.0.0.1:5000/user-info", {
            method: "GET",
            headers: { Authorization: `Bearer ${token}` },
        });

        const data = await response.json();
        setUser( data );
        };

        fetchUserInfo();
    }, []);

    if( !user ) return <h2>Loading...</h2>;*/
    
    const navigate = useNavigate();
    const [ user, setUser ] = useState({
        name: "John Doe",
        role: "Employee",
    });
    
    const [showDashboardOptions, setShowDashboardOptions] = useState(false);
    
    return(
        <div>
            <h2>Welcome, {user.name}!</h2>
            <h3>Your Role: {user.role}</h3>

            <ul>
                <li>
                    <a href="#" onClick={() => setShowDashboardOptions( !showDashboardOptions )}>
                        Dashboard { showDashboardOptions ? "▲" : "▼" }
                    </a>
                </li>

                { showDashboardOptions && (
                    <ul>
                        {user.role === "Employee" && (
                            <>
                                <li><a href="#">ViewSchedule</a></li>
                                <li><a href="#">Clock In/Out</a></li>
                                <li><a href="#">View Timesheet</a></li>
                            </>
                        )}

                        {user.role === "Scheduler" && (
                            <>
                                <li><a href="#">Assign Shifts</a></li>
                                <li><a href="#">ManageSchedules</a></li>
                            </>
                        )}

                        {user.role === "Manager" && (
                            <>
                                <li><a href="#">Manage Employees</a></li>
                                <li><a href="#">Assign Roles</a></li>
                                <li><a href="#">View Reports</a></li>
                            </>
                        )}
                    </ul>
                )}

                <li><a href="#">Profile</a></li>
                <li><a href="#" onClick={() => { localStorage.clear(); navigate("/"); }}>Logout</a></li>
            </ul>
        </div>
    );
}