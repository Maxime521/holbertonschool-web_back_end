/* eslint-disable */
export default function getStudentIdsSum(students) {
    return students.reduce((add, student) => add + student.id, 0);
  }
