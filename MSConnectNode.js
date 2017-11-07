var sql = require("mssql");

var dbConfig = {
	server:"SHISHIRS",
	database:"EdinaLocal",
	user:"sa",
	password:"",
	port:1433
};

function getAddress(){
	var conn = new sql.Connection(dbConfig);
	conn.connect().then(function(){
		var req = new sql.Request(conn);
		req.query("Select address from tblSales").then(function(recordset){
			console.log(recordset);
			conn.close();
		})
		.catch(function(err){
			console.log(err);
			con.close();
		});
	})
	.cathc(function(err){
		console.log(err);
	});
}
getAddress();