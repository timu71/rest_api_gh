const { application } = require('express')
const express = require('express')
const app =  express()
const port = 8080

app.get('/', (req, res) => {
    res.send('This is my first Node Application')
})

app.listen(port, () => {
    console.log('application is listening at http://localhost/${port}')
    
})