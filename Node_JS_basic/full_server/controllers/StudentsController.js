import readDatabase from "../utils.js";

class StudentsController {
  static async getAllStudents(req, res) {
    const databaseFile = process.argv[2]; // Récupère le fichier CSV au moment de l'exécution

    try {
      const studentsByField = await readDatabase(databaseFile);
      let responseText = "This is the list of our students";

      Object.keys(studentsByField)
        .sort()
        .forEach((field) => {
          const students = studentsByField[field];
          responseText += `\nNumber of students in ${field}: ${students.length}. List: ${students.join(", ")}`;
        });

      res.status(200).send(responseText);
    } catch (error) {
      res.status(500).send("Cannot load the database");
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const databaseFile = process.argv[2]; // Récupère le fichier CSV au moment de l'exécution
    const { major } = req.params;

    if (major !== "CS" && major !== "SWE") {
      res.status(500).send("Major parameter must be CS or SWE");
      return;
    }

    try {
      const studentsByField = await readDatabase(databaseFile);
      const students = studentsByField[major] || [];
      res.status(200).send(`List: ${students.join(", ")}`);
    } catch (error) {
      res.status(500).send("Cannot load the database");
    }
  }
}

export default StudentsController;
