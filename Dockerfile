FROM eclipse-temurin:11-jre-jammy

ARG JYTHON_VERSION=2.7.4
ENV LANG=C.UTF-8

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && curl -fL "https://repo1.maven.org/maven2/org/python/jython-standalone/${JYTHON_VERSION}/jython-standalone-${JYTHON_VERSION}.jar" -o /opt/jython.jar \
    && apt-get purge -y --auto-remove curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY exemplo1.py exemplo2.py ./

CMD ["sh", "-c", "set -e; echo '=== Exemplo 1: java.io + java.util ==='; java -jar /opt/jython.jar exemplo1.py; echo; echo '=== Exemplo 2: Threads da JVM ==='; java -jar /opt/jython.jar exemplo2.py"]
