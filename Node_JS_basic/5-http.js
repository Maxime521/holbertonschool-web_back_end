// This module to create a small HTTP server using the http module

const http = require("http");
const countStudents = require("./3-read_file_async");

const databaseFile = process.argv[2];

const app = http.createServer(async (req, res) => {
  if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/plain" });
    return res.end("Hello Holberton School!");
  }

  if (req.url === "/students") {
    res.writeHead(200, { "Content-Type": "text/plain" });

    let reponseText = "This is the list of our students\n";

    try {
      const studentData = await countStudents(databaseFile); 
      reponseText += studentData;
    } catch (error) {
      reponseText += (error.message);
    }
    return res.end(reponseText.trimEnd());
  }

  res.writeHead(404);
  res.end("Not found");
});

app.listen(1245, () => {
  console.log("Server is running on port 1245");
});

module.exports = app;
