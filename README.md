# Developing Machine learning app for seaspray icing

The AI research group at UiT Narvik has recently developed a machine learning model that can predict the amount of ice that forms and the icing rate on offshore structures and vessels. The model includes a range of different methods for analyzing data at various stages of the experiment, making it a powerful tool for those working in this field. One potential application of this model is in the context of seaspray icing experiments. These experiments are designed to test the effects of icing on offshore structures and vessels and having an easy-to-use app for the model could greatly assist in these experiments. With the help of this app, researchers would be able to quickly and easily access the model and input data, allowing them to make more accurate predictions and better understand the effects of icing on offshore structures. The project can be split into two main phases: design and implementation. During the design phase, the candidates will be responsible for creating an app that incorporates the developed machine learning functionality in an intuitive way. The app should be able to collect data during laboratory experiments and provide related analysis in the form of charts and tables. For the implementation phase, the candidates can use frameworks like Streamlit, Gradio, or Jina, using the Python programming language. These frameworks will help them to quickly and easily create an app that is able to effectively use the machine learning model to predict the amount of ice formed and the icing rate on offshore structures and vessels. The picture below the schematic illustrates of the current system and the way the task is being performed manually.


#### How to build and run docker image from scource.

```
1. git clone https://github.com/muhmad-f-k/bacheloroppgave
2. cd bacheloroppgave
3. docker build -t streamlit_app .
4. docker run -d -p 8501:8501 --name streamlit_app streamlit_app
5. docker logs streamlit_app -f
6. To access the website go to http://server-IP:8501
7. Test Website at http://198.46.190.55:8501/
```



