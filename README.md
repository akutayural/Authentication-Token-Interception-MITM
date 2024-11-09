# **Authentication Token Interception Program**

This project demonstrates how authentication tokens can be intercepted and stored by setting up a proxy to monitor network traffic. It leverages **mitmproxy** to intercept sensitive data from backend requests (like `/oauth/token`), showcasing potential security vulnerabilities that can arise in unprotected networks. The project stores intercepted tokens in **Redis** and is intended solely for educational and security awareness purposes.

**Note:** This project is designed to raise awareness about the importance of secure coding practices and network security. It should not be used for unauthorized access or malicious activities.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [Usage Guide](#usage-guide)
5. [How It Works](#how-it-works)
6. [Limitations & Warnings](#limitations--warnings)
7. [Live Demo and Blog](#live-demo-and-blog)
8. [Contributing](#contributing)
9. [License](#license)

---

## **Project Overview**

The purpose of this project is to demonstrate how insecure network practices can lead to the interception of sensitive data, such as authentication tokens. By simulating a **man-in-the-middle** (MITM) attack, this project highlights the importance of secure communication channels, HTTPS, and token handling.

This project uses **mitmproxy** to intercept HTTP/HTTPS requests sent to a backend authentication endpoint and extracts tokens or credentials from the intercepted data. The extracted tokens are then stored in **Redis** for analysis or further testing.

---

## **Features**

- **Proxy Interception with mitmproxy**: Intercepts traffic for specified endpoints (e.g., `/oauth/token`).
- **Redis Integration**: Stores intercepted tokens for secure handling and testing.
- **Custom Authentication**: Supports basic proxy authentication for controlled access.
- **Detailed Logging**: Logs intercepted data and authentication results for debugging and educational purposes.

---

## **Project Structure**

```plaintext
auth-token-interception/
├── proxy_server.py          # The main MITM script for intercepting tokens
├── README.md                # Documentation (this file)
```

## **Installation**

### **Prerequisites**

- **Python 3.11**: Ensure Python 3.11 is installed on your system.
- **Redis**: Redis is required to store intercepted tokens. [Download and install Redis](https://redis.io/download).
- **mitmproxy**: mitmproxy is required for network traffic interception. [Download mitmproxy](https://mitmproxy.org/).

### **Steps**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/auth-token-interception.git
   cd auth-token-interception
   ```
   
2. **Set Up a Virtual Environment and Install Python Dependencies**

   ```bash
   	python3.11 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
   ```
3. **Install mitmproxy and Redis**
   •	**Mitmproxy**
   ```bash
   	pip install mitmproxy
   ```
   •	**Redis** for macOS
   ```bash
   	brew install redis
   ```
   
## **Usage Guide**

### **Running the Proxy Script**

1. **Start mitmproxy with the Script**

   To start intercepting traffic, run mitmproxy with the provided script:

   ```bash
   mitmproxy --set console_eventlog_verbosity=debug -s proxy_server.py
   ```

2. **Configure Proxy in Your Application or Tool**
Set your application or testing tool (like curl, Postman) to route requests through mitmproxy. By default, mitmproxy listens on localhost:8080. Set your proxy configuration accordingly.

4. **Example Request**
Send a POST request to the authentication endpoint to see the interception in action:

   ```bash
   curl -x http://localhost:8080 -X POST \
  'https://user-auth-crru.onrender.com/oauth/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=testtest123&password=123456&scope=&client_id=string&client_secret=string'
  ```

After sending this request, mitmproxy will capture the request and response, allowing you to inspect them in real-time.















