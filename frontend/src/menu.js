export function Menu() {
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
                <li><a href="/login" onClick={() => localStorage.clear()}>Logout</a></li>
            </ul>
        </div>
    );
}