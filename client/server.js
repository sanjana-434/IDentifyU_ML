const express = require('express');
const app = express();
const multer = require('multer');

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'D:/Lab_Main/Sem_5/ML/package/celebrity-classification/assets'); // Set the directory where you want to save the images
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + '-' + file.originalname);
  },
});

const upload = multer({ storage: storage });

app.post('/upload', upload.single('image'), (req, res) => {
  // The image has been saved in the 'uploads/' directory
  res.send('Image uploaded successfully');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
