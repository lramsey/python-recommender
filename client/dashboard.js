var app = angular.module("dashboard",[]);

app.controller('retrieveDatum', function($scope, $http){
    console.log('module online');
    $scope.unfiltered = 'unfiltered results';
    $scope.filtered = 'filtered results';
    var customers;
    var customersMap;
    var productClusters;
    var powerClusters;
    var recommendationMatrix;
    (function(){
        $http.get('/script').success(function(data){
            console.log(data);
            customers = data[0];
            customersMap = data[1];
            productClusters = data[2];
            console.log(data[3]);
            $scope.unfiltered = data[3];
            $scope.filtered = data[4];
            powerClusters = data[5];
            recommendationMatrix = data[6];
        });
    })();

    $scope.recommender = function(){
        if(customersMap && customersMap[$scope.name] !== undefined){
            var customerRecs = recommendationMatrix[customersMap[$scope.name]];
            if (customerRecs.length > 0){
                var recommendation = recommendationMatrix[customersMap[$scope.name]].pop();
                var attraction = Object.keys(recommendation)[0];
                var indexes = recommendation[attraction];
                var cluster = powerClusters[indexes[1]];
                var indexMap = cluster[3];
                var product = indexMap[indexes[0]];
                console.log(indexMap);
                console.log($scope.name + ' should buy ' + product + '.');
            } else {
                console.log('things are recommended');
            }
        } else {
            console.log(customersMap);
            console.log('That customer is not in our records.');
        }
    };
});