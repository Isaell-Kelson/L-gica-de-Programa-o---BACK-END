const express = require('express');
const app = express();

app.get("/teste", function(req, res){
    res.send("Seja bem vindo!");
});

app.listen(8081, function(){
    console.log("Servidor funcionando normalmente na url http://localhost:8081");
});