export default function createEmployeesObject(departmentName, employees) {
  const MyObject = {
    [departmentName]: employees,
  };
  return MyObject;
}
