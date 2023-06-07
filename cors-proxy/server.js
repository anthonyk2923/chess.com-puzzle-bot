const express = require('express');
const app = express();
const fetch = require('node-fetch');
const cors = require('cors');

app.use(cors());

app.get('/', async (req, res) => {
  const response = await fetch(
    'https://www.chess.com/callback/tactics/rated/next'
  );
  const data = await response.json();
  res.json(await data);
});

app.listen(3000, () => {
  console.log('listening on port 3000');
});
