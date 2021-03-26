FROM ANL0KE/ICSS-USERBOT:latest

# نسخ رابط السورس 
RUN git clone https://github.com/ANL0KE/ICSS-USERBOT.git /root/userbot
# اخـراج العـمل 
WORKDIR /root/userbot

# لتنـزيل اضافات السورس
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
