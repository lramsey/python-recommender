var app = angular.module("dashboard",[]);

app.controller('retrieveDatum', function($scope, $http){
    console.log('module online');
    $scope.fetchData = function(){
        console.log('hello world');
        $http.get('/script').success(function(data){
            console.log(data);
        });
    };
});