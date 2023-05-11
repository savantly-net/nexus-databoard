# nexus-databoard

This application provides the boilerplate to rapidly build data applications on the streamlit framework (which is already rapid!).  


## Quick Start
There are a few options to get started rapidly.  

### Clone
Clone the repository, and do `pip install -r requirements.txt`  

You can add your own files to the [./pages](./pages) directory to add/replace the example pages.    
Then do `./run` or `streamlit run ./src/Home.py`  

### Docker Compose
Run the docker compose file to spin up the examples.  
You can also mount your own files in the `pages` directory in the app.  

### Extend the image
Extend the image and add your page files to the `pages` directory.  

Example - 
```
FROM savantly/nexus-databoard
COPY ./pages /app/src/pages/
```
