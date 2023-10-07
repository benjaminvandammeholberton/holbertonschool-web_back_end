function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const studentId = students.map((element) => element.id);
  return studentId;
}

module.exports = getListStudentIds;
