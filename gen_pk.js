var crypto = require('crypto');

var id = crypto.randomBytes(32).toString('hex');
var privateKey = "0x"+id;
console.log("SAVE BUT DO NOT SHARE THIS:", privateKey)