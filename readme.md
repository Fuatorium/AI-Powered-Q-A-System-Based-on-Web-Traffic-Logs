# AI-Powered Q&A System Based on Web Traffic Logs

## Project Overview

This project involves the development of an AI-powered question-and-answer (Q&A) system that is based on web traffic logs, specifically Apache log files. The system is designed to take user queries in natural language, analyze the provided log data, and generate the most appropriate responses. The core of this system is built on the Retrieval-Augmented Generation (RAG) model, which combines the power of retrieval-based search with generative AI.


## Features

- **Log Analysis:** Efficiently processes and analyzes large Apache log files.
- **RAG Model:** Integrates a retrieval-based search with generative AI to provide relevant and context-aware answers.
- **OpenAI API Integration:** Leverages OpenAI's powerful API to generate natural language responses based on log data.
- **Scalable:** Capable of handling extensive log files and delivering prompt responses.


## Project Structure

- **`apache_logs.txt`**: The raw Apache log file that contains web server activity data.
- **`processed_logs.csv`**: A preprocessed version of the log data that is ready for retrieval operations.
- **`faiss_index.bin`**: The FAISS index file that stores vectorized log data for efficient retrieval.
- **`retrieval.py`**: Contains functions to load the FAISS index and retrieve relevant log entries based on user queries.
- **`generation.py`**: Integrates with the OpenAI API to generate natural language responses from the retrieved log data.
- **`rag_model.py`**: The main file that orchestrates the retrieval and generation processes to answer user queries.
- **`preprocess_and_faiss_index.py`**: Handles the preprocessing of raw log data and the creation of the FAISS index.


## Installation

1. **Install the required Python packages:** ```bash pip install -r requirements.txt ``` 

2. **Set up your OpenAI API key:** Replace `"YOUR_API_KEY"` in `rag_model.py` with your actual OpenAI API key. 


3. **Preprocess the log data and create the FAISS index:** ```bash python preprocess_and_faiss_index.py ```


## Usage

1. **Run the main program:** ```bash python rag_model.py ``` 

2. **Example Query:** 

When prompted, enter a query like: ```csharp What happened on August 10, 2024? ``` The system will process the query, retrieve relevant log entries, and generate an appropriate response.



## Project Workflow

**Data Preparation:** Apache log data is cleaned, processed, and vectorized. FAISS index is created for efficient retrieval of log data. 

**Retrieval-Augmented Generation (RAG) Model:** Retrieval: User queries are vectorized and matched against the FAISS index to retrieve relevant log entries. Generation: Retrieved logs are passed to the OpenAI API to generate context-aware responses. 

**System Integration and Testing:** The system is tested with various user queries to ensure accuracy and performance.



## Challenges Encountered

**Data Processing:** Parsing and vectorizing large Apache log files. 

**FAISS Index Creation:** Ensuring efficient search and retrieval from the FAISS index. 

**API Integration:** Seamlessly integrating the OpenAI API for natural language response generation.




## Performance and Accuracy

The system is optimized for handling large datasets and delivering prompt responses. Accuracy is evaluated based on the relevance of responses to the user queries.





## Future Enhancements

**Improved Data Processing:** Implementing advanced data processing techniques to enhance accuracy. 

**Extended Functionality:** Expanding the system to handle multiple types of log files and queries. 

**Enhanced API Integration:** Utilizing more sophisticated prompting techniques to improve response quality.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request. For major changes, please open an issue to discuss what you would like to change.
