var express = require('express');
const { spawn } = require('child_process');
var router = express.Router();


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get("/feed", (req, res, next) => {
  console.log("executing")
  const motorScript = spawn("python", ["/home/kandi/Documents/animal-entertainment/feed_motor.py"])
  
    motorScript.stderr.on("data", (err) => {
      console.log(err.toString())
    })
  
  return res.status(200)
})

router.get("/right", (req, res, next) => {
  console.log("executing")
  const motorScript = spawn("python", ["/home/kandi/Documents/animal-entertainment/toy_right_motor.py"])
  
    motorScript.stderr.on("data", (err) => {
      console.log(err.toString())
    })
  
  return res.status(200)
})

router.get("/left", (req, res, next) => {
  console.log("executing")
  const motorScript = spawn("python", ["/home/kandi/Documents/animal-entertainment/toy_left_motor.py"])
  
    motorScript.stderr.on("data", (err) => {
      console.log(err.toString())
    })
  
  return res.status(200)
})
module.exports = router;
