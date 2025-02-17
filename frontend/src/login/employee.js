// employee.js
export function EmployeeLogin() {
  const navigate = useNavigate();
  const handleLogin = () => navigate("/menu");
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