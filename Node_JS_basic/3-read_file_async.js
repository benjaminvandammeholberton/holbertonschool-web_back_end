const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const messages = [];
        let message;
        const content = data.toString().split('\n');
        let students = content.filter((item) => item);
        students = students.map((item) => item.split(','));
        const nStudents = students.length ? students.length - 1 : 0;
        message = `Number of students: ${nStudents}`;
        console.log(message);
        messages.push(message);
        const subjects = {};
        for (let i = 1; i < students.length; i += 1) {
          if (i !== 0) {
            if (!subjects[students[i][3]]) subjects[students[i][3]] = [];
            subjects[students[i][3]].push(students[i][0]);
          }
        }
        delete subjects.subject;
        for (const key of Object.keys(subjects)) {
          message = `Number of students in ${key}: ${
            subjects[key].length
          }. List: ${subjects[key].join(', ')}`;
          console.log(message);
          messages.push(message);
        }
        resolve(messages);
      }
    });
  });
}

module.exports = countStudents;
