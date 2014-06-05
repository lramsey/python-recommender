/* GET script page. */
results = [];
names =  JSON.stringify(['bob','randy','steve']);
mockNames = 'False';
products = JSON.stringify(['starcraft','halflife','portal']);
mockProducts = 'False';
matrix = JSON.stringify([[1,1,1],[1,0,0],[0,1,1]]);
mockMatrix = 'False';
exports.datum = function(req, res){
  if(results.length === 0){
    var python = require('child_process').spawn(
      'python',
    ["./pyscript/exec.py", /*mockNames*/names, /*mockProducts*/products, /*mockMatrix*/matrix]);
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
