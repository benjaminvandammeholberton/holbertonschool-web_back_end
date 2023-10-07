function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const sumIndex = students.reduce((total, student) => total + student.id, 0);
  return sumIndex;
}
module.exports = getStudentIdsSum;
