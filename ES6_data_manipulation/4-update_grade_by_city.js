function updateStudentGradeByCity(students, city, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }
  if (typeof city !== 'string') {
    throw new Error('city must be a string');
  }

  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find(
        (grade) => grade.studentId === student.id,
      );

      const updatedStudent = { ...student };

      if (matchingGrade) {
        updatedStudent.grade = matchingGrade.grade;
      } else {
        updatedStudent.grade = 'N/A';
      }

      return updatedStudent;
    });
}

module.exports = updateStudentGradeByCity;
