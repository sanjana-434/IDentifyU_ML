import React, { useState, useRef } from 'react';
import Webcam from 'react-webcam';
import download from 'downloadjs';

function CameraApp() {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);

  const [capturedImage, setCapturedImage] = useState(null);

  const capture = () => {
    const webcam = webcamRef.current;
    const canvas = canvasRef.current;

    if (webcam && canvas) {
      const context = canvas.getContext('2d');
      canvas.width = webcam.video.videoWidth;
      canvas.height = webcam.video.videoHeight;

      context.drawImage(webcam.video, 0, 0, canvas.width, canvas.height);
      canvas.toBlob((blob) => {
        download(blob, 'captured-image', 'image/jpeg');
        setCapturedImage(URL.createObjectURL(blob));
      }, 'image/jpeg');
    }
  };

  const resetCapture = () => {
    setCapturedImage(null);
  };

  return (
    <div>
      {capturedImage ? (
        <div>
          <img src={capturedImage} alt="Captured" />
          <button onClick={resetCapture}>CLOSE!</button>
        </div>
      ) : (
        <div>
          <Webcam
            ref={webcamRef}
            videoConstraints={{ width: 1280, height: 655 }}
          />
          <button onClick={capture}>SNAP!</button>
        </div>
      )}
      <canvas ref={canvasRef} style={{ display: 'none' }} />
    </div>
  );
}

export default CameraApp;
