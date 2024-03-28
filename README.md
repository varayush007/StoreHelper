# **🐱‍🚀STORE HELPER🐱‍🚀**

A Streamlit application that helps store owners answer questions about their inventory easily using natural language. This application leverages LangChain to combine the power of Large Language Models (LLMs) with a MySQL database.

**Key Features**

*   **Natural Language Queries:** Ask questions about your inventory in plain English (e.g., "How many t-shirts do we have left for Nike in XS size and white color?").
    
*   **SQL Generation:** The app translates your questions into SQL queries to retrieve accurate data.
    
*   **Informative Answers:** Provides clear and concise answers derived from the database results.
    

**Setup**

1.  **Clone the repository:**
    
    **Bash**
    
        git clone https://github.com/your-username/store-helper
    
2.  **Install dependencies:**
    
    **Bash**
    
        pip install -r requirements.txt
    
3.  **Set up environment variables:**
    
    *   Create a `.env` file in the project's root directory.
        
    *   Add the following variables, replacing the placeholders with your actual credentials:
        
    
        GOOGLE_API_KEY=<Your Google API Key>
        db_user=<Your MySQL Username>
        db_password=<Your MySQL Password>
        db_host=<Your MySQL Host>
        db_name=<Your MySQL Database Name>
        
    
4.  **Run the application:**
    
    **Bash**
    
        streamlit run main.py
    

**Usage**

1.  Open the Streamlit app in your web browser (typically at http://localhost:8501).
    
2.  Type your inventory-related question in the "Question" field.
    
3.  Click the "Submit" button to get the answer.
    

**Code Structure**

*   `main.py`: Contains the core Streamlit application logic.
    
*   `langchain_helper.py`: Houses functions for setting up the LangChain pipeline, including:
    
    *   **Few-Shot Prompting:** Provides examples (`few_shots.py`) to guide the LLM on how to interact with the database.
        
    *   **SQL Database Integration:** Connects to your MySQL database.
        
    *   **LLM (Google PaLM):** Used to understand questions and generate SQL queries.
        
    *   **Vector Store (Chroma):** Efficiently finds the most relevant examples for the question.
        

**Database Schema**

Ensure your MySQL database has a schema similar to the examples and references used in the `few_shots.py` file.


**DEMO**
![Screenshot (92)](https://github.com/varayush007/StoreHelper/assets/108609442/1a38068c-b831-4f94-a1e4-1203d6e9547b)

