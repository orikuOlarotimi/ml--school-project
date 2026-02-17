# How to Run the ML Backend for React Native

## Prerequisites

1. Ensure you have Python 3 installed.
2.  2. Create a virtual environment and install dependencies:
       **Note**: We specifically use `tensorflow<2.16` to ensure compatibility with the `.h5` model format (Keras 2), as newer versions (Keras 3) may fail to load older models.

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/bMac
# On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Locally

Run the Flask server:

```bash
python app.py
```

This will start the server on `http://0.0.0.0:5000`.

## Connecting from React Native

### Option 1: Android Emulator

Use the special IP address `10.0.2.2` to access your local machine.

- URL: `http://10.0.2.2:5000/predict`

### Option 2: iOS Simulator

Use localhost.

- URL: `http://localhost:5000/predict`

### Option 3: Physical Device (Same Network)

Find your computer's local IP address (e.g., run `ifconfig` or check network settings).

- URL: `http://<YOUR_LOCAL_IP>:5000/predict`
- Ensure your firewall allows incoming connections on port 5000.

### Option 4: Tunneling (Using npx - Recommended)

If you have Node.js installed (typical for React Native), use `localtunnel` without installing extra software.

1. Run your Flask server: `python app.py`
2. In a new terminal:
    ```bash
    npx localtunnel --port 5000
    ```
3. Copy the URL (e.g., `https://funny-cat-42.loca.lt`) and use it in your app.

### Option 5: Tunneling (Using ngrok)

1. Install ngrok.
2. Run `ngrok http 5000`.
3. Use the HTTPS URL provided by ngrok.

## API Usage

- **Endpoint**: `/predict`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Body**:
    - `file`: The image file you want to predict.

Example fetch in React Native:

```javascript
const formData = new FormData();
formData.append("file", {
    uri: imageUri, // file path from image picker
    type: "image/jpeg",
    name: "upload.jpg",
});

const response = await fetch("http://YOUR_IP:5000/predict", {
    method: "POST",
    body: formData,
    headers: {
        "Content-Type": "multipart/form-data",
    },
});
const result = await response.json();
console.log(result);
```

## Cloud Hosting (Production)

### Deploy on Render (Recommended)

Render offers a generous free tier that should work for this project.

1.  **Push to GitHub**:
    Ensure this code is in a GitHub repository.
    Make sure `plant_disease_model.h5` and `disease_info(1).csv` are committed or available.

2.  **Sign up for Render**:
    Go to [render.com](https://render.com) and sign in with GitHub.

3.  **Create New Web Service**:
    - Click "New +" -> "Web Service".
    - Connect your repository.

4.  **Configure Service**:
    - **Name**: `plant-disease-api` (or similar)
    - **Region**: Choose closest to you.
    - **Branch**: `main` (or your default branch)
    - **Runtime**: Python 3
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`

5.  **Deploy**:
    - Click "Create Web Service".
    - Wait for the build to finish. Once you see "Your service is live", copy the URL (e.g., `https://plant-disease-api.onrender.com`).

6.  **Update React Native App**:
    - Replace your `localhost` or `localtunnel` URL with this new production URL.

**Note on Free Tier**:

- The free tier spins down after inactivity. The first request might take ~50 seconds to wake up.
- Tensorflow is a large library. If the build fails due to memory/slug size limits, consider using a smaller ML library or a paid instance, but for simple school projects, it usually fits if optimized.

### Option: Deploy with Docker (via Registry)

If you prefer to build the image locally and push it to a registry (like Docker Hub), follow these steps:

1.  **Configure Makefile**:
    Open the `Makefile` and change `REGISTRY_USER = codepraycode` to your Docker Hub username.

2.  **Login & Push**:

    ```bash
    docker login
    make all  # Builds, tags, and pushes to Docker Hub
    ```

3.  **Run Locally (Optional)**:

    ```bash
    make run
    ```

4.  **Deploy on Render**:
    - Go to Render Dashboard -> **New +** -> **Web Service**.
    - Select **"Deploy an existing image from a registry"**.
    - Enter your image URL: `docker.io/YOUR_USERNAME/plant-disease-api:latest`.
    - Click **Next** -> **Create Web Service**.

### Project Structure (Organized)

- `app.py`: Main Flask application entry point.
- `models/`: Contains the trained model file (`plant_disease_model.h5`).
- `data/`: Contains the disease info CSV (`disease_info.csv`).
- `scripts/`: Utility scripts:
    - `setup_env.sh`: Creates/updates the virtual environment.
    - `train_model.py`: Training script.
    - `verify_prediction.py`: Standalone test script.
- `notebooks/`: For Jupyter notebooks or experiments (`rag_experiment.py`).
- `tests/`: Test assets (`testimage.jpg`).
- `requirements.txt`: Python dependencies.
- `Dockerfile` & `Makefile`: Deployment configuration.
