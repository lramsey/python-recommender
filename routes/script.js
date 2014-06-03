/* GET script page. */
exports.datum = function(req, res){
  var python = require('child_process').spawn(
    'python',
  ["./pyscript/init.py"]);
  output = '';
  python.stdout.on('data', function(data){
    output += data;
  });
  python.stdout.on('close', function(){
    res.send(output);
  });
};
