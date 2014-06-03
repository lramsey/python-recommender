/* GET script page. */
results = [];
exports.datum = function(req, res){
  if(results.length === 0){
    var python = require('child_process').spawn(
      'python',
    ["./pyscript/init.py"]);
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
