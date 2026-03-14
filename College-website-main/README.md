Running the Project
Step 1 – Scrape Website Data
cd scraper
python notice_scraper.py

This will create:

data/notices.json
Step 2 – Create Vector Database
cd ../backend
python vector_store.py

This generates:

data/index.faiss
Step 3 – Start Backend Server
python app.py

Server will start at:

http://localhost:5000
Step 4 – Open the Website

Open the frontend in your browser:

frontend/index.html

You can now interact with the AI chatbot.

💬 Example Questions

Users can ask questions like:

What programs does the college offer?

How are placements at PVPIT?

What facilities are available on campus?

How can I contact the college?