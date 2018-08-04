FROM python
EXPOSE 5000
COPY app.py . 
COPY req.txt . 
RUN pip3 install -r req.txt
ENTRYPOINT python3 app.py


