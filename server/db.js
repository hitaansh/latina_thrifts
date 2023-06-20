require("dotenv").config({path: '../.env'});
const Pool = require("pg").Pool;

process.env
const pool = new Pool({
  user: process.env.username,
  password: process.env.pass,
  host: process.env.hostname,
  port: process.env.port_id,
  database: "depop"
})

module.exports = pool
