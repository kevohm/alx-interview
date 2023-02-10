#!/usr/bin/node
//prints all characters of a Star Wars movie
const request = require("request")
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function(error, response, body){
if(error){
	console.log(error)
}else{	
	JSON.parse(body).characters.forEach(
		(item)=>{
			request(item, function(error, response, body){
				if(!error){
					console.log(JSON.parse(body).name)
				}
			})
		}

	)
}
})

