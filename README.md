# IT & GIS Chatbot Usage Guide

## Prerequisites
- Python 3.12 installed
- Required Python packages installed (`fastapi`, `uvicorn`, `pydantic`)

## Running the Backend Server
1. Open a terminal.
2. Navigate to the project root directory.
3. Run the backend server with the command:
   ```
   python -m uvicorn backend.backend_free:app --host 127.0.0.1 --port 8000
   ```
4. The backend API will be available at `http://127.0.0.1:8000`.

## Using the Frontend Chatbot UI
1. Open the `frontend/index.html` file in a modern web browser (e.g., Chrome, Firefox).
2. The chatbot UI will load and greet you.
3. Type your message in the input box and click "Send" or press Enter.
4. The frontend will send your message to the backend API at `http://localhost:8000/chat`.
5. The chatbot will respond based on your input.

## Notes
- Ensure the backend server is running before using the frontend UI.
- If you want to run the frontend and backend on different hosts or ports, update the URL in `frontend/chatbot.js` accordingly.
- For production deployment, consider serving the frontend and backend via a web server or reverse proxy.

## Troubleshooting
- If the chatbot does not respond, check that the backend server is running and accessible.
- If you encounter CORS issues, backend CORS middleware may need to be added.

## Contact
For further assistance, please contact the development team.
