module.exports = (app) => {
    const controller = require('../controllers/controller.js')
    app.get('/get_applications', controller.getapplications)
    app.get('/get_teams', controller.getteams)
    app.get('/get_policies', controller.getpolicies)
    app.post('/update_rotation_details', controller.update_rotation_details)
    app.get('/search_applications/:s', controller.searchapplications)
    app.get('/search_teams/:s', controller.searchteams)
    app.post('/save_rotation', controller.save_rotation)
    app.delete('/unsave_rotation/:i', controller.unsave_rotation)
}

