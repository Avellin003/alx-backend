import { createClient } from 'redis';

function redisConnect() {
  const con = createClient();

  con.on('connect', function() {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

};

function setNewSchool(schoolName, value) {
  con.set(schoolName, value, print);
};

function displaySchoolValue(schoolName) {
  con.get(schoolName, function(error, result) {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
