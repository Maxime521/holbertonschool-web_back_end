// This module to create a small HTTP server using Express module

const express = require("express");
const countStudents = require("./3-read_file_async");

const app = express();
const port = 1245;
const databaseFile = process.argv[2];

app.get("/", (req, res) => {
  res.set("Content-Type", "text/plain");
  res.send("Hello Holberton School!");
});

app.get("/students", async (req, res) => {
  res.set("Content-Type", "text/plain");

  let responseText = "This is the list of our students";

  try {
    const studentData = await countStudents(databaseFile);
    responseText += `\n${studentData}`;
  } catch (error) {
    responseText += `\n${error.message}`;
  }

  res.send(responseText.trimEnd());
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

module.exports = app;
