// Use displayMessage function to print a message to the console.
const http = require("http");

const port = 1245;

const app = http.createServer((req, res) => {
  res.writeHead(200);
  res.end("Hello Holberton School!");
});

app.listen(port, () => {
  console.log(`Server is listening on port 1245`);
});

module.exports = app;