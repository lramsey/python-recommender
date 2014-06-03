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
            customers = data[0];
            customersMap = data[1];
            productClusters = data[2];
            $scope.unfiltered = data[3];
            $scope.filtered = data[4];
            powerClusters = data[5];
            recommendationMatrix = data[6];
        });
    })();

    $scope.recommender = function(){
        if(customersMap && customersMap[$scope.name] !== undefined){
            recommendation = recommendationMatrix[customersMap[$scope.name]].pop();
            attraction = Object.keys(recommendation)[0];
            indexes = recommendation[attraction];
            cluster = powerClusters[indexes[1]];
            indexMap = cluster[3];
            product = indexMap[indexes[0]];
            console.log(customers[0] + ' should buy ' + product + '.');
        } else {
            console.log(customersMap);
            console.log(customersMap[$scope.name]);
            console.log('That customer is not in our records.');
        }
    };
});