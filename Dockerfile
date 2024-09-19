# Используем официальный образ Python в качестве базового образа

FROM python
# Set the locale

RUN apt update

RUN apt upgrade
ENV PYTHONIOENCODING=utf-8
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8   
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app
# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt ./
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt
