const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8').trim();

    if (!data) {
      throw new Error('Cannot load the database');
    }

    const lines = data.split('\n').filter(line => line.trim() !== '');
    const students = lines.slice(1);

    console.log(`Number of students: ${students.length}`);

    const fields = {};

    students.forEach(line => {
      const studentData = line.split(',');
      const name = studentData[0];
      const field = studentData[studentData.length - 1];

      if(!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(name);
    });
    Object.entries(fields).forEach(([field, names]) => {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    });
  } catch (error) {
    throw new Error(`Cannot load the database`);
  }
}

module.exports = countStudents;
