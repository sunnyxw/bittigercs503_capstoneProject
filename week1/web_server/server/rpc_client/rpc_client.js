var jayson = require('jayson');
const config = require('../config/config.json');

// var ConfigClient = jayson.client.http({
//     port:4000,
//     hostname:'localhost'
// });

// function backendServerConfig(callback){
//     ConfigClient.request('backendServerConfig',[],function(err, error, response){
//         if (err) throw err;
//         // console.log(response);
//         // console.log(response.SERVER_HOST)
//         return callback(response);
//     });
// }

// console.log(backendServerConfig(function(response) {
//    res.json(response);
// }));

// var SERVER_PORT;
// var SERVER_HOST;

// ConfigClient.request('backendServerConfig', [], function(err, error, response){
//         if (err) throw err;
//         SERVER_PORT = response.SERVER_PORT;
//         SERVER_HOST = response.SERVER_HOST;
//         console.log(SERVER_PORT)
// })

var client = jayson.client.http({
    port: config.SERVER_PORT,
    hostname: config.SERVER_HOST
})

//Test RPC method
function add(a, b, callback){
    client.request('add', [a, b], function(err, error, response){
        if (err) throw err;
        console.log(response);
        callback(response);
    });
}

//get news summaries for a user.
function getNewsSummariesForUser(user_id, page_num, callback) {
  client.request('getNewsSummariesForUser', [user_id, page_num], function(err, error, response) {
    if (err) throw err;
    console.log(response);
    callback(response);
  });
}

// Log a news click event for a user
function logNewsClickForUser(user_id, news_id) {
    client.request('logNewsClickForUser', [user_id, news_id], function(err, error, response) {
        if (err) throw err;
        console.log(response);
    });
}

module.exports ={
    add: add,
    getNewsSummariesForUser: getNewsSummariesForUser,
    logNewsClickForUser: logNewsClickForUser
};