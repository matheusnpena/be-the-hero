const express = require("express");
const cors = require('cors');
const routes = require('./routes');

const app = express();

app.use(cors());
app.use(express.json());
app.use(routes);

/*
Tipo de parametros:

Query: Parametros nomeados enviados na rota após "?"
Route: Parametros utilizados para identificar recursos (rota)
Request Body: corpo da requisição. Utilizado para criar ou alterar recursos
*/

app.listen(3333);

