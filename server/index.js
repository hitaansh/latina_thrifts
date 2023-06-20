const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./db");
app.use(express.json());

// Routes

//create a product
app.post("/create", async(req, res) => {
  try {
    console.log(req.body);
  } catch (err) {
    console.error(err.message);
  }
})

// Middleware 
app.use(cors());
app.use(express.json());

app.listen(6900, () => {
  console.log("server has started on port 6900");
});
