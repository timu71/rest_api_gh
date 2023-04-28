# Builder image
FROM maven:3.8.4-jdk-17-slim AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src/ ./src/
RUN mvn package -DskipTests

# Release image
FROM openjdk:17-jdk-alpine3.14
WORKDIR /app
COPY --from=builder /app/target/demo-0.0.1-SNAPSHOT.jar ./app.jar
HEALTHCHECK --interval=30s --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost:8080/ || exit 1

CMD ["java", "-jar", "app.jar"]
