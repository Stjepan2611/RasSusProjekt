FROM python:3.10.11-slim


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI runs on port 8000 by default, expose it
EXPOSE 8000

ENV MONGO_DB_URI=mongodb://mongo:27017/Recipes

# Run main.py with Uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]