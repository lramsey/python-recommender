/* GET script page. */
results = [];

var mockNames = 300;
var mockProducts = 100;
var mockMatrix = 'False';

var names =  JSON.stringify(['bob','randy','steve']);
var products = JSON.stringify(['starcraft','halflife','portal']);
var matrix = JSON.stringify([[1,1,1],[1,0,0],[0,1,1]]);

exports.datum = function(req, res){
  if(results.length > -1){
    var python = require('child_process').spawn(
      'python',
    ["./pyscript/exec.py", mockNames, mockProducts, mockMatrix]);
    output = '';
    python.stdout.on('data', function(data){
      output += data;
    });
    python.stdout.on('close', function(){
      results = output;
      res.send(results);
    });
  } else {
    res.send(results);
  }
};
