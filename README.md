# Movies Recommendation Project
[live demo](https://movies-recommendation-5hiv.onrender.com)
## Overview

This project is a movie recommendation system built using the TMDb (The Movie Database) dataset. The recommendation system employs a similarity matrix created using the bag of words technique, calculating cosine similarities between pairs of movies.

## Features

- Movie Similarity Matrix: Utilizes the bag of words technique to establish a similarity matrix based on the cosine similarities between movies.
- Flask Web Application: The recommendation system is deployed on the web using Flask, providing an interactive user interface.
- Docker Integration: The project utilizes Docker for containerization, making it easy to deploy and run in various environments.

## How It Works

1. **Bag of Words Technique**: The project preprocesses the TMDb dataset and creates a bag of words representation for each movie.
2. **Cosine Similarities**: The similarity matrix is constructed by computing the cosine similarities between the bag of words representations of different movies.
3. **Flask Web Application**: The recommendation system is integrated into a Flask web application, allowing users to input preferences and receive personalized movie recommendations.
4. **Docker Deployment**: The entire project can be deployed as a Docker container, streamlining the setup process and ensuring consistent performance across different environments.

## Getting Started

### Prerequisites

- Python (version 3.10)
- Docker
- Flask

### Installation

1. Clone the repository: `git clone https://github.com/kunal-thakare-ai/movie_recommendation_flask.git`
2. Navigate to the project directory: `cd movie_recommendation_flask`
3. Install dependencies: `pip install -r requirements.txt`
4. Build the Docker image: `docker build -t movies-recommendation .`

### Usage

1. Run the Docker container: `docker run -p 5000:5000 movies-recommendation`
2. Access the application in your web browser at `http://localhost:5000`

## Additional Notes

Actual similarities matrix is not uploaded because of the large size, Instead top 5 picks for each movies are generated as dictionary.

Feel free to contribute or suggest improvements to enhance the functionality and user experience of the movie recommendation system.

## License

This project is licensed under the [MIT License](LICENSE).
