/* GET script page. */
results = [];
names =  "['bob', 'randy', 'steve']";
products = "['starcraft', 'halflife', 'portal']";
matrix = "[[1,1,1],[1,0,0],[0,1,1]]";
exports.datum = function(req, res){
  if(results.length === 0){
    var python = require('child_process').spawn(
      'python',
    ["./pyscript/exec.py", names, products, matrix]);
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
