import express from "express";
import router from "./routes/index.js";

const app = express();
const port = 1245;

app.use("/", router); // 🔗 Associe les routes définies dans routes/index.js

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

export default app;
