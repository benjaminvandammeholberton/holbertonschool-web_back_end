function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
  if (typeof city !== 'string') {
    throw new Error('city must be a string');
  }
  const studentByLocation = students.filter(
    (element) => element.location === city,
  );
  return studentByLocation;
}
module.exports = getStudentsByLocation;
