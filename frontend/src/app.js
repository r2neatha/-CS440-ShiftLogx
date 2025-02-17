import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginSelection, { AdminLogin, EmployeeLogin, Menu } from "./LoginSelection";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginSelection />} />
        <Route path="/login/admin" element={<AdminLogin />} />
        <Route path="/login/employee" element={<EmployeeLogin />} />
        <Route path="/menu" element={<Menu />} />
      </Routes>
    </Router>
  );
}

export default App;
