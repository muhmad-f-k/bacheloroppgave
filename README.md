# bacheloroppgave

Developing Machine learning app for seaspray icing

#How to build and run docker image from scource.

1. git clone https://github.com/muhmad-f-k/bacheloroppgave
2. cd bacheloroppgave
3. docker build -t streamlit_app .
4. docker run -d -p 8501:8501 --name streamlit_app streamlit_app
5. docker logs streamlit_app -f
