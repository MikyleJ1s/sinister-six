const mysql = require('mysql')

const database = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Mikyle123',
    database: 'sanlam_data_and_digital_academy'
})

database.connect((error) => {
    if (error) throw error
    console.log('Connected to Database')
})

exports.getapplications = (req, res) => {
    database.query("select * from policies",
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.getpolicies = (req, res) => {
    database.query("select * from approvedpolicies",
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.getteams = (req, res) => {
    database.query("select * from teams",
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.searchteams = (req, res) => {
    database.query("select * from teams where technologies like ? or name like ? or description like ? or expectations like ?",
        ['%'+req.params.s+'%', '%'+req.params.s+'%', '%'+req.params.s+'%', '%'+req.params.s+'%'],
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })
    

}

exports.searchpolicies = (req, res) => {
    database.query("select * from approvedpolicies where policy_type = ? ",
        [req.params.s],
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.searchapplications = (req, res) => {
    database.query("select * from policies where policy_type = ? ",
        [req.params.s],
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.save_rotation = (req, res) => {
    jsondata = req.body;
    console.log(req.body)
    a = jsondata['graduate_name'];
    b = jsondata['user_identifier']
    c = jsondata['rotation_identifier'];
    d = jsondata['apply_date']
    database.query("insert into applications (graduate_name, user_identifier, rotation_identifier, apply_date) values (?, ?, ?, ?)",
        [a, b, c, d],
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.update_rotation_details = (req, res) => {
    jsondata = req.body;
    console.log(req.body)
    a = jsondata['name'];
    b = jsondata['technologies']
    c = jsondata['expectations'];
    d = jsondata['manager']
    e = jsondata['description']
    f = jsondata['rotation_identifier']
    database.query("update teams set name = ?, technologies = ?, expectations = ?, manager = ?, description = ? where rotation_identifier = ?",
        [a, b, c, d, e, f],
        function (err, result, fields) {
            if (err) {
                return err
            }
            return res.send(JSON.stringify(result))
        })

}

exports.unsave_rotation = (req, res) => {
    database.query("delete from policies where policy_identifier = ?",
        [req.params.i],
        function (error, result, fields) {
            if (error) throw error;
            return res.send(JSON.stringify(result))
        })
}