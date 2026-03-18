FROM python:3.8

# Set working directory
WORKDIR /POSTWORK/Beams_and_Brackets_Safety_Validator

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy CLI tool
COPY cli ./cli

# Set entry point
ENTRYPOINT ["python", "-m", "cli.main"]