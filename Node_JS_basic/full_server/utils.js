import fs from "fs/promises";

async function readDatabase(filePath) {
  return new Promise(async (resolve, reject) => {
    try {
      const data = await fs.readFile(filePath, "utf8");
      const rows = data.trim().split("\n").slice(1); // Exclure l'en-tête
      const studentsByField = {};

      rows.forEach((row) => {
        const columns = row.split(",");
        const firstname = columns[0];
        const field = columns[columns.length - 1];

        if (firstname && field) {
          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstname);
        }
      });

      resolve(studentsByField); // ✅ Retourne un objet avec les étudiants triés par domaine
    } catch (error) {
      reject(new Error("Cannot load the database")); // ✅ Rejette la promesse en cas d'erreur
    }
  });
}

export default readDatabase;
